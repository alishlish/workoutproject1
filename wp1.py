import sys

def reverse_cipher(words):
    return words[::-1]

def main():
    if len(sys.argv)!= 3:
        print("Incorrect input format")
        return

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            input_text = input_file.read()

        if not input_text:
            print("Error: The input file is empty.")
            return

        encrypted_text = reverse_cipher(input_text)

        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(encrypted_text)

        print("Encryption completed. Check", output_filename)

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()



