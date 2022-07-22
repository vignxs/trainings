# test = {1:'A',2:'B',3:'C',4:"D",5:'E'}
# dict = {}

# for k,v in test.items():
#     dict[v] = k

# print(dict)


""" Counting Strings """
# from collections import Counter
# word = 'hello there how are you' #input("Enter a Word")
# res = Counter(word)
# print(res)

# text = "hello there how are you"
# dict = {}
# for i in text:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1
# print(dict)


""" common items in two lists """

# a = [1,2,3,4,5,6]
# b = [3,4,6,8,7,9]
# print(set(a))
# print(set(b))

# if set(a) and set(b):
#     print(set(a) )
#     print(set(b) )

# else:
#     print("no common values") 

# a = [1,2,3,4,5,6]
# b = [3,4,6,8,7,9]
# c= []
# for value in a :
#     if value in b:
#         c.append(value)
# print(c)

""" Reading Json  """
import json

f = open('user.json',)
data = json.load(f)
for i in data['emp_details']:
    print(i)
f.close()
