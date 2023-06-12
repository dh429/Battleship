#!python3

'''
There are 5 boats in battleship. They must occupy coordinates that are horizontal or vertical only (no diagonals). 
The size of the boats are 2, 3, 3, 4 and 5. Create a function that generates a list of the data for your boats.
'''

def create():
  '''
  You will need to specify what information you need as inputs, but the output should be a list
  Add whatever code you need for each of your different ships to specify what coordinates it
  occupies and/or whether it is vertical/horizontal
  '''
  output = [
    { "name" : "Tugboat", "size" : 2 },
    { "name" : "Sumbarine", "size" : 3 },
    { "name" : "Destroyer", "size" : 3 },
    { "name" : "Carrier", "size" : 4 },
    { "name" : "Battelship", "size" : 5 }
    ]
  return output
