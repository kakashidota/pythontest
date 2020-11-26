
#int
age = 29

print(age)

age = 10

print (age)

#float
pi = 3.14

print(pi)


#math

pi = 3.14

radius = 5

area = pi  * radius * radius

print(area)

#avancerad matte

pi = 3.14
radius = 5
area = pi * radius ** 2

#Division
div = 5/3
divutanDecimaler = 5 // 3
modulo = 5 % 3

print(div)
print(divutanDecimaler)
print(modulo)

#round
#Dividera 365.25 med 7 och avrunda till en decimail. Tildela sedan värde
#till en variabel som heter weeks

#Round tar två argument, första är talet, andra är decimaler
weeks = round(365.25 / 7, 1)
print(weeks)


#Conversion
print(int(area))

"""Potato """

mystory = "He doesn'nt like to eat chees"

anotherstory = "He dosent  like poato"

#Concetation
print(anotherstory * 3)

#Format
age = 29
height = 187

print("my age is {} and im {} cm tall".format(age, height))


#string formation
name = "KaKan"
mening = "Bob heter Frank och Frank heter Jose"

print(name.upper())

print(name.lower())

print(len(name))

print(mening.replace("Bob", "Matilda"))

print(mening.split())

#tar ut en char
print(mening[2])

print(mening[0:5])


# if else elif

sunny = True

if sunny:
    print("Sunny")

else:
    print("Not sunny")


#elif
a = -1

if a > 4:
    print("bigger then 4")
elif a > 0:
    print("bigger then 0 but less then 4")
else:
    print("less then 0")

#And and or
a = 6

if 7 >= a >= 5 and a % 2 == 0:
        print("Between 5 and 7")



#Functions
def hello():
    print("Hello world")
    print("Yes helloS")

hello()

def addtwo(num1, num2):
    print(num1+num2)

addtwo(int(input()),int(input()))

def story(name = "frank", verb, noun):
    print(name + "was" + verb + " with " + noun)

story("ahmed", "frank", "Runnings")
