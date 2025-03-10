def get_char_from_unicode(unicode_input):


    if unicode_input.startswith(('U+', 'u+')):
        unicode_input = unicode_input[2:]
    unicode_input = unicode_input.strip()


    try:

        code_point = int(unicode_input, 16)
    except ValueError:
        try:

            code_point = int(unicode_input)
        except ValueError:
            print("Invalid input. Please enter a valid Unicode code point.")
            return None


    try:
        char = chr(code_point)
        return char
    except ValueError:
        print("The code point is out of valid Unicode range.")
        return None



unicode_input = input("Enter a Unicode code point (e.g., U+0041, 0041, or 65): ")
character = get_char_from_unicode(unicode_input)

if character is not None:
    print("The character for the given Unicode code point is:", character)
