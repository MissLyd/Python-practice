# This program aims to create a Huffman tree algorithm and encode text messages

import heapq 

# Step 1: creating nodes that contain a character, its frequency in the text, and left and right children if found
class Node:
    def __init__(self,char,freq,left=None,right=None):
        self.char = char 
        self.freq = freq
        self.left = left
        self.right = right
    
    # This is in order to compare between nodes and sort them from min to max
    def __lt__(self, other):
        return self.freq < other.freq
    
# Step 2: build the huffman tree
def build_tree(text):
    freq = {ch: text.count(ch) for ch in set(text)} # We're creating a dictionary with each character and its frequency in the text
    heap = [Node(c,f) for c,f in freq.items()] # Creating an unsorted list of all the nodes
    heapq.heapify(heap) # Turning it into a priority queue

    while len(heap) > 1:
        left = heapq.heappop(heap) # Pops and returns the smallest value
        right = heapq.heappop(heap) # Pops and returns the second smallest value
        newfreq = left.freq + right.freq # Frequency of the two nodes combined 
        heapq.heappush(heap, Node(None,newfreq,left,right)) # Adding the new node of the two combined into the priority queue
        # Looping until there's one node left inside the queue, which is the root
    root = heap[0]
    return root

# Step 3: creating unique codes for each character using Huffman's encoding algorithm
def generate_codes(root,prefix="",codes={}):
    if root is None:
        return # If there's no node, stop
    if root.char is None: # If it's not a leaf, keep adding to the code
        generate_codes(root.left,prefix + "0", codes) # If the node is a left child, we add a 0 to the prefix
        generate_codes(root.right,prefix + "1", codes) # If the node is a right child, we add a 1 to the prefix
    else: # When we finally reacj a leaf
        codes[root.char] = prefix # We assign the character the sequence of 0 and 1 that we've built so far
        

    return codes
        
# Step 4: main program
text= input("Enter your text: ")
root = build_tree(text)
codes = generate_codes(root)

encoded_text = "".join(codes[c] for c in text) #joining all the codes for every character in the text

print("Character codes: ",codes)
print("Encoded message: ",encoded_text)
