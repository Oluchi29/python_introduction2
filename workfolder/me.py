# write a python code that loops through a list and print them out using python function

def fruits():
     listofitems=["cucumber","kola","groundnut","pineapple","carrot"]
     for x in listofitems:
          print(x)

     listofitems.remove("kola") #i removed kola from the list
     print(listofitems)
fruits()