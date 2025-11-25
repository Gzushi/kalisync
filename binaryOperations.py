def to_bin(n):
    return bin(n)[2:] if n >= 0 else "-" + bin(-n)[2:]

def to_hex(n):
    return hex(n)[2:].upper()

def pad_bits(b, n):
    return b.zfill(n)

def count_ones(b):
    return b.count("1")

def count_zeros(b):
    return b.count("0")

def twos_complement(b):
    width = len(b)
    n = int(b, 2)
    tc = ((~n) + 1) & ((1 << width) - 1)
    return bin(tc)[2:].zfill(width)

def signed_from_binary(b):
    width = len(b)
    n = int(b, 2)
    if b[0] == "1":  # negative
        n -= 1 << width
    return n

def signed_to_binary(d, width):
    if d < 0:
        d = (1 << width) + d
    return bin(d & ((1 << width) - 1))[2:].zfill(width)

def rotate_left(b, n):
    n = n % len(b)
    return b[n:] + b[:n]

def rotate_right(b, n):
    n = n % len(b)
    return b[-n:] + b[:-n]


print("Choose operation:")
print("1.  Add (+)")
print("2.  Subtract (-)")
print("3.  Multiply (*)")
print("4.  Divide (/)")
print("5.  Shift Left (<<)")
print("6.  Shift Right (>>)")
print("7.  Bitwise AND (&)")
print("8.  Bitwise OR (|)")
print("9.  Bitwise XOR (^)")
print("10. Binary → Hex")
print("11. Hex → Binary")
print("12. NOT (~)")
print("13. Binary → Decimal")
print("14. Decimal → Binary")
print("15. Pad Binary to N bits")
print("16. Count 1s and 0s")
print("17. Compare two binaries (<, >, =)")
print("18. Bitwise NAND (~&)")
print("19. Bitwise NOR (~|)")
print("20. Bitwise XNOR (~^)")
print("21. Rotate Left (ROL)")
print("22. Rotate Right (ROR)")
print("23. Two's Complement")
print("24. Binary (signed) → Decimal")
print("25. Decimal (signed) → Binary with N bits")

choice = input("Enter choice (1-25): ")


# ---------------------- Single / special operations ----------------------

if choice == "10":
    a = int(input("Enter binary: "), 2)
    print("Hex:", to_hex(a))
    exit()

if choice == "11":
    h = input("Enter hex: ")
    print("Binary:", to_bin(int(h, 16)))
    exit()

if choice == "12":
    a = input("Enter binary: ")
    flipped = "".join("1" if bit == "0" else "0" for bit in a)
    print("NOT (~):", flipped)
    exit()

if choice == "13":
    a = input("Enter binary: ")
    print("Decimal:", int(a, 2))
    exit()

if choice == "14":
    d = int(input("Enter decimal: "))
    print("Binary:", to_bin(d))
    exit()

if choice == "15":
    b = input("Enter binary: ")
    n = int(input("Pad to how many bits? "))
    print("Padded:", pad_bits(b, n))
    exit()

if choice == "16":
    b = input("Enter binary: ")
    print("1s:", count_ones(b))
    print("0s:", count_zeros(b))
    exit()

if choice == "17":
    a = int(input("Enter first binary: "), 2)
    b = int(input("Enter second binary: "), 2)
    if a > b:
        print("Result: First > Second")
    elif a < b:
        print("Result: First < Second")
    else:
        print("Result: First = Second")
    exit()

if choice == "21":
    b = input("Enter binary: ")
    n = int(input("Rotate left by how many bits? "))
    print("ROL:", rotate_left(b, n))
    exit()

if choice == "22":
    b = input("Enter binary: ")
    n = int(input("Rotate right by how many bits? "))
    print("ROR:", rotate_right(b, n))
    exit()

if choice == "23":
    b = input("Enter binary (fixed width): ")
    print("Two's Complement:", twos_complement(b))
    exit()

if choice == "24":
    b = input("Enter binary (two's complement): ")
    print("Signed decimal:", signed_from_binary(b))
    exit()

if choice == "25":
    d = int(input("Enter signed decimal: "))
    width = int(input("Bit width: "))
    print("Binary (two's complement):", signed_to_binary(d, width))
    exit()


# ---------------------- Normal binary ops (with result) ----------------------

a = int(input("Enter first binary number: "), 2)

if choice in ["1", "2", "3", "4", "7", "8", "9", "18", "19", "20"]:
    b = int(input("Enter second binary number: "), 2)

if choice in ["5", "6"]:
    n = int(input("Shift by how many bits? "))

if choice == "1":
    result = a + b
elif choice == "2":
    result = a - b
elif choice == "3":
    result = a * b
elif choice == "4":
    result = a // b
elif choice == "5":
    result = a << n
elif choice == "6":
    result = a >> n
elif choice == "7":
    result = a & b
elif choice == "8":
    result = a | b
elif choice == "9":
    result = a ^ b
elif choice in ["18", "19", "20"]:
    width = max(a.bit_length(), b.bit_length())
    mask = (1 << width) - 1
    if choice == "18":       # NAND
        result = ~(a & b) & mask
    elif choice == "19":     # NOR
        result = ~(a | b) & mask
    elif choice == "20":     # XNOR
        result = ~(a ^ b) & mask
else:
    print("Invalid choice")
    exit()

print("Binary:", to_bin(result))
print("Hex   :", to_hex(result))

