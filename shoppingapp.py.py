from datetime import datetime
from tabulate import tabulate
data = [
    {"s.no": 1,"product": "biscuits", "quantity": 5, "price":33},
    {"s.no": 2,"product": "cereals", "quantity": 30, "price": 34},
    {"s.no": 3,"product": "chicken", "quantity": 28, "price":200 },
    {"s.no": 4,"product": "oats", "quantity": 28, "price":37.99 },
     {"s.no": 5,"product": "rice", "quantity": 28, "price":37.99}
]

table=tabulate(data, headers="keys", tablefmt="grid")
print(table)
a=int(input("biscuits:"))
while(a>5):
  print("out of stock max stock:5")
  a=int(input("biscuits :"))
b=int(input("cereals:"))
while(b>30):
  print("out of stock max stock:30")
  b=int(input("cereals :"))
c=int(input("chicken:"))
while(c>28):
  print("out of stock max stock:28")
  c=int(input("chicken:"))
d=int(input("oats:"))
while(d>28):
  print("out of stock max stock:28")  
  d=int(input("oats :"))
e=int(input("rice:"))
while(e>28):
  print("out of stock max stock:28")  
  e=int(input("rice :")) 
print("DELIVERY DETAIL:")
x=input("Name:")
y=input("Address:")
now=datetime.now()
dateset=f"{now.day}/{now.month}/{now.year}"
m=int(input("dist"))
dc=m*2
print(f"the distance {dateset}:",dc)
f=33*a
g=34*b
h=200*c
i=37.99*d
j=37.99*e
v=f+g+h+i+j
data = [
    {"s.no": 1,"product": "biscuits", "quantity": a, "price":f},
    {"s.no": 2,"product": "cereals", "quantity": b, "price": g},
    {"s.no": 3,"product": "chicken", "quantity": c, "price":h},
    {"s.no": 4,"product": "oats", "quantity": d, "price":i },
     {"s.no": 5,"product": "rice", "quantity": e, "price":j }]
table=tabulate(data, headers="keys", tablefmt="grid")
print(table)
print("total item :",v)
print("total bill :",v+dc)
print("name :",x)
print("Address:",y)
ch=input("continue shopping?")
sa=5-a
sb=30-b
sc=28-c
sd=28-d
se=28-e
while(True):
  if(ch=="yes"):
    a1=int(input("biscuits:"))
    while(a1>sa):
      print("out of stock max stock:",sa)
      a1=int(input("biscuits:"))
    b1=int(input("cereals:"))
    while(b1>sb):
      print("out of stock max stock:",sb)
      b1=int(input("cereals:")) 
    c1=int(input("chicken:"))
    while(c1>sc):
      print("out of stock max stock:",sc)
      c1=int(input("chicken:"))
    d1=int(input("oats:"))
    while(d1>sd):
      print("out of stock max stock:",sd)
      d1=int(input("oats:"))  
    e1=int(input("rice:"))
    while(e1>se):
      print("out of stock max stock:",se)
      e1=int(input("rice:"))
    f1=33*a1
    g1=34*b1
    h1=200*c1
    i1=37.99*d1
    j1=37.99*e1
    v1=v+f1+g1+h1+i1+j1
    data = [
          {"s.no": 1,"product": "biscuits", "quantity": a1+a, "price":f1+f},
          {"s.no": 2,"product": "cereals", "quantity": b1+b, "price": g1+g},
          {"s.no": 3,"product": "chicken", "quantity": c1+c, "price":h1+h},
          {"s.no": 4,"product": "oats", "quantity": d1+d, "price":i1+i },
          {"s.no": 5,"product": "rice", "quantity": e1+e, "price":j1+j }]
    table=tabulate(data, headers="keys", tablefmt="grid")
    print(table)
    print("total item :",v1)
    print("total bill :",v1+dc)
    print("name :",x)
    print("Address:",y)
    sa=5-a1
    sb=30-b1
    sc=28-c1
    sd=28-d1
    se=28-e1
    a += a1
    b += b1
    c += c1
    d += d1
    e += e1
    f += f1
    g += g1
    h += h1
    i += i1
    j += j1
    v += v1
    ch=input("continue shopping?") 
      
  else:
    print("have a nice day")
    break


