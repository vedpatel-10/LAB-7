dict1 = {}
dict2 = {"Sahil":"Rajasthan","Deep":"RCB","Pinak":"CSK"}
dict3 ={"RCB": 0,"CSK":5,"MI":5,"GT":1}
dict4 = {**dict1,**dict2,**dict3}
print(dict4)

#OUTPUT:
# {'Sahil': 'Rajasthan', 'Deep': 'RCB', 'Pinak': 'CSK', 'RCB': 0, 'CSK': 5, 'MI': 5, 'GT': 1} 
