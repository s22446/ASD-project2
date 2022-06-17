# IMPORTS
import file_handler.file_handler as file_handler
import config

import time


def decode(mode):
    if (mode == "main"):
        input_path = config.DECODE_MAIN_INPUT_BIN_FILE_PATH
        output_path = config.DECODE_MAIN_OUTPUT_TXT_FILE_PATH
    else:
        input_path = config.DECODE_INPUT_BIN_FILE_PATH
        output_path = config.DECODE_OUTPUT_TXT_FILE_PATH

    dictionary = {}
    file = file_handler.bin_opener(input_path)
    while (file_content := file.readline().decode()):
        if (file_content == "\r\n"):
            break

        split_content = file_content.split(":")

        letter = split_content[0]
        value = split_content[1].replace(" ", "").replace("\r", "").replace("\n", "")

        dictionary[value] = letter

    #print("DEBUG - Read dictionary: ", dictionary)
    encoded_message = file.read()
    encoded_bits = ""
    for letter in encoded_message:
        encoded_bits += '{0:08b}'.format(letter)

    #print("DEBUG - Read bits: ", encoded_bits)
    decoded_message = ""
    position = 0
    for i in range(0, len(encoded_bits)):
        bit_sequence = encoded_bits[position:i + 1]
        if (bit_sequence in dictionary):
            decoded_message += dictionary[bit_sequence]
            position = i + 1

    #print("DEBUG - Decoded message: ", decoded_message, "\n")

    print("Writing decoded message to file")
    start_time = time.time()
    file_handler.write_decoded_message_to_text_file(output_path, decoded_message)
    end_time = time.time()
    print("Encoded message successfully written in files; time: ", end_time - start_time)


if __name__ == '__main__':
    print("Starting decoding\n")

    start_time = time.time()
    decode("decoder")
    end_time = time.time()

    print("\nText decoded successfully; time: ", end_time - start_time)
