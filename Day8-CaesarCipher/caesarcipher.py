from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print(logo)
#1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    new_text = []
    for letter in text:
        if (alphabet.index(letter)+shift > 25):
            new_text.append(alphabet[(alphabet.index(letter)+shift)-26])
        else:
            new_text.append(alphabet[alphabet.index(letter)+shift])

    print(f"The encoded text is {''.join(new_text)}")

def decrypt(text, shift):
    new_text = []
    for letter in text:
        if (alphabet.index(letter)-shift < 0 ):
            new_text.append(alphabet[(alphabet.index(letter)-shift)+26])
        else:
            new_text.append(alphabet[alphabet.index(letter)-shift])
    
    print(f"The decoded text is {''.join(new_text)}")

#2 ask the user for the parameters
while True:
    try:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction != 'encode' and direction != 'decode':
            raise
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if direction == 'encode':
            encrypt(text, shift)
        else:
            decrypt(text, shift)
        cont = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if cont == 'yes':
            continue
        else:
            print('Good Bye!')
            break          
    except:
        print('Please, insert valid paramenters')




#2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#e.g. 
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 