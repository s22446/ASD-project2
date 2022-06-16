# IMPORTS
import node.node as noder
import binascii


# CREATING FREQUENCY DICTIONARY
def count_frequency(text):
    dictionary = {}
    for letter in text:
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1

    return dictionary


# CREATING HUFFMAN CODES
def create_codes_heap(heaper):
    node_list = {}

    for i in range(1, heaper.size):
        x = extract_min(heaper)
        y = extract_min(heaper)

        node = noder.Node(x + y, x, y)
        node_list[x + y] = node

        heaper.dictionary[x + y] = heaper.dictionary[x] + heaper.dictionary[y]
        heaper.array.append(x + y)

        heaper.min_heap()

    heaper.node_list = node_list
    codes = create_codes(heaper)

    return codes


def extract_min(heaper):
    size = len(heaper.array)
    heaper.array[0], heaper.array[size - 1] = heaper.array[size - 1], heaper.array[0]

    deleted_element = heaper.array[size - 1]
    heaper.array.pop(size - 1)
    heaper.size = len(heaper.array)
    heaper.min_heap()

    return deleted_element


def create_codes(heaper):
    codes_dictionary = {}
    for character in heaper.original_dictionary:
        character_code = ""
        current_character = (character + '.')[:-1]
        for node in heaper.node_list:
            if (heaper.node_list[node].left_child == current_character):
                current_character = node
                character_code += "0"
            elif (heaper.node_list[node].right_child == current_character):
                current_character = node
                character_code += "1"

        codes_dictionary[character] = character_code[::-1]

    return codes_dictionary


def encode_message(codes, message):
    encoded_message = ""
    for letter in message:
        encoded_message += codes[letter]

    return encoded_message
