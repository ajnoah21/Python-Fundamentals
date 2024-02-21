import sys

def add_two(a,b):
    return a+b

def test():
    assert add_two(2,2) == 4
    assert add_two(2,3) == 5
    assert add_two(1,1) == 2
    print("All tests passed!", file=sys.stderr)  # Writes a success message to error output

def main():
    print("A really fancy program")

test()   # This is the first line to run
main()  # Then this function runs

