#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        sentences = [sentence for sentence in self.value.split('.') if sentence.strip()]
        return len(sentences)

string = MyString("This is a sentence.")
print(string.is_sentence())  # Output: True
print(string.is_question())  # Output: False
print(string.is_exclamation())  # Output: False
print(string.count_sentences())  # Output: 1






