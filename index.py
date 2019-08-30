# Problem 1:
# Ask a user for the year they were born by calculating their age.
# Assuming they already had their birthday and it’s 2019 print “You are [AGE] years old”

# def figureAge():
#     question = int(input('what year were you born?'))
#     age = 2019 - question
#     print(f'you are {age} years old')
#
# figureAge()

# Problem 2:
#
# Ask the user for a string. If they enter “Kenn”, “Kevin”, “Erin”, or “Autumn” print “Hello Teacher”. Otherwise print “Hello Student”

# def ask4String():
#
#     gimmeString = input("Enter a string")
#     if gimmeString == 'kenn':
#         print('Hello Teacher')
#     elif gimmeString == 'kevin':
#         print('Hello Student')
#     elif gimmeString == 'erin':
#         print('Hello teacher')
#     elif gimmeString == 'kevin':
#         print('Hello teacher')
#     elif gimmeString == 'autumn':
#         print('Hello teacher')
#     else:
#         print('Hello student')
#
# ask4String()

# Problem 3:
#
# Ask the user for a negative number. Print from 7 down to the user's negative number. You must include the user's number.
#
# negNum = int(input('Enter a negative number'))
# for i in range(7,negNum -1, -1):
#     print(i)

# Problem 4:
#
# Ask the user to enter a number between -10 to -5.
# If their input is not between the two numbers ask them to do it again until they get it right.
# Afterward they print the correct number, print "Good job"
# num = -1
# numBetween = -2
# while num != numBetween:
#     num = int(input('enter number between -10 to -5'))
#     numBetween = num < -10 or num > -5
# if num == numBetween:
#     print('try  again')
# else:
#     print('good job')

# Problem 5:
#
# Create the list: squad = ["One", "Two", "Three", "Four", "Five"]. Print the list in reverse without using a list method.

# squad = ["One", "Two", "Three", "Four", "Five"]
#
# print(squad[-1:]) # just prints 5

# Problem 6:
#
# Create a function that will have the string firstName as a parameter. In the function ask the user for their last name.
# Print "Hello [FIRST & LAST NAME]" in the function. Call that function
#
# def name(fname):
#     last = input('what is your last name?')
#     print(f'Hello {fname + last}')
#
# name('Dekevion ')
#
# Problem 7:
#
# Create the class Books with name, rating, genre, and author properties/attributes. Create a class method that will change the rating of the book. Outside of the class, create three objects of the class Book and put them in an array. Lastly, USING THE ARRAY print only the names of the books using any method we’ve learned in class.
#

# class Book:
#     def __init__(self,name, rating,genre, author):
#         self.name = name
#         self.rating = rating
#         self.genre = genre
#         self.author = author
#     def changeRating(self,newRating):
#         self.rating = newRating
#
# book1 = Book('good','5/5', 'thriller','me')
# book2 = Book('bad','1/5', 'zzz','him')
# book3 = Book('ok','3/5', 'snooze','we')
# bookArray = [book1, book2, book3]

# Problem 8:
#
# Create a function that asks the user to enter a number. If the number is between and include -50 and 5, return "Funds too low". If the number is between 5 and 50, return “You should add more funds.” If the number is more than 50, return “Just enough.”
#
# def num():
#     giveNum = int(input('enter a number'))
#
#     if giveNum > -50 or giveNum < 5:
#         print('funds too low')
#     elif giveNum >= 5 or giveNum <= 50:
#         print('you should add more funds')
#     elif giveNum > 50:
#         print('just enough')
#
#
# num()
#
#


# Problem 9:
#
# Ask the user for a positive number. Create an empty array and starting from zero, add each number by 1 into the array. Print EACH ELEMENT of the array.
emptyArray = []
posNum = int(input('enter a positive number'))
emptyArray.append(posNum)
print(emptyArray)
#
# Problem 10:
#
# Create a new empty array called pet_list. Create a Pet class with a type and breed attribute/property. Include a method that will print each attribute/property. Add 3 pet objects to the pet_list array. Print the attributes/properties for each pet.


petL