class Survey:

    def __init__ (self,question):
        self.question = question
        self.response = []
    
    def ask_question(self):
        print(self.question)

    def respnse(self,new_responce):
        self.response.append(new_responce)
    
    def results(self):
        #print("Survey Results :")
        for ans in self.response:
            #print(f"-  {ans}")
            print(ans)


class RaiSalary:

    def __init__(self,first_name,last_name , salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        

    def give_raise(self,raisee =5000):
        self.salary += raisee
        
       
        # if raisee :
        #     self.salary += raisee
        #     output = (f"{self.first_name} {self.last_name} your raise is {self.salary}")
        #     self.ans = output.title()
        # else:
        #     self.salary += 5000
        #     output = (f"{self.first_name} {self.last_name} your raise is {self.salary}")
        #     self.ans = output.title()
