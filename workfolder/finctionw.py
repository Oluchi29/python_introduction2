
 
#
#
def coloured_balls():
 list=["3 black balls" "4 yellow balls" "5 white blls"]
 for i in list:
    print( "pick a ball")
    i=input()
    if i=="yellow balls":
      print(" i have picked the right ball! ")
    else:
      print("oh no!")
    break    
coloured_balls()