import time
import random
import string
from text import type

type("Welcome to Password Generater/Cracker!!!")
type("Version 1.8\n by: Abdifitah")

LOWERCASE = list(string.ascii_lowercase)
UPPERCASE = list(string.ascii_uppercase)
password = ""
like = ""

Charectors = LOWERCASE + UPPERCASE + ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

type("Do you want a custom password or random? (c or r) WARNING:\nMORE THAN 3 CHARECTORS TAKES A LONG TIME!: ")
if input() == "r":
  type("How long should the password be? (An int more than 0 and less than 11):\n")
  lenght = input()
  
  password = ""
  for lenght in range(int(lenght)):
    password += random.choice(Charectors)
  
  type("The password is:\n" + password)
else:
  type("What do you want the password to be?:\n")
  password = input()

if input("Would you like to crack the password? (y or n): ") != "y":
  while True:
    type("Goodbye!!!!")
do_i_print = False

if input("Would you like to see the computor solve(WARNING TAKES LONGER)? (y or n)") == "y":
  do_i_print = True

guess   = ""
dots    = 0
cracked = False

type("Cracking password with brute force...")

tested = 0

start = time.time()
while cracked == False:

  #_____________1 Char____________
  for c1 in Charectors:
    if guess != password:
      tested += 1
      test = c1
      if do_i_print == True:
        print(test)
      if c1 == password:
        guess = test
        end = time.time()
        timer = str(end - start)
        print("It took ", tested, "tries and ", timer, "seconds to crack the password: ", password)
        break 
        
  #___________2 Char____________
  for c1 in Charectors:
    for c2 in Charectors:
      if guess != password:
        tested += 1
        
        test = c1 + c2
        
        if do_i_print == True:
          print(test)
        if test == password:
          guess = test
          end = time.time()
          timer = str(end - start)
          print("It took ", tested, "tries and ", timer, "seconds to crack the password: ", password)
          break
  #__________3 Char__________
  for c1 in Charectors:
    for c2 in Charectors:
      for c3 in Charectors:  
        if guess != password:
          tested += 1
          
          test = c1 + c2 + c3
          
          if do_i_print == True:
            print(test)
          if test == password:
            guess = test
            end = time.time()
            timer = str(end - start)
            print("It took ", tested, "tries and ", timer, "seconds to crack the password: ", password)
            break

  #_________4 Char__________
  for c1 in Charectors:
    for c2 in Charectors:
      for c3 in Charectors:
        for c4 in Charectors:  
          if guess != password:
            tested += 1
            
            test = c1 + c2 + c3 + c4
            
            if do_i_print == True:
              print(test)
            if test == password:
              guess = test
              end = time.time()
              timer = str(end - start)
              print("It took ", tested, "tries and ", timer, "seconds to crack the password: ", password)
              break
  #_________5 Char__________
  for c1 in Charectors:
    for c2 in Charectors:
      for c3 in Charectors:
        for c4 in Charectors:
          for c5 in Charectors:  
            if guess != password:
              tested += 1
              
              test = c1 + c2 + c3 + c4 + c5
              
              if do_i_print == True:
                print(test)
              if test == password:
                guess = test
                end = time.time()
                timer = str(end - start)
                print("It took ", tested, "tries and ", timer, "seconds to crack the password: ", password)
                break
  #_________6 Char__________
  for c1 in Charectors:
    for c2 in Charectors:
      for c3 in Charectors:
        for c4 in Charectors:
          for c5 in Charectors:
            for c6 in Charectors:  
              if guess != password:
                tested += 1
                
                test = c1 + c2 + c3 + c4 + c5 + c6
                
                if do_i_print == True:
                  print(test)
                if test == password:
                  guess = test
                  end = time.time()
                  timer = str(end - start)
                  print("It took ", tested, "tries and ", timer, "seconds to crack the password: ", password)
                  break

  #_________7 Char__________
  for c1 in Charectors:
    for c2 in Charectors:
      for c3 in Charectors:
        for c4 in Charectors:
          for c5 in Charectors:
            for c6 in Charectors:  
              for c7 in Charectors:
                if guess != password:
                  tested += 1
                  
                  test = c1 + c2 + c3 + c4 + c5 + c6 + c7
                  
                  if do_i_print == True:
                    print(test)
                  if test == password:
                    guess = test
                    end = time.time()
                    timer = str(end - start)
                    print("It took ", tested, "tries and ", timer, "seconds to crack the password: ", password)
                    break

  #_________8 Char__________
  for c1 in Charectors:
    for c2 in Charectors:
      for c3 in Charectors:
        for c4 in Charectors:
          for c5 in Charectors:
            for c6 in Charectors:  
              for c7 in Charectors:
                for c8 in Charectors:
                  if guess != password:
                    tested += 1
                    
                    test = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8
                    
                    if do_i_print == True:
                      print(test)
                    if test == password:
                      guess = test
                      end = time.time()
                      timer = str(end - start)
                      print("It took ", tested, "tries and ", timer, "seconds to crack the password: ", password)
                      break

    #_________9 Char__________
  for c1 in Charectors:
    for c2 in Charectors:
      for c3 in Charectors:
        for c4 in Charectors:
          for c5 in Charectors:
            for c6 in Charectors:  
              for c7 in Charectors:
                for c8 in Charectors:
                  for c9 in Charectors:
                    if guess != password:
                      tested += 1
                      
                      test = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9
                      
                      if do_i_print == True:
                        print(test)
                      if test == password:
                        guess = test
                        end = time.time()
                        timer = str(end - start)
                        print("It took ", tested, "tries and ", timer, "seconds to crack the password: ", password)
                        break

    #_________10 Char__________
  for c1 in Charectors:
    for c2 in Charectors:
      for c3 in Charectors:
        for c4 in Charectors:
          for c5 in Charectors:
            for c6 in Charectors:  
              for c7 in Charectors:
                for c8 in Charectors:
                  for c9 in Charectors:
                    for c10 in Charectors:
                      if guess != password:
                        tested += 1
                        
                        test = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10
                        
                        if do_i_print == True:
                          print(test)
                        if test == password:
                          guess = test
                          end = time.time()
                          timer = str(end - start)
                          print("It took ", tested, "tries and ", timer, "seconds to crack the password: ", password)
                          break

  if guess == password:
    cracked = True