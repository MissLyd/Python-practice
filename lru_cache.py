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
        self.key,self.value = key,value
        self.prev = self.next= None

class LRUCache:
      
    def __init__(self, cap):
        self.cap = cap
        self.cache = {}
        
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def remove(self,node):

        prev,next=node.prev,node.next
        prev.next,next.prev=next,prev
        
        
    def insert(self,node): # null--2--3--null / Null--1--2

        prev,next=self.tail.prev,self.tail
        node.prev,node.next=prev,next
        
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
            # Same logic, you just used your key, so it is most recently used
            # Move it at the end of your order list
            self.remove(self.cache[key].value)
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])
        
        #If cache reaches full capacity
        if len(self.cache) >= self.cap:
            # pop the first item of the list
            LRU = self.head
            self.remove(LRU)
            # delete it from the cache
            del self.cache[LRU.key]

