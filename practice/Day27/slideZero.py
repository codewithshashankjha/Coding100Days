num=[1,0,-7,9,0,2,7,0,-7,0]


p=[x for x in num if x>0 or x<=-1]
n=[x for x in num if x==0]

r=p+n

print(r)

