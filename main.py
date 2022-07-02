# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from ast import Return


def find_anagram(word, anagram):
    # Change the word and the anagram to lowercase
    word = word.lower()
    anagram=anagram.lower()
    
    # Remove the white space from the word and the anagram 
    word = word.replace(" ", "")
    anagram=anagram.replace(" ", "")
     
    #  Sort the word and the anagram 
    return sorted(word) == sorted(anagram)

print(find_anagram("silent", "listen"))
print(find_anagram("elvis","lives"))


