user= "Akila"
pas="Perumal@2000"
i=3
while i>0:
    username = input("Enter the username: ")
    if user == username:
      password = input("Enter the password: ")
      if password==pas:
        print("Successfully login")
        break
      else:
        i = i-1
        if i == 2:
          print("Invalid password. Only 2 times left")
        else:
            if i == 1:
              print("Invalid password. Only one more time left")
            else:
              print("Invalid password")
              print("Account Blocked")
    else:
      i = i-1
      if i==2:
        print("Invalid username. Only 2 times left")
      else:
          if i==1:
            print ("Invalid username. Only one time left")
          else:
            print("Invalid username")
            print("Account Blocked")
