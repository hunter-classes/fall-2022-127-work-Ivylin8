#extras:
#1: opended a story file and read the lines from it
#2: Used proper lettercases for beginning of sentences

from random import randint
#sets up dict
word_dict = {
    '<HERO>' :['Sam', 'Nate', 'Jen', 'Carl'],
    '<LOCATION>' :['beach', 'playground', 'store', 'mall', 'school', 'basement'],
    '<NOUN>' :['bear', 'rocket', 'kangaroo', 'shark'],
    '<VERB>' : ['jumped', 'walked', 'ran', 'skipped', 'laughed']
}

#sets up list of special words
special_words = ['<HERO>', '<LOCATION>', '<NOUN>', '<VERB>']

result = ''

def is_punctuated(word):
    last_char = word[-1] #get the last character of a word
    if (last_char == '.'): #last character is a punctuation mark or else
        return True
    else:
        return False

def remove_punctuation(word):
    if (is_punctuated(word) == True):
        return word[0:len(word) - 1] #gets rid if there is
    else:
        return word 

def remove_newline(word):
    last_char = word[-1] 
    if (last_char == '\n'): 
        return word[0:len(word) - 1] #remove the last character if it is a newline
    else:
        return word

#open story file and read the lines from it
f = open('story.txt')
story = f.readlines()
for line in story: 
    words = line.split(' ') #splits into list of words 
    for word in words: 
        no_newline_word = remove_newline(word)
        processed_word = remove_punctuation(no_newline_word) #remove punctuation from the word
            
        if (processed_word in special_words): #spot special word
            word_dict_entry = word_dict[processed_word] #uses special word
            random_index = randint(0, len(word_dict_entry) - 1)
            result += ' ' + word_dict_entry[random_index] 
            
            if (is_punctuated(no_newline_word)):
                result += no_newline_word[-1] 
        else:
            result += ' ' + no_newline_word 
    result += '\n' 
f.close() 

print('madlib:\n' + result) 
