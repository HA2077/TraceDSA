import subprocess
import platform
import os

def get_binary(name):
    system = platform.system().lower()
    ext = ".exe" if system == "windows" else ""
    folder = "macos" if system == "darwin" else system
    base = os.path.dirname(__file__)
    return os.path.join(base, "bins", folder, f"{name}{ext}")

class DSBridge:
    def __init__(self, name):
        self.proc = subprocess.Popen(
            [get_binary(name)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True
        )
        ready_line = self.proc.stdout.readline().strip()
        if ready_line != "READY":
            raise RuntimeError(f"Expected READY from binary, got: {ready_line}")

    def send(self, command):
        self.proc.stdin.write(command + "\n")
        self.proc.stdin.flush()
        return self.proc.stdout.readline().strip()

    def close(self):
        try:
            self.proc.stdin.write("EXIT\n")
            self.proc.stdin.flush()
        except BrokenPipeError:
            # Process may have already terminated
            pass
        self.proc.terminate()