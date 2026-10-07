fruit=("Apple","apple","orange")
print(fruit)

temp=list(fruit)
temp.append("Mango")
fruit=tuple(temp)
print(fruit)
fruit.append("kiwi")
print(fruit)