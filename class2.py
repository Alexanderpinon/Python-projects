class User:
     name = "Mark"
     email = "mark@gmail.com"
     password = "1234abcd"



     def getLoginInfo(self):
         entry_name = input("Enter your name here")
         entry_email = input("Enter your email: ")
         entry_password = input("Enter your password: ")
         if (entry_email == self.email and entry_password == self.password):
             print("Welcome back, {}".format(self.name))
         else:
             print("You are not authorized for this page.")


class Empolyee(User):
    base_pay = 11.00
    department = 'General'
    pin_number = "3920"



     def getLoginInfo(self):
         entry_email = input("Enter your email: ")
         entry_name = input("Enter your name: ")
         entry_pin = input("Enter your pin: ")
         if (entry_email == self.email and entry_pin == self.pin_number):
             print("Welcome back, {}".format(self.name))
         else:
             print("The pin or email is incorrect")

class Customer(User):
    mailing_address = ' '
    mailing_list = True


     def getLoginInfo(self):
         mailing_address = input("Enter your mailing address: ")
         mailing_list = input("Enter your mailing list: ")
         if (mailing_address == self.mailing_address and mailing_list == self.mailing_list):
             print("your address is{}".format(self.address))
         else:
             print("The mailing address is wrong")
    


    customer = User()
    customer.getLoginInfo()

    manager = Employee()
    manager.getLoginInfo()


