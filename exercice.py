# # Given a list [1,2,3,4], print out all the values in the list.
# my_list = [1,2,3,4]
# print(my_list)
# print(" --------------------------\n" )
# # Given a list [1,2,3,4], print out all the values in the list multiplied by 20.
# for i in my_list:
#     print(f"{i} * {20} = {i*20}")

# # Given a list [“Elie”, “Tim”, “Matt”], return a new list with only the first letter ([“E”, “T”, “M”]).
# persons = ["Elie", "Tim", "Matt"]
# new_person = []
# for person in ["Elie", "Tim", "Matt"]:
#    i = person[0]
#    new_person.append(i)
# print(new_person)

# # Given a list [1,2,3,4,5,6] return a new list of all the even values ([2,4,6]).
# numbers = [1,2,3,4,5,6]
# new_numbers = []
# for i in numbers:
#     if i % 2 == 0:
#         new_numbers.append(i)
# print(new_numbers)

# Given two lists [1,2,3,4] and [3,4,5,6], return a new list that is the intersection of the two ([3,4]).
list1 = [1,2,3,4]
list2 = [3,4,5,6]
new_list = []
for val in list1 :
    if val in list2:
        new_list.append(val)
print(new_list)

# Given a list of words [“Elie”, “Tim”, “Matt”] return a new list with each word reversed and in lower case ([‘eile’, ‘mit’, ‘ttam’]).
list_word =  ["Elie", "Tim", "Matt"]  
for word in list_word:
    word_r = ''.join(reversed(word))
    print(word_r.lower())
    
# Given two strings “first” and “third”, return a new string with all the letters present in both words ([“i”, “r”, “t”]).
word1 = "first"
word2 = "third"
new_word_list =[]
for i in word1 :
    if i in word2:
        new_word_list.append(i)
        
print(new_word_list)

# For all the numbers between 1 and 100, return a list with all the numbers that are divisible by 12 ([12, 24, 36, 48, 60, 72, 84, 96]).
divisible = [12, 24, 36, 48, 60, 72, 84, 96]
for i in range(100):
    if i%12 == 0:
        if i == 0:
            continue
        else :
            print(i)
            
# Given the string “amazing”, return a list with all the vowels removed ([‘m’, ‘z’, ‘n’, ‘g’]).
word3 =  "amazing"
vowels = ["a","e","i","o", "h","u"]
for i in word3 :
    if i in vowels :
        print(i)
#         word3.replace(i,"")
# print(word3)


def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [char for char in string if char.lower() not in vowels]
    return consonants

# Example usage
string = "amazing"
result = remove_vowels(string)
print("le resultat est " , result)

# my_list = [[num for num in range(3)] for _ in range(3)]

my_list = [[num for num in range(3)] for _ in range(3)]
print(my_list)

# Generate a list with the value:
'''
[
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
]'''

my_lists = [i for i in range(0,10)] 
for num in range(0,10) :
    print(my_lists)
# Renvoie un dict_keysobjet contenant toutes les clés d'un objet. 
d = dict(a=1,b=2,c=3)
 # dict_keys(['a', 'b', 'c'])
print(d.values())

