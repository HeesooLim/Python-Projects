#----------------------------------------------------------------------------
# File name   : 7_caesar-cipher.py
# Created By  : Heesoo Lim
# Created Date: 20/01/2022
# ---------------------------------------------------------------------------

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(is_encoding, message, shift):
  # message to return
  result_message = ""
  for m in message:
    # if m is not a letter in the list, not encode or decode
    if m not in letters:
      result_message += m
    else:
      # find the index of letter
      i = letters.index(m)
      if is_encoding:
        i += shift
      else:
        i -= shift
      # add the encoded letter to the string
      result_message += letters[(i) % 26]
  return result_message

print("""
 ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗     
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗    
██║     ███████║█████╗  ███████╗███████║██████╔╝    
██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗    
╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║    
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    
                                                    
 ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗          
██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗         
██║     ██║██████╔╝███████║█████╗  ██████╔╝         
██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗         
╚██████╗██║██║     ██║  ██║███████╗██║  ██║         
 ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝  
""")
# repeat the program 
while True:
  # check the type of encryption user wants
  encryption_type = input("Please type 'encode' to encrypt, 'decode' to decrypt.\n").lower()
  # get the message that the user wants to encode or decode
  message = input("Type the message to encode or decode:\n").lower()
  shift = int(input("Type the number of shift: \n"))

  if encryption_type == "encode":
    print(f"\nEncoded message:\n{caesar_cipher(True, message, shift)}\n")
  elif encryption_type == "decode":
    print(f"\nDecoded message:\n{caesar_cipher(False, message, shift)}\n")
  else:
    print("please try again with a valid input.\n")
    break
  answer = input("Type 'yes' if you want to continue. Otherwise type any other key.\n")
  print("___________________________________________________________\n")

  # stop the program if the user types yes
  if answer.lower() != "yes":
    break
  
    
