class Parent():
    def __init__(self, last_name,eye_color):
        print("parent Constructor is called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last_name - "+self.last_name)
        print("eye_color - "+self.eye_color)




        
class Child(Parent):
    def  __init__(self,last_name,eye_color,number_of_toys):
        print("Child Constructor is called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last_name - "+self.last_name)
        print("eye_color - "+self.eye_color)
        print("eye_color - "+str(self.number_of_toys))



#billy_cyrus = Parent("Cyrus"  , "BLUE")
#billy_cyrus.show_info()
miley_cyrus = Child("Cyrus","Blue",5)
miley_cyrus.show_info()
#print(miley_cyrus.number_of_toys)
#print(miley_cyrus.last_name)

#always child class constructor is called rather that parent class
