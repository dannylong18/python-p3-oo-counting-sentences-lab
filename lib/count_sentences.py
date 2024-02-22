#!/usr/bin/env python3
import re

class MyString:
    
    def __init__(self, value = ''):
        self._value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if isinstance (value, str):
            return self._value == value
        else:
            print('The value must be a string.')

    def is_sentence(self):
        string = self._value
        if string.endswith('.'):
            return True
        else:
            return False

    def is_question(self):
        string = self._value
        if string.endswith('?'):
            return True
        else:
            return False
        
    def is_exclamation(self):
        string = self._value
        if string.endswith('!'):
            return True
        else:
            return False
        
    def count_sentences(self):
        endings = ['.', '?', '!']
        sentences = re.split('[{}]+'.format(''.join(endings)), self.value)
        sentences = [s.strip() for s in sentences if s.strip()]
        return (len(sentences))

simple_string = MyString("one. two. three?")
empty_string = MyString()
complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")

complex_string.count_sentences()