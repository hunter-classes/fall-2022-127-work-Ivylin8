def hello_name(name):
  """
  Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
  """
  return "Hello " + name + "!"


def make_out_word(out, word):
    
    """
Given an "out" string length 4, such as "<<>>", and a
word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".
    """

    return out[:2] + word + out[2:]

    
def first_two(str):
  """
  Given a string, return the string made of its first two chars, so the 
  String "Hello" yields "He". If the string is shorter than length 2, return 
  whatever there is, so "X" yields "X", and the empty string "" yields the 
  empty string "". 
  """
  return str if len(str)<=2 else str[:2]    