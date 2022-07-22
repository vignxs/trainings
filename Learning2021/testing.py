import unittest
# from func import fullname
# # print(fullname("vignesh","sivakumar"))

# while True:
#     print("Enter Your First and Last Name OR Press Q to Quit ")
    
#     first = input("Enter Your First Name : ")
#     if first == "q" :
#         break
    
#     last = input("Enter Your Last Name : ")
#     if last == "q":
#         break

#     name = fullname(first,last)
#     print(name)

# import unittest
# from namee import fullname

# class NameTest(unittest.TestCase):
    
#     def test_fullname(self):
#         formated_name = fullname("vignesh","sivakumar")
#         self.assertEqual(formated_name,"Vignesh Sivakumar")

#     def test_middle(self):
#         formated_name = fullname("dhivya","hii","udayakumar")
#         self.assertEqual(formated_name, "Dhivya Udayakumar Hii")

# if __name__ == "__main__":
#     unittest.main()

# import unittest
# from namee import city

# class TestCity(unittest.TestCase):

#     def test_name(self):
#         name1 = city("tamilnadu","chennai")
#         self.assertEqual(name1,"Tamilnadu, Chennai")

#     def test_name2(self):
#         name2 = city("united kingdom","london","british english")
#         self.assertEqual(name2,"United Kingdom, London And The Language Is British English ")

# if __name__ =="__main__":
#     unittest.main()


# import unittest
# from survey import Survey

# class TestSurvy(unittest.TestCase):

#     def test_sur(self):

#         question = "What IS The First Language That You Learned"
#         mysur = Survey(question)
#         mysur.respnse("English")
        
#         self.assertIn("English", mysur.response)

#     def test_survey(self):
#         question = "What IS The First Language That You Learned"
#         mysur = Survey(question)
#         responses =  ["English","Tamil","mandarin"]
#         for response in responses:
#             mysur.respnse(response)
#         for response in responses:
#             self.assertIn(response, mysur.response)

# if __name__ == "__main__":
#     unittest.main()

# """testing with Setup()"""

# import unittest
# from survey import Survey

# class TestSur(unittest.TestCase):

#     def setUp(self) :
#         question = "What IS The First Language That You Learned"
#         self.mysur = Survey(question)
#         self.responses = ["English","Tamil","Mandarin"] 
    
#     def test_survy(self):
#         self.mysur.respnse(self.responses[0])
#         self.assertIn("English",  self.mysur.response)

#     def test_survey(self):
#         for response in self.responses:
#             self.mysur.respnse(response)
        
#         for response in self.responses:
#             self.assertIn(response, self.mysur.response)

# if __name__ == "__main__" :
#     unittest.main()


#"""Tesiting for raise salary coding the salary amount by default it will add 5000 or 
#it will add any number we want """
 
from survey import RaiSalary

class TestRaise(unittest.TestCase):
     
    def setUp(self):
        self.vignesh = RaiSalary("vignesh","sivakumar",20000)       

    def test_defualt(self):
        self.vignesh.give_raise()
        self.assertEqual(self.vignesh.salary ,25000)

    def test_input(self):
        self.vignesh.give_raise(4000)
        self.assertEqual(self.vignesh.salary, 24000)

if __name__ == "__main__":
    unittest.main()