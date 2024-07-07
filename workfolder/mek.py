# write a python code to add numbers together print out the sum
#check if total is greater than 50, if yes divide by 20 and add 19
#otherwise add 500

def list():
    list1=[12,154,79,134,3,10]
    total=0
    for i in list1:
        total=total+i
    print(total)

    if total >50: #yes
        newresult=(total/20)+19
        print(newresult)
    else:
        total=total+500
list()
    