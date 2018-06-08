import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.decode(str(encoding), errors = errors)
    cooked_string = raw_bytes.encode(encoding, errors = errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("Supplimental Files/ex23_unencoded_languages.txt")

main(languages, input_encoding, error)