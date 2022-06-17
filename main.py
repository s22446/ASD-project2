# IMPORTS
import file_handler.file_handler as file_handler
import encrypter.encrypter as encrypter
import min_heap.min_heap as heap
import decoder.decoder as decoder
import config

import time

if __name__ == '__main__':
    file = file_handler.opener(config.ENCODE_INPUT_ENCRYPTION_FILE_PATH)
    file_content = file.read()
    frequency_dictionary = encrypter.count_frequency(file_content)
    original_dictionary = frequency_dictionary.copy()
    letters_array = list(frequency_dictionary.keys())

    print("ALL FILES ARE SAVED IN output DIRECTORY!")
    print("Frequency dictionary: ", frequency_dictionary)

    print("\nCharacters before min heapify: ", letters_array)

    heaper = heap.MinHeaper(frequency_dictionary, letters_array, original_dictionary)
    heaper.min_heap()

    print("Characters after min heapify: ", heaper.array, "\n")

    print("Starting encoding")

    start_time = time.time()
    codes = encrypter.create_codes_heap(heaper)
    encoded_message = encrypter.encode_message(codes, file_content)
    end_time = time.time()

    print("Text encoded successfully; time: ", end_time - start_time)

    print("\nWriting to file")
    start_time = time.time()
    file_handler.write_codes_to_text_file(config.ENCODE_OUTPUT_CODES_FILE_PATH, codes)
    file_handler.write_encoded_message_to_text_file(config.ENCODE_OUTPUT_TXT_FILE_PATH, codes, encoded_message)
    file_handler.write_encoded_message_to_bin_file(config.ENCODE_OUTPUT_BIN_FILE_PATH, codes, encoded_message)
    end_time = time.time()
    print("Encoded message successfully written in files; time: ", end_time - start_time)

    print("\n\nWould you like to decode message to the new file?\nUse y/Y key to confirm, any other to decline")
    user_input = input()
    if (user_input == "y" or user_input == "Y"):
        print("Starting decoding\n")

        start_time = time.time()
        decoder.decode("main")
        end_time = time.time()

        print("\nText decoded successfully; time: ", end_time - start_time)
