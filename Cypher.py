#Devyn Pruden 100828479 & Liam Pruden 100924161
from tkinter import *
import random

class Message:
    def __init__(self, message=''):
        # Initialize the Message object 
        self.__message = message

    def set_message(self, message):
        self.__message = message

    def get_message(self):
        # get the message stored in the object.
        return self.__message

    def encrypt(self):
        # Placeholder method for encryption
        pass

    def decrypt(self):
        # Placeholder method for decryption
        pass

class Substitution(Message):
    def __init__(self, message=''):
        super().__init__(message)
        #this will be used to layout the groundwork for the cypher, for ex 'a' will become 'm' etc
        self.substitution_dict = {
            'a': 'm', 'b': 'n', 'c': 'b', 'd': 'v', 'e': 'c', 'f': 'x', 'g': 'z', 'h': 'a', 'i': 's', 'j': 'd',
            'k': 'f', 'l': 'g', 'm': 'h', 'n': 'j', 'o': 'k', 'p': 'l', 'q': 'p', 'r': 'o', 's': 'i', 't': 'u',
            'u': 'y', 'v': 't', 'w': 'r', 'x': 'e', 'y': 'w', 'z': 'q', ' ': ' ',
        }

        self.reverse_dict = {a: b for b, a in self.substitution_dict.items()}  # Reverse the dictionary to decrypt

    def encrypt(self):
        # Encrypts the message using a substitution cipher
        encrypted_message = ""
        for char in self.get_message().lower():
            if char in self.substitution_dict:  # Check if the character is in the dictionary
                encrypted_message += self.substitution_dict[char]  # Swaps the letter with corresponding letter
            else:
                encrypted_message += char  # If not in the dictionary, don't change (accounts for punctuation)
        self.set_message(encrypted_message)

    def decrypt(self):
        # Decrypts the message using a substitution cipher
        decrypted_message = ""
        for char in self.get_message().lower():
            if char in self.reverse_dict:
                decrypted_message += self.reverse_dict[char]
            else:
                decrypted_message += char
        self.set_message(decrypted_message)

class Caesarcypher(Message):
    def __init__(self, message='', shift=3):
        super().__init__(message)
        self.shift = shift

    def encrypt(self):
        # Encrypts the message using the Caesar cipher with a specified shift
        encrypted_message = ""
        for char in self.get_message():
            if char.isalpha():
                if char.isupper():
                    encrypted_message += chr((ord(char) - 65 + self.shift) % 26 + 65)
                else:
                    encrypted_message += chr((ord(char) - 97 + self.shift) % 26 + 97)
            else:
                encrypted_message += char
        self.set_message(encrypted_message)

    def decrypt(self):
        # Decrypts the message using the Caesar cipher with a specified shift
        decrypted_message = ""
        for char in self.get_message():
            if char.isalpha():
                if char.isupper():
                    decrypted_message += chr((ord(char) - 65 - self.shift) % 26 + 65)
                else:
                    decrypted_message += chr((ord(char) - 97 - self.shift) % 26 + 97)
            else:
                decrypted_message += char
        self.set_message(decrypted_message)

class ProductCypher(Message):
    def __init__(self, message=''):
        super().__init__(message)

    def encrypt(self):

        substitution = Substitution(self.get_message())
        substitution.encrypt() #encrypts message w/ substiution cypher
        caesar = Caesarcypher(substitution.get_message())
        caesar.encrypt() #encrypts the encrypted message w/ caesar cypher
        self.set_message(caesar.get_message())

    def decrypt(self):
        caesar = Caesarcypher(self.get_message())
        caesar.decrypt() #decrypts message w/ caesar decypher
        substitution = Substitution(caesar.get_message())
        substitution.decrypt() #decrypts message w/ substiution decypher
        self.set_message(substitution.get_message())


class PlayFairCypher(Message):
    def __init__(self, message=''):
        super().__init__(message)

    def FiveByFiveSquare(self):
        pass #create a 5x5 square w/ alphabet

    def prepare(self):
        pass

    def split(self):
        pass #Split words into groups of 2

    def encrypt(self):
        pass

    def decrypt(self):
        pass


class RSAcypher(Message):
    def __init__(self, message=''):
        super().__init__(message)
        # Prime numbers for demonstration
        self.prime_one = 541
        self.prime_two = 547
        # Calculate modulus and phi
        self.modulus = self.prime_one * self.prime_two
        self.phi = (self.prime_one - 1) * (self.prime_two - 1)
        # public exponent
        self.public_exponent = 65537
        # private exponent
        self.private_exponent = 194633

    def encrypt(self):
        # Encrypts the message using RSA encryption
        encrypted_msg = []
        for character in self.get_message():
            char_ascii = ord(character)
            cypher_num = pow(char_ascii, self.public_exponent, self.modulus)
            encrypted_msg.append(str(cypher_num))
        self.set_message(" ".join(encrypted_msg))

    def decrypt(self):
        # Decrypts the message using RSA decryption
        decrypted_msg = ""
        encrypted_values = self.get_message().split()
        for num in encrypted_values:
            cypher_num = int(num)
            char_ascii = pow(cypher_num, self.private_exponent, self.modulus)   #encrypts using the RSA algorithm with public exponent and modulus.
            decrypted_msg += chr(char_ascii)
        self.set_message(decrypted_msg)

class TranspositionCypher(Message):
    def __init__(self, message=''):
        super().__init__(message)

    def encrypt(self):
        # Convert the text into a list
        chars = list(self.get_message())
        n = len(chars)
        for i in range(n // 2):
            # Swap the character at position i with the character at n-i-1 (n-i-1 can be changed to alter the shuffling)
            chars[i], chars[n - i - 2] = chars[n - i - 2], chars[i]
        # Convert the list back into a string
        self.set_message(''.join(chars))

    def decrypt(self):
        #applying the encryption twice will return the original form
        self.encrypt()


class cypherGUI:
    def __init__(self):
        # Set up the main window
        self.window = Tk()
        self.window.title("Cipher GUI by Devyn & Liam")

        # Input area for text 
        Label(self.window, text="Enter text:").grid(row=0, column=0, sticky=W)
        self.user_entry = Entry(self.window, width=25, bg="white")
        self.user_entry.grid(row=0, column=1, columnspan=2)

        # Buttons to trigger encryption and decryption
        Button(self.window, text="Encrypt", command=self.encrypt, bg="orange").grid(row=1, column=1, sticky=W)
        Button(self.window, text="Decrypt", command=self.decrypt, bg="lightblue").grid(row=1, column=2, sticky=W)

        # Result of the encryption or decryption.
        self.result_label = Label(self.window, text="Result:", fg="black", bg="white")
        self.result_label.grid(row=2, column=0, columnspan=3)

        # Indicates which cipher was used 
        self.cypher_label = Label(self.window, text="Used Cipher:", fg="black", bg="white")
        self.cypher_label.grid(row=3, column=0, columnspan=3)

        # Dictionary 
        self.cyphers = {
            "substitution": Substitution(""),
            "caesar": Caesarcypher(""),
            "product": ProductCypher(""),
            "RSA": RSAcypher(""),
            "Transposition": TranspositionCypher(""),
        }
        self.last_cypher_used = None  
        self.last_encrypted_text = ""  

    def encrypt(self):
        # Handles the encryption process.
        text = self.user_entry.get()
        cypher_choice = random.choice(list(self.cyphers.keys()))  # Randomly selects a cipher.
        cypher = self.cyphers[cypher_choice]
        cypher.set_message(text)
        cypher.encrypt()

      
        result = cypher.get_message()
        self.result_label.config(text=f"Result: {result}")
        self.cypher_label.config(text=f"Used Cipher: {cypher_choice.capitalize()}")
        self.last_cypher_used = cypher_choice
        self.last_encrypted_text = result

    def decrypt(self):
        # Handles the decryption process using the last cipher used.
        if not self.last_cypher_used:
            # alert if no encryption is preformed
            self.result_label.config(text="Result: No encryption performed yet!")
            return

        cypher = self.cyphers[self.last_cypher_used]
        cypher.set_message(self.last_encrypted_text)
        cypher.decrypt()

        # Update the GUI with the decryption result.
        result = cypher.get_message()
        self.result_label.config(text=f"Result: {result}")

gui = cypherGUI()
gui.window.mainloop()


