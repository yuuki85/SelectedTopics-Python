number = 0
while number < 10:
    number +=3
    if number == 9:
        continue
    print (number)

varl = 'Welcome to UniKL'
var2 = 'SE tOPICS cOURSE'
print ( "varl[0]:", varl[0:7])
print ( "var2[1:5]:", var2[3:5])

numbers =[1,3,5,2,8]
even_num = {x: x ** 2 for x in numbers if x % 2 == 0}
print (even_num)

A = 0
while A<7:
    A += 1
    if A == 4:
        continue
    print (A)

for i in range(7):
    if i % 2 == 0 and i % 3 == 0:
        print (i)
    elif i % 2 == 0:
        print (i)
    elif i % 3 == 0:
        print (i)

a = 1
while a < 7:
    print (a)
    if a == 4:
        break
    a+=1

a=1
while a< 7:
    print (a)
    a+=1
else:
    print (a)

a = 0
for a in range(1,7):
    a = a+1
    if a>6:
        break
    else:
        print (a)


myListNo = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print('Output:',myListNo[0])

print('Output:',myListNo[0: 5])


myListNo.append(10)
print('Output:',myListNo)

myListNo.extend([11,0])
print('Output:',myListNo)

myListNo.insert(5, 6)
print('Output:',myListNo)


mesg1 = 'Universiti Kuala Lumpur'
mesg2 = "MIIT" 
#q1
print (mesg1.upper( ) )
#q2
print (mesg2.lower ( ) )
#q3
print('WELCOME TO' . lower())
#q4
print (len(mesg1))
#q5
print ("mesg1[0]:", mesg1[0])
#q6
print ("mesg2[1:5]:", mesg2[1:5])
#q7
print (mesg1[0:4])
#q8
print  (mesg1[6:7])
#q9
print (mesg1[6:20])
#q10
print (mesg2[2:])




word= "banana" 
count=0
for letter in word:
    if letter == "a":
        count = count + 1
        print ("Number of a in", word, "is:",count)

largest = None
for val in [9, 1, 11]:
    if largest is None or val > largest:
        largest = val
    print ("Loop", val,"Largest" ,largest)

class Person():
    def __init__(self, name):
        self.name = name
        self.__course = 'Python' # (QI)
        self.__education = 'UniKL'
        
    def displayInfo(self):
        name = self.name
        course = self.__course
        education = self.__education
        print('My name is', name, ', I study in', education, 'and I love', course) # (QII)
        
if __name__ == '__main__':
    myObj = Person('Peter Pan')
    myObj.displayInfo() # (QIV)
    print(myObj.name) 
    print(myObj._Person.education) # (QV)

class Pet:
    def eat(self):
        print( "Cat can eat!")
    def sleep(self):
        print( "Cat can sleep!")

class Cat(Pet):
    def meow(self) :
        print( "Cat sound is Meow Meow!")
    def climb(self) :
        print( "Cat can climb")
cat1 = Cat()
cat1.eat( )
cat1.sleep( )

x = 1
while x <=5: print(x,end=" "); x =x+1

fruit = 'durian'
letter= fruit[1]
print (letter)
index=3
w = fruit[index-1]
print (w)
print (len(fruit))