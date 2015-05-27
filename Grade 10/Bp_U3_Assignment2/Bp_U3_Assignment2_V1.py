'''
Created on May 14, 2014

@author: Basil
'''

def menu():
    choice = raw_input('Which program would you like to run? 1-13, 'end' to quit\n>> ')
    if choice == '1':
        question1()
        menu()
        
    elif choice == '2':
        question2()
        menu()
        
    elif choice == '3':
        question3()
        menu()
        
    elif choice == '4':
        question4()
        menu()
        
    elif choice == '5':
        question5()
        menu()
        
    elif choice == '6':
        question6()
        menu()
    
    elif choice == '7':
        question7()
        menu()
    
    elif choice == '8':
        question8()
        menu()
    
    elif choice == '9':
        question9()
        menu()
    
    elif choice == '10':
        question10()
        menu()
    
    elif choice == '11':
        question11()
        menu()
    
    elif choice == '12':
        question12()
        menu()
    
    elif choice == '13':
        question13()
        menu()
    
    else:
        menu()

def question1():
    for i in range(0, 3):
        text = raw_input('Please enter a word\n>> ')
        print text.center(50)
        print text.rjust(50)
        i = i

def question2():
    
    text = ''
    
    while text != 'end':
        text = raw_input('Please enter a word, type end to quit\n>> ')
        if len(text) % 2 == 0: # If length of text is an even number
            text_middle = text[(len(text)/2) - 1 : (len(text)/2) + 1]
            
        elif len(text) % 2 != 0: # If length of text is an odd number
            text_middle = text[len(text)/2]
        
        print text_middle

def question3():
    
    text = ''
    
    while text != 'end':
        text = raw_input('Please enter a number in the format 12,123 type end to quit\n>> ')
        text = text.replace(',', '')
        print text

def question4():
    word1_upper = raw_input('Please enter a word, type end to quit\n>> ')
    word1 = word1_upper.lower()
    if word1 == 'end':
        menu()
    word2_upper = raw_input('Please enter another word, type end to quit\n>> ')
    word2 = word2_upper.lower()
    if word2 == 'end':
        menu()
    if len(word1) < len(word2):
        short_word = len(word1)
    else:
        short_word = len(word2)
    for i in range(short_word):
        if word1[i] > word2[i]:
            final = word2_upper, word1_upper
            break
        elif word1[i] < word2[i]:
            final = word1_upper + ' ' + word2_upper
            break
        else:
            if len(word1) > len(word2):
                final = word1_upper + ' ' + word2_upper
                break
            else:
                final = word2_upper + ' ' + word1_upper
                break
    print final

def question5():
    text = raw_input('Please enter a word, type end to quit\n>> ')
    if text.lower() == 'end':
        menu()
    print text.rfind('a')

def question6():
    text = raw_input('Please enter a sentence, type end to quit\n>> ')
    if text.lower() == 'end':
        menu()
    print text.title()
    if text.istitle() == True:
        print 'YES'
    else:
        print 'NO'
        
    '''
    str.title() turns the string into a title
    str.istitle() checks if it is a title
    '''

def question7():
    text = raw_input('Please enter a word, type end to quit\n>> ')
    text_len = len(text)
    text_space = []
    final = ''
    if text.lower() == 'end':
        menu()
    for i in range(text_len):
        text_space.append(text[i] + ' ')
    for i in range(len(text_space)):
        final += text_space[i]
    print final

def question8():
    text = raw_input('Please enter a word, type end to quit\n>> ')
    final = ''
    if text.lower() == 'end':
        menu()
    for i in range(len(text), 0, -1):
        final += text[i-1]
    print final

def question9():
    text = raw_input('Please enter a word, type end to quit\n>> ')
    final = ''
    if text.lower() == 'end':
        menu()
    for i in range(len(text), 0, -1):
        final += text[i-1]
    if final == text:
        print 'Yes,', text, 'is a palindrome'
    else:
        print 'No,', text, 'is not a palindrome'

def question10():
    prefixes = 'JKLMNOPQ'
    suffix = 'uack'
    
    for i in prefixes:
        print i + suffix

def question11():
    word = raw_input('Please enter a word, type end to quit\n>> ')
    if word.lower() == 'end':
        menu()
    char = raw_input('Please enter the letter to count, type end to quit\n>> ')
    if char.lower() == 'end':
        menu()
    def count_letters(word, char):
        count = 0
        for letter in word:
            if letter == char:
                count += 1
        print count
    count_letters(word, char)

def question12():
    text = raw_input('Please enter a word or sentence to count the vowels, type end to quit\n>> ')
    if text.lower() == 'end':
        menu()
    count = 0
    for i in text:
        if i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u' or i.lower() == 'y':
            count += 1
    print count

def question13():
    text = ''
    
    while text != 'end':
        text = raw_input('Please enter a word, type end to quit\n>> ')
        if len(text) % 2 == 0: # If length of text is an even number
            text_middle = text[(len(text)/2) - 1 : (len(text)/2) + 1]
            text_old = text.replace(text_middle, '')
            
        elif len(text) % 2 != 0: # If length of text is an odd number
            text_middle = text[len(text)/2]
            text_old = text.replace(text_middle, '')
        
        new_text = text_old + text_middle
        print new_text

menu()