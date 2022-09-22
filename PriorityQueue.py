# -*- coding: utf-8 -*-
"""
Array-Based Max-Heap Priority Queue

J. Galloway
22 Sept 2022
Version: Original Code
"""

class PriorityQueue:
    
    def __init__(self):
        self.data = [] # init as empty string
        
    def root_node(self):
        '''
        Returns Root which is always in the zero index

        Returns
        -------
        TYPE Numeric
            DESCRIPTION.Root node value

        '''
        if self.data:
            return self.data[0]
        else:
            return None
    
    def last_node(self):
        '''
        Returns Last Node value which is always at the end of the list

        Returns
        -------
        TYPE Numeric
            DESCRIPTION. Last node value

        '''
        if self.data:
            return self.data[-1]
        else:
            return None
    def check_exists(self,node_index):
        '''
        Check if node exists in current heap

        Parameters
        ----------
        node_index : TYPE Integer
            DESCRIPTION. Index of node to check

        Returns
        -------
        TYPE Boolean
            DESCRIPTION. True if node exists false otherwise

        '''
        return not(node_index > (len(self.data) -1))
        
        
    def left_child_index(self, node_index):
        '''
        Calculates left child index of given node index

        Parameters
        ----------
        node_index : TYPE Integer
            DESCRIPTION.Parent node index of left child

        Returns
        -------
        TYPE Integer
            DESCRIPTION. Left child index in array of parent node

        '''
        idx = int(node_index * 2 + 1)
        if self.check_exists(idx):
            return idx
        else:
            return None
        
        
    def right_child_index(self, node_index):
        '''
        Calculates right child index of given node index

        Parameters
        ----------
        node_index : TYPE Integer
            DESCRIPTION.Parent node index of right child

        Returns
        -------
        TYPE Integer
            DESCRIPTION. right child index in array of parent node

        '''
        idx = int(node_index * 2 + 2)
        if self.check_exists(idx):
            return idx
        else:
            return None
    
    
    def parent_index(self, node_index):
        '''
        Calculates the parent node index of the given node

        Parameters
        ----------
        node_index : TYPE Integer
            DESCRIPTION. Index of the child node

        Returns
        -------
        TYPE Integer
            DESCRIPTION. Parent Node index of the child passed in

        '''
        idx = int((node_index - 1)/2)
        if self.check_exists(idx):
            return idx
        else:
            return None
    
    def has_greater_child(self, node_index):
        '''
        Returns True if node has a child with value greater than the 
        passed-in node

        Parameters
        ----------
        node_index : TYPE Integer
            DESCRIPTION. Index of node to check

        Returns
        -------
        TYPE Boolean
            DESCRIPTION. True if node has a child of greater value, False otherwise

        '''
        if not self.check_exists(node_index):
            return False # node does not exist so has no greater childern
        
        val = self.data[node_index]
        left_child_idx = self.left_child_index(node_index)
        right_child_idx = self.right_child_index(node_index)
        
        left_is_none = (left_child_idx is None)
        right_is_none = (right_child_idx is None)
        
        if left_is_none and right_is_none:
            return False
        elif (not left_is_none) and (self.data[left_child_idx] > val):
            return True
        elif (not right_is_none) and (self.data[right_child_idx] > val):
            return True
        else:
            return False
        
    def calculate_larger_child_index(self, node_index):
        '''
        Returns index of largest child or None if has no childern

        Parameters
        ----------
        node_index : TYPE Integer
            DESCRIPTION. index of node to check

        Returns
        -------
        TYPE Integer
            DESCRIPTION. Index of greatest child node

        '''
        if not(self.check_exists(node_index)):
            return None
        
        left_idx = self.left_child_index(node_index)
        right_idx = self.right_child_index(node_index)
                
        # if no right child, return left child index
        if (right_idx is None):
            return left_idx
        
        # if left exists, compare right and left values and return index of largest
        if not (left_idx is None):
            if self.data[left_idx] > self.data[right_idx]:
                return left_idx
            else:
                return right_idx
        
        # left and right are both empty, no children found so return none
        return None
            
    
    def insert(self, node_value):
        '''
        Insert Value and move to proper place in heap to satisfy the 
        heap condition and completeness

        Parameters
        ----------
        node_value : TYPE Object
            DESCRIPTION. object to be inserted in queue

        Returns 
        -------
        None.

        '''
        # add node in last postion
        self.data.append(node_value)
        
        new_node_index = len(self.data) - 1
        
        # trickle up the new node to it's proper place
        while (new_node_index > 0) and (self.data[new_node_index] > self.data[self.parent_index(new_node_index)]):
            # get parent index
            parent_idx = self.parent_index(new_node_index)
            # swap parent and new node since parent < child
            self.data[parent_idx], self.data[new_node_index] = self.data[new_node_index], self.data[parent_idx]
            # update new node index
            new_node_index = parent_idx
        
    def delete(self):
        '''
        Deletes highest priority node (root node) and re-sorts heap

        Returns
        -------
        None.

        '''
        if self.data:
            if len(self.data) == 1:
                self.data.pop()
            else:
                # make last node the root node and trickle down to correct spot
                self.data[0] = self.data.pop()
                trickle_node_idx = 0 
                
                while self.has_greater_child(trickle_node_idx):
                    larger_child_idx = self.calculate_larger_child_index(trickle_node_idx)
                    
                    # swap trickle node and larger child
                    self.data[trickle_node_idx], self.data[larger_child_idx] = self.data[larger_child_idx], self.data[trickle_node_idx]
                    
                    # update trickle index
                    trickle_node_idx = larger_child_idx
                    
                
            
            
    
    