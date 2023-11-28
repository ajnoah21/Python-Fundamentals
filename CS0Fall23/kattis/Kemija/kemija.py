'''
Name: Corin Chepko
Date: 10/23/23
Program Description: https://open.kattis.com/problems/kemija08
Algorithm: Translate string;
    input phrase
    split phrase into list
    for each word:
        read chars until encounter a vowel, remove next two charcters
        proceed
'''

def test():
    pass

def main():
    vowels = ('a','e','i','o','u')
    phrase = input().split()
    translated = []
    for word in phrase:
        new_word = ""
        i=0
        while(i < len(word)):
            new_word += word[i]
            if word[i] in vowels:
                i += 3
                continue
            i+=1
        translated.append(new_word)
    print(' '.join(translated))
            



# if I'm the main program, run my main function,
#  otherwise just my functions are available
if(__name__ == '__main__'):
    main()