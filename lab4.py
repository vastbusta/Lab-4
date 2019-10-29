# -*- coding: utf-8 -*-
"""
Author:Ruben Bustamante
Instructor: Diego Aguirre
TA:Gerarado Barraza
Course: CS 2302
Assigment: Lab 4B
Date of last modification: 10/29/2019
Purpose of program: uses reb black tree and avl tree and B-tree to find anagrams
"""

from redblacktree import RedBlackTree
from avl import AVL_Tree, Node
from BTrees import BTree
import time

count = -1 # global variable to count the anagrams

def b_tree_file_reader(file):
    
    b_tree = BTree() # stores the red black tree in to variable 

    for line in file:
        
        word = line.strip('\n').lower()
        b_tree.insert(word)
        
    file.close()

    return b_tree

def rb_file_reader(file): # this function loads file in to red and black tree 
    
    rb_tree = RedBlackTree() # stores the red black tree in to variable 

    for line in file:
        
        word = line.strip('\n').lower()
        rb_tree.rbt_insert(word)
        
    file.close()

    return rb_tree


def avl_file_reader(file): # this function loads file in to avl tree
    
    avl_tree = AVL_Tree() # stores avl tree in to a vairable 

    for line in file:
        
        word = line.strip('\n').lower()
        avl_tree.insert(Node(word))
        
    file.close()

    return avl_tree


def count_anagrams(word, word_file, prefix=""): # counts anagrams that are match words in the file
 
    global count 
  
    if len(word) <= 1:
        str = prefix + word

        if word_file.search(str):
            count += 1
    else:
        
        for i in range(len(word)):
            
            curr = word[i: i + 1]
            before = word[0: i]
            after = word[i + 1:]

            if curr not in before:
                count_anagrams(before + after, word_file, prefix + curr)
                
    return count  
    

def max_anagram(file, word_file): # checks the max number of anagrams

    global count
    usr_file = open(file, "r") #re-opens file to scan every element in the file and compare against data structure
    max_count = 0
    anagram_count = 0
    longest_word = ""

    for line in usr_file:
        
        word = line.strip('\n').lower()
        anagram_count= count_anagrams(word, word_file) # each iteration of the file read gives count a new value
        
        if anagram_count > max_count:
            
            max_count = count
            longest_word  = word
            
        count = 0 # global variable updated, in order to provide new count value in count_anagrams method return
        
        
    usr_file.close() 
    
    print("Word with the most anagrams is: ",longest_word , "\nThe number of anagrams it has is: ", max_count, "\n")


def main():

    global count # global count

    user_file = input("\n\nPlease provide the name of the file: ") # ask for user to input a file
    
    file = open(user_file, "r")

    user_tree = input("\nPlease choose:\n1. AVL Tree\n2. Red-Black Tree\n3  B-Tree\n") # user choice of tree

    if int(user_tree) == 1:
        
        english_words = avl_file_reader(file)
        
        user_word = input("\nPlease enter a word? ")
        start_time = time.time()
        print("The word '",user_word,"' has a total of ", count_anagrams(user_word, english_words), " anagrams.")
        print('time:', (time.time()-start_time))
        count = 0 # updates count to zero once done with this avl tree
        
    elif int(user_tree) == 2:
        
        english_words = rb_file_reader(file)
        
        user_word = input("\nPlease enter a word?: ")
        start_time = time.time()
        print("The word '",user_word,"' has a total of ", count_anagrams(user_word, english_words), " anagrams.")
        print('time:', (time.time()-start_time))
        count = 0 # updates count to zero once done with this red black tree
        
    elif int(user_tree) ==3:
        
        english_words = b_tree_file_reader(file)                                
        user_word = input("\nPlease enter a word? ")
        
        start_time = time.time()
        
        print("The word '",user_word,"' has a total of ", count_anagrams(user_word, english_words), " anagrams.")
        
        print('time:', (time.time()-start_time))
        count=0
    else:
        print("Invalid Selection. Good Bye.")
    
    user_check = input("\nWould you like to check which word has the most anagrams in the file? (Enter Y or N): ")

    if user_check == "Y" or user_check == "y":
        
        max_anagram(user_file, english_words)
        
    else:
        
        print("Goodbye! \n")


main()