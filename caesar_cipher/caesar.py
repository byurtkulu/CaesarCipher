'''
This is a Ceasar cipher encription and decription program. 
It can encript and decript a given sentence. 

'''

from random import randint
from time import sleep

alphabet = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
copy_of_alphabet_1 = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
copy_of_alphabet_2 = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
#copy of alphabet 1 and 2 are for shifting with the key

def key(): 
  # Shifts the alphabet with the random/choosen key
  
  key_choice = raw_input("Do you want to choose the key? (or key will be random..) (Y/N): ")
  key_choice = key_choice.upper()
  
  if key_choice == "Y":
    key = input("Enter the key (1-25): ")
    print "Shifting..."
    sleep(1)
  elif key_choice == "N":
    print "Choosing the key..."
    sleep(1)
    key = randint(1,25)             # use this key to shift
  else:
    print "invalid choice. Key is going to be random."
    sleep(1)
    key = randint(1,25)
  
  print "key: %s" % key 
  for element in sorted(copy_of_alphabet_1):
    copy_of_alphabet_1[element] += key     # shifting...
    copy_of_alphabet_1[element] = copy_of_alphabet_1[element] % 26
    print str(element) + ":" + str(copy_of_alphabet_1[element])

def encription():
  encripted_message = ""
  key()
  message = raw_input('Enter a message to encript:\n')   # Takes message from user
  message = message.upper()
  inverted_alphabet = {y:x for x,y in copy_of_alphabet_1.items()}   # To reach the messege we need inverted version of copy_of_alphabet!
  
  for char in message:

    if char in alphabet:  
      encripted_message += "%s" % inverted_alphabet[alphabet[char]]   # This part still makes me confused.. But it works!
    else:
      encripted_message += char
  print "message is being encripted..."
  sleep(2)
  print encripted_message

  



 
def decription():
  decripted_message = ""
  choice = raw_input("If you know the key please type 'key' and hit the enter, or program can try to solve it also. Type 'AI' and hit the enter: " )
  choice = choice.lower()
  if choice == "key":
    key = input("Enter the key (1-25): ")
    if key in range(1, 26):
      for element in sorted(copy_of_alphabet_2):
        copy_of_alphabet_2[element] += key     # shifting...
        copy_of_alphabet_2[element] = copy_of_alphabet_2[element] % 26
        print str(element) + ":" + str(copy_of_alphabet_2[element])
      while True:
        message = raw_input("Enter message to decript(type 'X' to stop): ")
        message = message.upper()
        inverted_alphabet = {y:x for x,y in alphabet.items()}

        if message == "X":
          print "Decription is stopping..."
          sleep(1)
          break
        else:  
          for char in message:
            if char in alphabet:
              decripted_message += "%s" % inverted_alphabet[copy_of_alphabet_2[char]]
            else:
              decripted_message += char          
          print "Decription in proccess. Please wait..."
          sleep(2)
          print decripted_message
          continue
  elif choice == "ai": # will guess by using frequency of letters
    frequency_alphabet = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
    message = raw_input("What is the message? :  ")
    message = message.upper()
    message = message.replace(" ", "")
    
    for letter in message: # detects the frequency of letters
      if letter in frequency_alphabet:
        frequency_alphabet[letter] += 1 
      else:
        pass
    print "Detecting the frequency of letters..."
    sleep(2)
    # print frequency_alphabet     -use this to print dictionary-
   
    for letter in frequency_alphabet: #prints the frequency of letters for user
      if frequency_alphabet[letter] > 0:
        print str(letter) + " = " + str(frequency_alphabet[letter])
      else:
        pass
    
    base_list = []
    base_num = 0
    base_letter = "A"
    
    for letter in frequency_alphabet:
      if frequency_alphabet[letter] >= base_num:
        base_num = frequency_alphabet[letter]
        base_letter = letter
      else:
        pass
    print "Base number: %.0f" % base_num
    print "Base letter: %s" % base_letter
    base_list.append(base_letter)
    print base_list
  else:
    print "invalid choice!"
    sleep(1)
        

print "welcome to Ceasar Cipher program!"
sleep(1)
while True:
  user_choice = raw_input("Do you want to 'encript' or 'decript' (type 'X' to exit): ")
  user_choice = user_choice.lower()
  if user_choice == "encript":
    print "Great let's start!"
    sleep(1)
    encription()
    continue
  elif user_choice == "decript":
    print "Get ready to decript!"
    sleep(1)
    decription()
    continue
  elif user_choice == "x":
    print "Exiting..."
    sleep(1)
    break
  else: 
    valid = raw_input("This is not a valid choice. Do you want to exit? (Y/N): ")
    valid = valid.upper()
    if valid == "Y":
      break
    elif valid == "N":
      continue
    else:
      print "Ok, you need a fresh air. Exiting..."
      sleep(1)
      break



      










