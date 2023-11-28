'''
Name: Corin Chepko
Date: 10/23/23
Program Description: https://open.kattis.com/problems/piglatin
Algorithm:
    input a phrase
    for each word:
        if begins with vowel:
            add 'yay' to word
        if not (begins with consonant):
            take all letters before first vowel, add 'ay' to it and add that to the rest of the word
        add revised word to translated phrase
'''
def test():
    pass

def translate(phrase):
    translated = []
    vowels = ['a','e','i','o','u','y']
    for word in phrase:
        if word[0] in vowels:
            new_word = word + 'yay'
        else:
            consonants = ""
            index=0 
            for ch in word:
                if ch in vowels:
                    break
                consonants += ch
                index += 1

            end = consonants + 'ay'
            new_word = word[index::] + end
        
        #print(new_word)
        translated.append(new_word)
    
    return ' '.join(translated)

def main():
    
    
    while(True):
        try:
            phrase = input()
        except EOFError:
            break
        phrase = phrase.split()
        new_phrase = translate(phrase)
        print(new_phrase)
        #phrase = input().split()
        
# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()