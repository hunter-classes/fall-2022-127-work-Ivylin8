#extras:
#1: opended a story file and read the lines from it
#2: Used proper lettercases for beginning of sentences

from random import randint

#sets up dictionary 
word_dict = {
    '<HERO>' :['Sam', 'Nate', 'Jen', 'Carl'],
    '<LOCATION>' :['beach', 'playground', 'store', 'mall', 'school', 'basement'],
    '<ADJECTIVE>' :['muscular', 'bewildered', 'colossal', 'witty'],
    '<NOUN>' :['bear', 'rocket', 'kangaroo', 'shark'],
    '<VERB>' : ['jumped', 'walked', 'ran', 'skipped', 'laughed']
}

story_file = "story.txt"
result = ""

def is_punctuated(word):
    last_char = word[-1]
    return (last_char == '.' or last_char == '!' or last_char == '?')


def remove_punctuation(word):
    if (is_punctuated(word)):
        return word[0:len(word) - 1]
    else:
        return word

#open story file and read the lines from it
file = open(story_file)
story = file.readlines()
for line in story:
    words = line.split(' ')
    for word in words:
        word_no_punct = remove_punctuation(word)
            
        if (word_no_punct in word_dict.keys()):
            word_dict_entry = word_dict[word_no_punct]
            random_index = randint(0, len(word_dict_entry) - 1)
            result += " " + word_dict_entry[random_index]
            
            if (is_punctuated(word)):
                result += word[-1]
        else:
            result += " " + word
    result += '\n'
        
print("madlib: " + result)