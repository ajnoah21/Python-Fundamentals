import string

def funct(name):
    #name = "" # comment out when done
    name.capitalize()
    out = name.count('o')
    return out
    

def main():
    name = "Corin Chepko"
    print(funct(name))

    phrase = "The pirates of the carribean, the scourge of the sea!"
    index=phrase.find("the")
    while(index != -1): # not == -1 means it's been found
        print(index, phrase[index:index+3])
        index = phrase.find("the",index+1)
    
    print(string.punctuation)
    new_str = ""
    for ch in phrase:
        if ch not in string.punctuation:
            new_str += ch
    print(new_str)

main()