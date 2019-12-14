films = {
    "Finding Dory":[3,5],
    "Borne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
    }

while True:
    choice = input("What film would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("Enter your age: ").strip())
        if age >= films[choice][0]:
            if films[choice][1] > 0:
                print("Enjoy the film....")
                films[choice][1] = films[choice][1]-1
            else:
                print("Sorry, No seats available for this show..")

        else:
            print("You are too young to watch this film..")
    else:
        print("We don't have that film...")
        
    
