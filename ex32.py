the_count =[1, 2, 3, 4, 5]
fruits=["apples", "oranges", "pears", "apricots"]
print (the_count)
print (fruits)

for i in the_count:
    print (f"This is count {i}")

for i in fruits:
    print(f"This is the fruit {i}")

elements =[]

def siffror(a):
    for i in range (0,a):
        print (f"Adding {i} to the list.")
        elements.append(i)

for i in elements:
    print(f"Element was: {i}")


numbers=[]
def funktion(i):
    while i < 6:
        print(f"At the top i is {i}")
        numbers.append(i)
        i=i+1
    print (numbers)

funktion(1)
siffror(19)

