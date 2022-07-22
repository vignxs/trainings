frnd= ["jims","china","yasith","askar"]
print(f"my friend {frnd[-1].title()} play pubg with me")
print(frnd[-2])
bike= ["R15","RS200","Ninja","Duke","KTM"]
print(f"i would like to own a {bike[-4]}")
frnd.append("sadik")
print(frnd)
frnd.remove('china')
print(frnd)
frnd.pop(0)
print(frnd)
del frnd[-1]
print(frnd)
frnd.insert(0,"jims")
print(frnd)
frnd.sort()
print(frnd)
frnd.sort(reverse=True)
print(frnd)

cars=["BMW","lambo","audi"]
x = sorted(cars)
print(x)