def is_private_use(char):
    """Check if the given character is in one of the Unicode Private Use Areas."""
    code_point = ord(char)
    # Unicode Private Use Area ranges:
    # 1. Basic Multilingual Plane (BMP) PUA: U+E000 to U+F8FF
    # 2. Supplementary Private Use Area-A: U+F0000 to U+FFFFD
    # 3. Supplementary Private Use Area-B: U+100000 to U+10FFFD
    return ((0xE000 <= code_point <= 0xF8FF) or
            (0xF0000 <= code_point <= 0xFFFFD) or
            (0x100000 <= code_point <= 0x10FFFD))



char = input("Enter a single character: ")

if len(char) != 1:
    print("Please enter exactly one character.")
else:

    code_point = ord(char)
    print("The Unicode code point for", char, "is U+{:04X}".format(code_point))


    utf8_bytes = char.encode('utf-8')
    print("UTF-8 encoding:", utf8_bytes)


    if is_private_use(char):
        print("The character is in a Unicode Private Use Area.")
    else:
        print("The character is not in a Unicode Private Use Area.")
