#!/usr/bin/env python3
import subprocess
import sys

def test_stack(binary_path):
    print(f"\n{'='*50}")
    print(f"Testing: {binary_path}")
    print('='*50)
    
    # Start the process
    proc = subprocess.Popen(
        [binary_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )
    
    # Read READY
    line = proc.stdout.readline().strip()
    print(f"<-- {line}")
    assert line == "READY", f"Expected READY, got: {line}"
    
    # Test PUSH
    print("\n-- Testing PUSH --")
    commands = ["PUSH 10", "PUSH 20", "PUSH 30"]
    for cmd in commands:
        print(f"--> {cmd}")
        proc.stdin.write(cmd + "\n")
        proc.stdin.flush()
        line = proc.stdout.readline().strip()
        print(f"<-- {line}")
        assert line.startswith("OK"), f"Expected OK, got: {line}"
    
    # Test PEEK
    print("\n-- Testing PEEK --")
    cmd = "PEEK"
    print(f"--> {cmd}")
    proc.stdin.write(cmd + "\n")
    proc.stdin.flush()
    line = proc.stdout.readline().strip()
    print(f"<-- {line}")
    assert line.startswith("OK"), f"Expected OK, got: {line}"
    
    # Test PRINT
    print("\n-- Testing PRINT --")
    cmd = "PRINT"
    print(f"--> {cmd}")
    proc.stdin.write(cmd + "\n")
    proc.stdin.flush()
    line = proc.stdout.readline().strip()
    print(f"<-- {line}")
    assert line.startswith("OK"), f"Expected OK, got: {line}"
    
    # Test POP
    print("\n-- Testing POP --")
    for i in range(3):
        cmd = "POP"
        print(f"--> {cmd}")
        proc.stdin.write(cmd + "\n")
        proc.stdin.flush()
        line = proc.stdout.readline().strip()
        print(f"<-- {line}")
        assert line.startswith("OK"), f"Expected OK, got: {line}"
    
    # Test POP on empty (should ERROR)
    print("\n-- Testing POP on empty stack --")
    cmd = "POP"
    print(f"--> {cmd}")
    proc.stdin.write(cmd + "\n")
    proc.stdin.flush()
    line = proc.stdout.readline().strip()
    print(f"<-- {line}")
    assert line.startswith("ERROR"), f"Expected ERROR, got: {line}"
    
    # Test EXIT
    print("\n-- Testing EXIT --")
    cmd = "EXIT"
    print(f"--> {cmd}")
    proc.stdin.write(cmd + "\n")
    proc.stdin.flush()
    line = proc.stdout.readline().strip()
    print(f"<-- {line}")
    assert line == "BYE", f"Expected BYE, got: {line}"
    
    proc.wait()
    print("\n✅ All tests passed!")

if __name__ == "__main__":
    # Test array-backed stack
    test_stack("TUI/bins/linux/stack")
    
    # Test linked list stack
    test_stack("TUI/bins/linux/stackll")
    
    print(f"\n{'='*50}")
    print("ALL TESTS COMPLETED SUCCESSFULLY")
    print('='*50)