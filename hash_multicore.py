# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:48:44 2024

@author: 96160
"""
from math import ceil
from hashlib import sha512
from multiprocessing import Pool
import time

 
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
    
    #load the data 
    path = '1m_words.txt'
    words = load_words(path)
    print(f'Loaded {len(words)} words from {path}')
    
    # seq
    known_words_seq = {hash_word(word) for word in words}
    start_time = time.perf_counter_ns()
    end_time = time.perf_counter_ns()

    print(f'Seq method Done, with {len(known_words_seq)} hashes in {end_time-start_time} nanosec')


    #multi process
    start_time = time.perf_counter_ns()
    with Pool(1) as pool:
        # create a set of word hashes
        known_words_mul = pool.map_async(hash_word, words)
    end_time = time.perf_counter_ns()

    print(f'Mutiprocess method Done, with {len("known_words_mul")} hashes in {end_time-start_time} nanosec')

if __name__ == '__main__':
    main()