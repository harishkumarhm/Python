names=["Harish","Girish","Ram","Ajay","Rahul","Suresh"]

while True:
    print("Dummy Security System..")
    name= input("What is your name?: ").strip().capitalize()
    if name in names:
        print("Hello! {}".format(name))
        remove = input("Do you want to remove the user, y/n?: ").lower()
        if remove == 'y':
            names.remove(name)
            print("Name removed..")
        elif remove == 'n':
            print("Okay. you are not removed!")
            
    else:
        varadd = input("Name does not exist.Would you like to be added to the system, y/n?: ").strip().lower()
        if varadd == 'y':
            names.append(name)
            print("Name added to the system")
        elif varadd == 'n':
            print("Okay..See you later!")
                  
            
        
    
