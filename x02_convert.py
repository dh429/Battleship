#!python3
"""
Given a string literal convert it to a list that contains the coordinate. Your string literal should be able to remove whitespace and work with both lower and upper case values. "B3", "b3" , "B 3" and "b 3" should all correspond to the list item [1,2]
"""



def convert(coordinate):


  newcoord = coordinate.replace(" ", "")
  
  x = ord(newcoord[0])


  if x >= 97:
    x -= 97
  else:
    x -= 65
  
  newcoord = coordinate.replace(newcoord[0],"")

  y = int(newcoord)

  y -= 1

  coordlist = []
  coordlist.append(x)
  coordlist.append(y)

  return coordlist



convert("d5")
convert("D5")

if __name__ == "__main__":
  assert convert("B3") == [1,2]
  assert convert("A10") == [0,9]
  assert convert("d 4") == [3,3]
  
