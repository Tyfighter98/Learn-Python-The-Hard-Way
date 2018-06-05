import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    # Checks to see if there is any data on the current line otherwise skip this whole block
    if line:
        print_line(line, encoding, errors)
        # Loops main until the if statement fails
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    # strip gets rid of the "\n" at the end of the line
    next_lang = line.strip()
    # We must encode the string from ex23_languages.txt with the passed in encoding type (UTF-8 in our case)
    # errors is set to whatever is put into the errors argument
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # Now that it is encoded we decode it using UTF-8 once again
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    # print(raw_bytes, "<===>", cooked_string)
    print(raw_bytes)
    unencoded_output.write(str(raw_bytes) + "\n")


languages = open("Supplimental Files/ex23_languages.txt", encoding="utf-8")
unencoded_output = open("Supplimental Files/ex23_unencoded_languages.txt", "w")

main(languages, input_encoding, error)