#extras:
#1: Store file in pirate dat
#2: Handle upper and lower case and/or punctuation

#this will read story file 
file = open("input.txt", "r")
content = file.read()
print(content)
file.close()

pirate_speech = []
story = ''.join(pirate_speech)

#Handle Punctions
def is_punctuated(word):
    last_char = word[-1] #get the last character of a word
    if (last_char == '.' or last_char == '!' or last_char == '?'): #last character is a punctuation mark or else
        return True
    else:
        return False

def remove_punctuation(word):
    if (is_punctuated(word) == True):
        return word[0:len(word) - 1] #gets rid if there is
    else:
        return word 


#translate to pirate language 
def toPirate(dictionary):
    pirateDic = {
    "Hello":"avast",
    "excuse":"arrr",
    "sir":"matey",
    "boy":"matey",
    "man":"matey",
    "hi":"ahoy",
    "officer":"foul blaggart",
    "the":"th'",
    "my":"me",
    "your":"yer",
    "is":"be",
    "are":"be",
    "before":"afore",
    "the":"th'",
    "earlier":"afore",
    "people":"landlubbers",
    "there":"thar"}
    
    pirateDictionary=''
    wordList=dictionary.split()
    for i in wordList:
        if i in pirateDic:
            i=pirateDic[i]
        pirateDictionary=pirateDictionary+' '+i
    return pirateDictionary
print(toPirate(" Hello sir, the officer wants me to question the people. The boy was chased down. My legs came off as I chased the boy."))

    
