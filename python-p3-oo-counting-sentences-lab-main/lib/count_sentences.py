#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self.value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        if (type(value) == str):
            self._value = value
        else:
            print("The value must be a string.")

    value = property(get_value, set_value)

    def is_sentence(self):
        return True if self._value[-1] == "." else False

    def is_question(self):
        return True if self._value[-1] == "?" else False

    def is_exclamation(self):
        return True if self._value[-1] == "!" else False

    def count_sentences(self):
        count = 0
        for word in self._value.split():
            if (word[-1] == "." or word[-1] == "!" or word[-1] == "?"):
                count += 1
        return count
