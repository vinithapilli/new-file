print("hello world")

'''t = (1,3.3,"john")
for val in "john":
   if val == 'h':
      break
   print(val)
   print("the end")'''

t = (1,3.3,"john")
for val in t:
   if val == 'h':
      break
   print(val)
   print("the end")

   string = "vinitha"
   print(string.upper())#uppercase

   string = "VINITHAPILLI"
   print(string.lower())#lower
   print(string.split())

   s = '''
      this
       is 
       string
       '''
   print(type(s))
   h = s.replace("is",'are')
   print(h)

s2 = '''
    this
    is
    string'''
print(s2.count('is'))

s = "Johnclass"
print(s.startswith('J'))
print(s.endswith('s'))


print('my name is {}'.format('kiran'))

set = {1, 2, 3}
print(type(set))

s2={}
print(type(s2))

set = {1,2,3.3}
set.update(['python'])
print(set)

set = {1,2,3.3,'john'}
set.remove(2)
print(set)
set.update([0,'py'])
print(set)


s1 = {1,2,3,4,5,6}
s2 = {5,6,7,99,100}
print(s1.union(s2))
print(s2.difference(s1))
print(s2.isdisjoint(s1))
print(s2.issubset(s1))

b="hello world"
print(b[2:5])


d = {"name":"vinitha","age":22}#dictionary
print(d)
print(type(d))
print(d["name"])

d.update({"address":"hyd"})
print(d)
d.clear()
print(d)

d={"name":"vinitha","age":22,"address":"hyd"}
for i in d.keys(),d.values():
   print(i)

d={"name":"john","age":"22"}
print(len(d))

d={"class1":{
   "name":"akhila",
   "score":"99"
   },"class2":{
      "name":"pravalika",
      "score":"98"
   },"class3":{
   "name":"pravalika",
   "score":"89"
}
}
print(d["class2"])

def john(b,c):#dic items
   print(b,c)
john(3,5)

def john(b,c):
 return(b,c)
w=john(2, 6)
print(w)

def john(*a):
   print(a)
john(3,4,5,6)

def john(**a):
   print(a)
john(name="lenovo",cost=20000)

def student(name):
   print("this is my first function",name)
student('sujatha')

#oops concept
class john:
   d=67
   def display(self):
    a=12
    b=2
    c=a+b
    print(c)
obj=john()
obj.display()
print(obj.d)

class bike:
   d=33
   def display(self):
      print("bike stops when brake apply")
obj=bike()
obj.display()
print(obj.d)

class Mobile:
   def __init__(self,brand,battery,ram,camera,price):
      self.brand=brand
      self.battery=battery
      self.ram=ram
      self.camera=camera
      self.price=price
   def display(self):
      print("brand:",self.brand)
      print("battery:",self.battery)
      print("ram:",self.ram)
      print("camera:",self.camera)
      print("price:",self.price)
obj=Mobile("apple","4000mah",'4gb','48px','100000')
obj.display()

obj1=Mobile("realme","5000mah",'6gb','50px','20000')
obj1.display()
      
class students:
   def __init__(self,name,classno,rolln0,section,phno):
      self.name=name
      self.classno=classno
      self.rollno=rolln0
      self.section=section
      self.phno=phno
   def display(self):
      print("name:",self.name)
      print("classno:",self.classno)
      print("rollno:",self.rollno)
      print("section:",self.section)
      print("phno:",self.phno)
obj=students("vinith","first",'34',"B",'xxxxxxxx')
obj.display()
obj1=students("nithin","first",'44',"C",'xxxxxxxx')
obj.display()