import operator

dict_dep = {"rakesh":1 ,"ashish":3,"sahil":2, "tirth":3,"hardik":1,"swayam":2,"om":1}
dict_roll = {"rakesh":32,"ashish":53,"sahil":56,"tirth":3,"hardik":12,"swayam":29,"om":76}
dict_salary = {"rakesh":15000,"ashish":23000,"sahil":25000,"tirth":30000,"hardik":18000,"swayam":22000,"om":18500}

d1 = sorted(dict_dep.items(), key = operator.itemgetter(1))
d2 = sorted(dict_roll.items(), key = operator.itemgetter(1))
d3 = sorted(dict_salary.items(), key = operator.itemgetter(1))

print(d1)
print(d2)
print(d3)

lst_d1,lst_d1_salary = [],[]
lst_d2,lst_d2_salary=  [],[]
lst_d3,lst_d3_salary = [],[]

for k,v in dict_dep.items():
    if v == 1:
        lst_d1.append(k)
    elif v == 2:
        lst_d2.append(k)
    elif v == 3:
        lst_d3.append(k)        

for i in lst_d1:
    lst_d1_salary.append(dict_salary[i])

for i in lst_d2:
    lst_d2_salary.append(dict_salary[i])

for i in lst_d3:
    lst_d3_salary.append(dict_salary[i])

print("Maximum salary of department 1 is :" , max(lst_d1_salary))
print("Minimum salary of department 1 is :", min(lst_d1_salary))

print("Maximum salary of department 2 is :" , max(lst_d2_salary))
print("Minimum salary of department 2 is :", min(lst_d2_salary))

print("Maximum salary of department 3 is :" , max(lst_d3_salary))
print("Minimum salary of department 3 is :", min(lst_d3_salary))

