"""Generate Markov text from text files."""
import sys
from random import choice

file_path = "green-eggs.txt"

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    # file = open(file_path).read()
    file = open(file_path)
    text = file.read()
    file.close()
    
    return text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    
    words = open_and_read_file(file_path).split()
    
    words.append(None)

    for i in range(len(words)- 2): #iterates through the length of all the words in the file and
                                   #stopping at the second-to-last index
        
        key = (words[i],words[i + 1]) #makes the key a tuple equal to the current word, and the next word 

        # value = []
        # chains[key]=value
        
        # if key in chains:
        #     chains[key].append(words[i+2])
            
            # chains[key] = 

        value = words[i + 2] #makes the value equal to the word after the next (3rd word)

        if key not in chains: #checks if the key (whic is the combination of the current word and the next word) has not been added to the chains dictionary
            chains[key] = []  #if the key hasn't been added to the chains dictionary, make the value and empty list
                              #

        chains[key].append(value)  #chucks the value into the list of empty (what was done above) or and existing list of values



    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    key = choice(list(chains.keys())) #makesa singluar key from keys of chains converted from a tuple into a list, and a random key picked out of the list
    words = [key[0], key[1]] #takes the two words from the randomized list and sets them to a new veriable, words
    word = choice(chains[key]) #

    while word is not None:
        key = (key[1], word)
        words.append(word)
        word = choice(chains[key])

  
    return ' '.join(words)

# make_text(make_chains(open_and_read_file(file_path)))

input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
