import subprocess
import platform
import os
import stat

def get_binary(name):
    system = platform.system().lower()
    ext = ".exe" if system == "windows" else ""
    folder = "macos" if system == "darwin" else system
    base = os.path.dirname(__file__)
    binary = os.path.join(base, "bins", folder, f"{name}{ext}")
    
    if not os.path.exists(binary):
        raise FileNotFoundError(f"Binary not found: {binary}")
    
    if os.name != "nt":  # Not Windows
        try:
            mode = os.stat(binary).st_mode
            if not (mode & stat.S_IEXEC):
                os.chmod(binary, mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
        except (OSError, PermissionError):
            pass  # Best effort only
    
    return binary

class DSBridge:
    def __init__(self, name):
        self.name = name
        binary = get_binary(name)
        self.proc = subprocess.Popen(
            [binary],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        ready_line = self.proc.stdout.readline().strip()
        if not ready_line:
            stderr_tail = self._read_stderr()
            raise RuntimeError(
                f"Binary '{name}' produced no output (crashed?). "
                f"Stderr: {stderr_tail or '(empty)'}"
            )
        if ready_line != "READY":
            raise RuntimeError(f"Expected READY from '{name}', got: {ready_line}")

    def _read_stderr(self):
        try:
            return self.proc.stderr.read().strip()
        except Exception:
            return None

    def is_alive(self) -> bool:
        return self.proc.poll() is None

    def send(self, command):
        if not self.is_alive():
            raise RuntimeError("Process terminated")

        try:
            self.proc.stdin.write(command + "\n")
            self.proc.stdin.flush()
        except (BrokenPipeError, OSError) as e:
            raise RuntimeError(f"Failed to send command: {e}")

        try:
            response = self.proc.stdout.readline()
        except (ValueError, OSError) as e:
            raise RuntimeError(f"Failed to read response: {e}")

        if not response:
            stderr_tail = self._read_stderr()
            detail = f" (stderr: {stderr_tail})" if stderr_tail else ""
            raise RuntimeError(f"Binary '{self.name}' closed stdout — likely crashed{detail}")

        return response.strip()

    def close(self):
        try:
            if self.is_alive():
                self.proc.stdin.write("EXIT\n")
                self.proc.stdin.flush()
        except (BrokenPipeError, OSError):
            pass
        finally:
            try:
                self.proc.terminate()
            except ProcessLookupError:
                pass