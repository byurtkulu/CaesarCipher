'''
This is a Ceasar cipher encription and decription program. 
It can encript and decript a given sentence. 

'''

from random import randint

alphabet = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
copy_of_alphabet_1 = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
copy_of_alphabet_2 = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
#copy of alphabet 1 and 2 are for shifting with the key

def key(): 
  # Shifts the alphabet with the random key
  key = randint(1,25)             # use this key to shift
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
        message = raw_input("Enter message to decript(type 'EXIT' to stop): ")
        message = message.upper()
        inverted_alphabet = {y:x for x,y in alphabet.items()}

        if message == "EXIT":
          break
        else:  
          for char in message:
            if char in alphabet:
              decripted_message += "%s" % inverted_alphabet[copy_of_alphabet_2[char]]
            else:
              decripted_message += char          
          print decripted_message
          continue
  elif choice == "ai":
    print "coming soon..."
  else:
    print "invalid choice"
        

encription()
decription()

      










