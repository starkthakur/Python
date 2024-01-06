import ModulesLect21
import random
import Lec17_Function

classmates = {'Tony': 'cool but smells', 'Emma': 'backbencher', 'Ashish': 'Most Intelligent person on earth'}
print(classmates)
print(classmates['Ashish'])

'''
for key, value in classmates.items():
 # print(key, value)  // we can choose any line 6 or 7 Key and Value can also be reffered as K and V
 print(key+ value)
 
 '''

for Name, Character in classmates.items():
    # print(key, value)  // we can choose any line 6 or 7 Key and Value can also be referred as K and V or comma or +

    print(Name, Character)

y = Lec17_Function.add_numbers(18, 32)
print(y)

ModulesLect21.module()

x = random.randrange(1, 1000)
print(x)
