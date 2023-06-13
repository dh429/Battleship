#!python3
import random as r

'''
There are 5 boats in battleship. They must occupy coordinates that are horizontal or vertical only (no diagonals). 
The size of the boats are 2, 3, 3, 4 and 5. Create a function that generates a list of the data for your boats.
'''

map = { 9 :{0 :"*",1 : "*",2 : "*",3 : "*",4 : "*",5 : "*",6 : "*",7 : "*",8 : "*",9 : "*"},
        8 :{0 :"*",1 : "*",2 : "*",3 : "*",4 : "*",5 : "*",6 : "*",7 : "*",8 : "*",9 : "*"},
        7 :{0 :"*",1 : "*",2 : "*",3 : "*",4 : "*",5 : "*",6 : "*",7 : "*",8 : "*",9 : "*"},
        6 :{0 :"*",1 : "*",2 : "*",3 : "*",4 : "*",5 : "*",6 : "*",7 : "*",8 : "*",9 : "*"},
        5 :{0 :"*",1 : "*",2 : "*",3 : "*",4 : "*",5 : "*",6 : "*",7 : "*",8 : "*",9 : "*"},
        4 :{0 :"*",1 : "*",2 : "*",3 : "*",4 : "*",5 : "*",6 : "*",7 : "*",8 : "*",9 : "*"},
        3 :{0 :"*",1 : "*",2 : "*",3 : "*",4 : "*",5 : "*",6 : "*",7 : "*",8 : "*",9 : "*"},
        2 :{0 :"*",1 : "*",2 : "*",3 : "*",4 : "*",5 : "*",6 : "*",7 : "*",8 : "*",9 : "*"},
        1 :{0 :"*",1 : "*",2 : "*",3 : "*",4 : "*",5 : "*",6 : "*",7 : "*",8 : "*",9 : "*"},
        0 :{0 :"*",1 : "*",2 : "*",3 : "*",4 : "*",5 : "*",6 : "*",7 : "*",8 : "*",9 : "*"}
}

def addboats(size):
  occupied = []

  direction = r.randint(1,2)
  #1 means points up, 2 means sideways

  direction = 1
  def run():
    direction = 1
    if direction == 1:
      try:
        y = r.randint(0,9)
        x = r.randint(0,9)

        map[y][x] = "*"
        for i in range(size):
          map[y+i][x] = "X"
      except:
        print("failed")
        for i in range(size):
          if y+1 >= 10:
            map[y][x] = "*"
          else:
            map[y+1][x] = "*"
        run()
  run()

      
    



def printmap():
    maplen = len(map) - 1
    for i in range(len(map)):
        for a in range(len(map[i])):
            print(map[maplen][a], end = " ")
            
        maplen -= 1
        print()


addboats(3)
printmap()