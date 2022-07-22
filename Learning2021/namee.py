def fullname(first,last,middle=""):
	if middle:
		name = f"{first} {middle} {last}"
	else:
		name = f"{first} {last}"
	return name.title()

def city(country,capital,lang =""):
	if lang:
		name = f"{country}, {capital} and the Language is {lang} "
	else:
		name = f"{country}, {capital}"
	return (name.title())

hi =  city("tamilnadu","chennai","tamil")
print(hi)


#languages survey

from survey import Survey

question = "What is the Language That You First Learn ? "
lang_survy = Survey(question)

lang_survy.ask_question()

print("Enter q to Leave")

while True:
	response   = input("Language :")
	if response== "q" :
		break
	lang_survy.respnse(response)

lang_survy.results()
