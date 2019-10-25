# -*- coding: utf-8 -*-
"""

Author:Ruben Bustamante
Instructor: Diego Aguirre
TA:Gerarado Barraza
Course: CS 2302
Assigment: Lab 3B
Date of last modification: 10/19/2019
Purpose of program: Redblack file for lab3
"""
class RBT_Node:
    def __init__(self, key, parent,color, left, right):
        
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color
        
 
    def are_both_children_black(self): # Returns true if both child nodes are black
        
        if self.left != None and self.left.is_red():
            
            return False
        
        if self.right != None and self.right.is_red():
            
            return False
        
        return True

    def get_grandparent(self): # Returns the grandparent of the current node
        
        if self.parent is None:
            
            return None
        
        return self.parent.parent


    def get_predecessor(self): # Gets this node's predecessor from the left child's subtree
        
        node = self.left
        
        while node.right is not None:
            
            node = node.right
            
        return node


    def get_sibling(self): # Returns this node's sibling or none if no sibiling
        
        if self.parent is not None:
            
            if self is self.parent.left:
                
                return self.parent.right
            
            return self.parent.left
        
        return None

    
    def get_uncle(self): # Returns the uncle of current node
        
        grandparent = self.get_grandparent()
        
        if grandparent is None:
            return None
        
        if grandparent.left is self.parent:
            
            return grandparent.right
        
        return grandparent.left
  
    def is_black(self): # if node's color is black return true
        return self.color == "black"
    

    def is_red(self): # if node's color is red return true
        
        return self.color == "red"

    
    def replace_child(self, current_child, new_child): # Replaces node's children with a new child
        
        if self.left is current_child:
            
            return self.set_child("left", new_child)
        
        elif self.right is current_child:
            
            return self.set_child("right", new_child)
        
        return False

    
    def set_child(self, which_child, child): # Sets the left or right child or current node
        
        if which_child != "left" and which_child != "right":
            return False

        if which_child == "left":
            self.left = child
        else:
            self.right = child

        if child != None:
            child.parent = self

        return True


class RedBlackTree:
    
    def __init__(self):
        self.root = None


    def rbt_insert(self, key):
        
        new_node = RBT_Node(key, None, None, None, None)
        
        self.insert_node(new_node)

    def insert_node(self, node):
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            
            while current_node is not None:
                
                if node.key < current_node.key:
                    
                    if current_node.left is None:
                        current_node.set_child("left", node)
                        
                        break
                    
                    else:
                        current_node = current_node.left
                else:
                    
                    if current_node.right is None:
                        current_node.set_child("right", node)
                        
                        break
                    
                    else:
                        current_node = current_node.right

       
        node.color = "red" # Color the node red

       
        self.rbt_balance(node)  # Balance the tree

    def rbt_balance(self, node):
        
       
        if node.parent is None:  # If node is the root returns the node black
            node.color = "black"
            return

        
        if node.parent.is_black(): # If parent is black, then return
            return

        parent = node.parent
        grandparent = node.get_grandparent()
        uncle = node.get_uncle()

        
        if uncle is not None and uncle.is_red():
            parent.color = uncle.color = "black"
            grandparent.color = "red"
            self.rbt_balance(grandparent)
            return

        if node is parent.right and parent is grandparent.left:
            self.rotate_left(parent)
            node = parent
            parent = node.parent

        elif node is parent.left and parent is grandparent.right:
            self.rotate_right(parent)
            node = parent
            parent = node.parent

        # Color parent black and grandparent red
        parent.color = "black"
        
        grandparent.color = "red"

        # If node is parent's left child, then rotate right at grandparent, otherwise rotate left
     
        if node is parent.left:
            self.rotate_right(grandparent)
        else:
            self.rotate_left(grandparent)

    def rotate_left(self, node):
        
        right_left_child = node.right.left
        
        if node.parent != None:
            node.parent.replace_child(node, node.right)
            
       
        else:  # node is root 
            
            self.root = node.right
            self.root.parent = None
            
        node.right.set_child("left", node)
        node.set_child("right", right_left_child)

    def rotate_right(self, node):
        
        left_right_child = node.left.right
        
        if node.parent != None:
            node.parent.replace_child(node, node.left)
            
        else:  # node is root
            
            self.root = node.left
            self.root.parent = None
            
        node.left.set_child("right", node)
        node.set_child("left", left_right_child)

    def search(self, key):
        
        current_node = self.root
        
        while current_node is not None:
            
           
            if current_node.key == key: # if the current node and key match return True
                return True

            
            elif key < current_node.key: #if the key is less than current node search left
                
                current_node = current_node.left

           # if the key is greater than current node search right
            else:
                current_node = current_node.right

        # The key was not found in the tree.
        return False