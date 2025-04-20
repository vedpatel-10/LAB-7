string = input("Enter a string : ")
character = []
frequency = []

for i in range(65,91):
    if (chr(i) in  string):
        character.append(chr(i))

for i in range(97,123):
    if (chr(i) in string):
        character.append(chr(i))

for i in character:
    frequency.append(string.count(i))

new_dict_freq = {}
for i in range(len(character)):
    dict_freq = {character[i]:frequency[i]}   
    new_dict_freq.update(dict_freq)

print(new_dict_freq)

#OUTPUT:
# Enter a string : HELLO READERS !
# {'A': 1, 'D': 1, 'E': 3, 'H': 1, 'L': 2, 'O': 1, 'R': 2, 'S': 1} 
