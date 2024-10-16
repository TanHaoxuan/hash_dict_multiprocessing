# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:37:05 2024

@author: 96160
"""

# SuperFastPython.com
# example of hashing a word list serially
from hashlib import sha512
 
# hash one word using the SHA algorithm
def hash_word(word):
    # create the hash object
    hash_object = sha512()
    
    # convert the string to bytes
    byte_data = word.encode('utf-8')
    
    # hash the word
    hash_object.update(byte_data)
    
    return hash_object.hexdigest()
 
# load a file of words
def load_words(path):
    with open(path, encoding='utf-8') as file:
        # read all data as lines
        return file.readlines()
 
# entry point
def main():
    path = '1m_words.txt'
    words = load_words(path)
    print(f'Loaded {len(words)} words from {path}')
    
    known_words = {hash_word(word) for word in words}
    print(f'Done, with {len(known_words)} hashes')
 
if __name__ == '__main__':
    main()