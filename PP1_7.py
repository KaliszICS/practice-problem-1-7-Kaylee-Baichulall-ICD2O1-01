'''
    Lesson: Booleans
    Author: Kaylee Baichulall
    Date Creatd: Sept 25, 2024
    Date Last Modified: Sept 26, 2024
'''

def q1():
  bool1 = 1 < 2
  print(bool1)

def q2():
  userInt1 = input("Input an integer: ")
  userInt1 = int(userInt1)
  bool2 = userInt1 > 5
  print(bool2)

def q3():
  userWord1 = input("Input the letter a: ")
  bool4 = userWord1 == "a"
  print(bool4)

def q4():
  userWord2 = input("Input a word earlier in the dictionary than google: ")
  bool5 = userWord2 < "google"
  print(bool5)

def q5():
  userInt5 = input("Input an integer: ")
  userInt6 = input("Input another integer: ")
  userInt5 = int(userInt5)
  userInt6 = int(userInt6)
  num = userInt5 * userInt6
  bool5 = num > 40
  print(f"Your numbers multiplied together are greater than 40: {bool5}")

#Do edit the code below
#Comment the lines below when running your tests
'''
q1()
q2()
q3()
q4()
q5()
'''
