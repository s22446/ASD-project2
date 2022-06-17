# IMPORTS
from bitstring import BitArray


def opener(path):
    file = open(path, "r")

    return file


def write_codes_to_text_file(path, codes):
    file = open(path, "w+")
    for code in codes:
        file.write(code + ": " + codes[code] + "\n")
    file.close()


def write_encoded_message_to_text_file(path, codes, encoded_message):
    file = open(path, "w+")
    for code in codes:
        file.write(code + ": " + codes[code] + "\n")
    file.write("\n")
    file.write(encoded_message)
    file.close()


def write_encoded_message_to_bin_file(path, codes, encoded_message):
    file = open(path, "w+")
    for code in codes:
        file.write(code + ": " + codes[code] + "\n")
    file.write("\n")
    message = BitArray(bin=encoded_message)
    file = open(path, "ab")
    message.tofile(file)
    file.close()

def bin_opener(path):
    file = open(path, "rb")

    return file


def write_decoded_message_to_text_file(path, decoded_message):
    file = open(path, "w+")
    file.write(decoded_message)
    file.close()
