# we start with an empty cache and an empty list of keys 
# 1-
# each get function find the key in the cache and returns its value
# that value becomes the most recently used MRU
# if it's not in our list, we insert it at the head
# if it's in our list, we delete it and insert it at the head
# 2-
# each put function insert a key and a value inside the cache
# that value becomes the most recently used MRU
# if it's not in our list, we insert it at the head
# if it's already it our list, we delete it and insert it at the head
#3-
# if the length of cache exceeds its capacity, we delete the least recently used LRU at the tail of our list

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
      
    def __init__(self, cap):
        self.cap = cap
        self.cache = {}
        
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def remove(self,node):

        curr = node # Storing it in a variable for easy deleting later

        if curr == self.head : 
            self.head = curr.next # Giving the head the value of the node after our current one
            if self.head is not None: # If the list isn't empty now that we deleted the current node
                self.head.prev = None # Set the new head with None as its prev
            del curr
        
        elif curr == self.tail:
            self.tail = curr.prev  # Giving the tail the value of the node before our current one
            if self.tail is not None: # If the list isn't empty now that we deleted the current node
                self.tail.next = None # Set the new tail with None as its next
            del curr

        else:
            if curr.prev is not None: # Safety check not to call next on None
                curr.prev.next = curr.next
            if curr.next is not None: # Safety check not to call prev on None
                curr.next.prev = curr.prev
            del curr

        return node
        
        
    def insert(self,node): # null--2--3--null / Null--1--2

        node.next = self.head # Linking our node's next to the head
        node.prev = None # Linking our node's prev to None
        if self.head is not None: # if the list is not empty
            self.head.prev = node # Linking the head's prev to our node
        self.head = node # Updating the self.head variable
        return node 
        
    def get(self, key):
        # if key not found, return -1
        if key not in self.cache:
            return -1
        
        # Now you just used your key, so it is most recently used
        # Your goal is then to move it at the beginning of your  list
        node=self.cache[key]
        self.remove(node)
        self.insert(node)


    def put(self, key, value):
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            # Same logic, you just used your key, so it is most recently used
            # Move it at the end of your order list
            self.remove(node)
            self.insert(node)
            
        else:
            # if cache reaches full capacity
            if len(self.cache) >= self.cap:
                # pop the first item of the list
                discard = self.head
                self.remove(discard)
                # delete it from the cache
                del self.cache[discard.key]

            new_node=Node(key,value)
            self.insert(new_node)
            self.cache[key]=new_node

while True:
    cap = int(input("Enter your cache capacity(positive and <10**3): "))
    if cap<0 or cap>10**3:
        gh