import sys

def reverse_cipher(words):
    return words[::-1]

def main():
    if len(sys.argv)!= 3:
        print("Incorrect input format")
        return

    #input_filename = sys.argv[1]
    #output_filename = sys.argv[2]

