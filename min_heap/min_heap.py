class MinHeaper:
    def __init__(self, dictionary, array, original_dictionary):
        self.dictionary = dictionary
        self.array = array
        self.size = len(array)
        self.original_dictionary = original_dictionary
        self.node_list = {}

    def min_heap(self):
        for position in range(self.size // 2, -1, -1):
            self.min_heapify(self.size, position)

    def min_heapify(self, heap_size, position):
        left_element_position = 2 * position + 1
        right_element_position = 2 * position + 2

        if (left_element_position <= self.size - 1 and
                self.dictionary[self.array[left_element_position]] < self.dictionary[self.array[position]]):
            smallest = left_element_position
        else:
            smallest = position

        if (right_element_position <= self.size - 1 and
                self.dictionary[self.array[right_element_position]] < self.dictionary[self.array[smallest]]):
            smallest = right_element_position

        if (smallest != position):
            self.swap_elements(position, smallest)
            self.min_heapify(heap_size, smallest)

    def swap_elements(self, position1, position2):
        self.array[position1], self.array[position2] = self.array[position2], self.array[position1]
