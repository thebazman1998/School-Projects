'''
Created on May 22, 2014

@author: Basil
'''

encode_cipher = {'a':'f', 'b':'e', 'c':'a', 'd':'t', 'e':'h', 'f':'r', 'g':'z', 'h':'y', 'i':'x', 'j':'w', 'k':'v', 'l':'u', 'm':'s', 'n':'q', 'o':'p', 'p':'o', 'q':'n', 'r':'m', 's':'l', 't':'k', 'u':'j', 'v':'i', 'w':'g', 'x':'d', 'y':'c', 'z':'b', ' ':' '}

decode_cipher = {'f':'a', 'e':'b', 'a':'c', 't':'d', 'h':'e', 'f':'r', 'z':'g', 'y':'h', 'x':'i', 'w':'j', 'v':'k', 'u':'l', 's':'m', 'q':'n', 'p':'o', 'o':'p', 'n':'q', 'm':'r', 'l':'s', 'k':'t', 'j':'u', 'i':'v', 'g':'w', 'd':'x', 'c':'y', 'b':'z', ' ':' '}

def menu():
    choice = raw_input('Would you like to encode? or decode? Type end to quit.\n>> ').lower()
    
    if choice == 'encode':
        encode()
        menu()
    
    elif choice == 'decode':
        decode()
        menu()
    
    elif choice != 'end':
        menu()

def encode():
    text = raw_input('Enter the text to encode\n>> ')
    end_text = []
    for i in text:
        encoded_char = encode_cipher[i]
        end_text.append(encoded_char)
    print end_text

def decode():
    text = raw_input('Enter the text to encode\n>> ')
    end_text = []
    for i in text:
        decoded_char = decode_cipher[i]
        end_text.append(decoded_char)
    print end_text

menu()