import sys
from vending_machine import VendingMachineParser

def main():
    if len(sys.argv) != 2:
        print("Usage: python CodingTest.py <input_file>")
        return

    input_file = sys.argv[1]

    parser = VendingMachineParser()
    with open(input_file, 'rb') as f:
        while True:
            byte = f.read(1)
            if not byte:
                break
            parser.read_byte(byte[0])

if __name__ == "__main__":
    main()
