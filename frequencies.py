"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    visitedItems = []

    for x in items:
        if(not (str(x) in visitedItems)):
            frequency = 0;
            frequencies[str(x)] = frequency;
            visitedItems.append(str(x))
            for y in items:
                if(str(y) == str(x)):
                    frequency = frequency + 1;
                    frequencies[str(x)] = frequency;
    
    return frequencies
