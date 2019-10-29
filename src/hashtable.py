import os
import sys
import random
os.system( 'clear' )
# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        # buckets
        hashsum = 5001

        for i in range( len( self.storage ) ):
            if self.storage[i] == None:
                return i
            else:
                if i == len( self.storage ) - 1:
                    print( 'STORAGE IS FULL' )
                    self.resize()
                    return i + 1


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        print( 'INSERT - Key:' , key , 'Value:' , value )

        index = self._hash_mod( key )
        print( 'index from insert' , index )
        node = self.storage[ index ]

        # if storage is empty
        if node is None:

            self.storage[ index ] = LinkedPair( key , value )
            return



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        pass


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # os.system( 'clear' )
        for i in self.storage:
            if i is not None:
                print( i.key , i.value )


        print( 'Retrieve:' , key )
        for i in self.storage:
            if i is not None:

                if i.key == key:

                    return i.value


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        print( 'RESIZING!')

        current_len = len( self.storage )

        HashTable( current_len * 2 )

        for i in range( current_len ):
            self.storage.append( None )



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
