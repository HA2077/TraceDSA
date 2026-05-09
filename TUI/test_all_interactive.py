#!/usr/bin/env python3
import subprocess
import sys
import os

def test_binary(binary_path, test_name, test_commands):
    print(f"\n{'='*60}")
    print(f"Testing: {test_name}")
    print(f"Binary: {binary_path}")
    print('='*60)
    
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
    if line != "READY":
        print(f"❌ FAILED: Expected READY, got: {line}")
        proc.terminate()
        return False
    
    success = True
    
    # Execute test commands
    for cmd, expected_start in test_commands:
        print(f"\n--> {cmd}")
        proc.stdin.write(cmd + "\n")
        proc.stdin.flush()
        line = proc.stdout.readline().strip()
        print(f"<-- {line}")
        
        if not line.startswith(expected_start):
            print(f"❌ FAILED: Expected response starting with '{expected_start}', got: {line}")
            success = False
            # Don't break, continue testing other commands
    
    # Test EXIT
    print(f"\n--> EXIT")
    proc.stdin.write("EXIT\n")
    proc.stdin.flush()
    line = proc.stdout.readline().strip()
    print(f"<-- {line}")
    if line != "BYE":
        print(f"❌ FAILED: Expected BYE, got: {line}")
        success = False
    
    proc.wait()
    
    if success:
        print(f"✅ {test_name} PASSED")
    else:
        print(f"❌ {test_name} FAILED")
    
    return success

def main():
    # Change to the project directory
    os.chdir("/home/ha07/Desktop/Projects/TraceDSA")
    
    # Define test binaries and their commands
    tests = [
        # Stack (array-backed)
        (
            "./TUI/bins/linux/stack",
            "Stack (Array)",
            [
                ("PUSH 10", "OK"),
                ("PUSH 20", "OK"),
                ("PUSH 30", "OK"),
                ("PEEK", "OK Peek: 30"),
                ("PRINT", "OK"),
                ("POP", "OK"),
                ("POP", "OK"),
                ("POP", "OK"),
                ("POP", "ERROR"),  # Should error on empty
            ]
        ),
        # Queue (array-backed)
        (
            "./TUI/bins/linux/queue",
            "Queue (Array)",
            [
                ("ENQUEUE 5", "OK"),
                ("ENQUEUE 15", "OK"),
                ("ENQUEUE 25", "OK"),
                ("PEEK", "OK Peek:"),  # Will check for "Peek:" in response
                ("PRINT", "OK"),
                ("DEQUEUE", "OK"),
                ("DEQUEUE", "OK"),
                ("DEQUEUE", "OK"),
                ("DEQUEUE", "ERROR"),  # Should error on empty
            ]
        ),
        # BST
        (
            "./TUI/bins/linux/bst",
            "BST",
            [
                ("INSERT 50", "OK"),
                ("INSERT 30", "OK"),
                ("INSERT 70", "OK"),
                ("INSERT 20", "OK"),
                ("INSERT 40", "OK"),
                ("PREORDER", "OK"),
                ("INORDER", "OK"),
                ("POSTORDER", "OK"),
                ("FIND 50", "OK true"),
                ("FIND 25", "OK false"),
                ("REMOVE 20", "OK"),
                ("REMOVE 30", "OK"),
                ("ISEMPTY", "OK false"),
                ("CLEAR", "OK"),
                ("ISEMPTY", "OK true"),
            ]
        ),
        # Heap
        (
            "./TUI/bins/linux/heap",
            "Heap (Min/Max)",
            [
                ("ENQUEUE_MIN 50", "OK"),
                ("ENQUEUE_MIN 30", "OK"),
                ("ENQUEUE_MIN 70", "OK"),
                ("ENQUEUE_MIN 20", "OK"),
                ("ENQUEUE_MIN 40", "OK"),
                ("PRINT_MIN", "OK"),
                ("PEEK_MIN", "OK Peek (min):"),
                ("SIZE", "OK Size:"),
                ("DEQUEUE_MIN", "OK"),
                ("DEQUEUE_MIN", "OK"),
                ("DEQUEUE_MIN", "OK"),
                ("DEQUEUE_MIN", "OK"),
                ("DEQUEUE_MIN", "OK"),  # Should empty the heap
                ("PEEK_MIN", "ERROR"),  # Should error on empty
                ("ENQUEUE_MAX 10", "OK"),
                ("ENQUEUE_MAX 30", "OK"),
                ("ENQUEUE_MAX 20", "OK"),
                ("PRINT_MAX", "OK"),
                ("PEEK_MAX", "OK Peek (max):"),
                ("DEQUEUE_MAX", "OK"),
                ("DEQUEUE_MAX", "OK"),
                ("DEQUEUE_MAX", "OK"),  # Should empty the heap 
                ("PEEK_MAX", "ERROR"),  # Should error on empty
            ]
        ),
    ]
    
    # Run all tests
    results = []
    for binary_path, test_name, commands in tests:
        if os.path.exists(binary_path):
            result = test_binary(binary_path, test_name, commands)
            results.append((test_name, result))
        else:
            print(f"\n⚠️  SKIPPING {test_name}: Binary not found at {binary_path}")
            results.append((test_name, False))
    
    # Summary
    print(f"\n{'='*60}")
    print("TEST SUMMARY")
    print('='*60)
    all_passed = True
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: {test_name}")
        if not passed:
            all_passed = False
    
    print(f"\n{'='*60}")
    if all_passed:
        print("🎉 ALL TESTS PASSED! Ready for TUI development.")
    else:
        print("💥 SOME TESTS FAILED! Please fix issues before proceeding.")
    print('='*60)
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)