# LAB8

from abc import ABC, abstractmethod


class FrequencyCounter(ABC):
    address = None

    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFreqs(self):
        pass


class ListCount(FrequencyCounter):
    def calculateFreqs(self):
        letter_freqs = []
        with open(self.address, 'r') as file:
            text = file.read().lower()
            for letter in sorted(set(text)):
                freq = text.count(letter)
                letter_freqs.append((letter, freq))
        return letter_freqs


class DictCount(FrequencyCounter):
    def calculateFreqs(self):
        letter_freqs = {}
        with open(self.address, 'r') as file:
            text = file.read().lower()
            for letter in text:
                if letter.isalpha():
                    if letter in letter_freqs:
                        letter_freqs[letter] += 1
                    else:
                        letter_freqs[letter] = 1
        return letter_freqs


if __name__ == '__main__':
    file_address = 'weirdWords.txt'

    list_counter = ListCount(file_address)
    letter_freqs_list = list_counter.calculateFreqs()
    print('List:')
    for letter, freq in letter_freqs_list:
        print(f'{letter} = {freq}')

    print()

    dict_counter = DictCount(file_address)
    letter_freqs_dict = dict_counter.calculateFreqs()
    print('Dictionary:')
    for letter, freq in letter_freqs_dict.items():
        print(letter, '=', freq)
