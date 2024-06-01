class User:
    
    def __init__(self,first_name,last_name,username,password) :
        self.first_name=first_name
        self.last_name=last_name
        self.username=username
        self.password=password

    def __str__(self) :
        print("#"*50)
        return f"""
first_name --> {self.first_name}
last_name --> {self.last_name}
user name --> {self.username} 
        """
        
list_0f_user=[]
class UserManeger:
    def register(self,first_name,last_name,username,password):
        new_user=User(first_name,last_name,username,password)
        list_0f_user.append(new_user)
        print("New user registied succesfuly")
    def login(self,user,password):
        for i in list_0f_user:
            if i.username==user and i.password==password:
                print ("Login successful! ")
            else:
                print("User not found ")
    def change_password(self,username,old_pass,new_pass):
        for i in list_0f_user:
            if i.username==username and i.password==old_pass:
                i.password=new_pass
                print("password succesfuly changed")
                break
        else:
                print("wrong password or username")
    def get_users(self):
        for i in list_0f_user:
            print (i) 
          


ob1=UserManeger
while True:
    print(f"""
    1.Rgisteration
    2.Lgin
    3.Change password
    4.Get users
    0.exit
      """)
    choise=input("Enter your choise -->  ")
    match choise:
        case "1":
            ob1.register(ob1,input("Enter first name -->"),input("Enter your last name --> "),input("Enter your username --> "),input("enter your pass -->"))
        case "2":
            ob1.login(ob1,input("enter username ->"),input("enter your password ->"))
        case "3":
            ob1.change_password(ob1,input("Enter your username -->"),input("Enter your old password -->"),input("Enter your new password -->"))
        case "4":
            ob1.get_users(ob1)
        case "0":
            break
        case _:
            print("wrong !")