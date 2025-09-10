# -- Main --#
print("Hello Reader! what type of manga do you enjoy?")
print("1. Action\n2. Fantasy\n3. Drama")
genre_choice = input("Enter your choice (1/2/3) > ")

# -- Layer 1.1 -- # Action Manga
if genre_choice == "1" :
    print("You have selected -Action- Genre")
    print("\nHow long do you want you Manga be?")
    print("1. Short\n2. Medium\n3. Long")
    length_choice = input("Enter your choice (1/2/3) > ")

    # -- Layer 1.2 -- #
    if length_choice == "3" :
        print("You have selected -Long- length")
        print("\nWhat year do you want your Manga be")
        print("1. 1990-2000\n2. 2001-2015\n3. 2016-2025")
        # -- Layer 1.3 -- #
        year_choice = input("Enter your choice (1/2/3) > ")
        if year_choice == "1" :
            print("You have selected year 1990-2000")
            print("\nthere's 2 manga available in our gallery")
            print("-One Piece\n-Dragon Ball")
        else :
            print("Sorry there's no available Manga in our gallery this year")
    else : # choice 1 and 2
        print ("There's no available length in this Genre")
    
# -- Layer 2.1 -- # Fantasy Manga
elif genre_choice == "2" :
    print("You have selected -Fantasy- Genre")
    print("\nHow long do you want you Manga be?")
    print("1. Short\n2. Medium\n3. Long")
    length_choice = input("Enter your choice (1/2/3) > ")

    # -- Layer 2.2
    if length_choice == "2" :
        print("You have selected -Medium- length")
        print("\nWhat year do you want your Manga be")
        print("1. 1990-2000\n2. 2001-2015\n3. 2016-2025")
        year_choice = input("Enter your choice (1/2/3) > ")
        if year_choice == "3" :
            print("You have selected year 2016-2025")
            print("\nthere's 1 manga available in our gallery")
            print("-Frieren: Beyond Journeys End")
        else :
            print("Sorry there's no available Manga in our gallery this year")
    # -- Layer 2.2.1
    elif length_choice == "3" :
        print("You have selected -Long- length")
        print("\nWhat year do you want your Manga be")
        print("1. 1990-2000\n2. 2001-2015\n3. 2016-2025")
        year_choice = input("Enter your choice (1/2/3) > ")
        if year_choice == "2" :
            print("You have selected year 2001-2015")
            print("\nthere's 2 manga available in our gallery")
            print("-Mushoku Tensei\n-That Time I Got Reincarnated as a Slime")
        else :
            print("Sorry there's no available Manga in our gallery this year")
    else : # choice 1
        print ("There's no available length in this Genre")      

# -- Layer 3.1 -- # Drama Manga
elif genre_choice == "3" :
    print("You have selected -Drama- Genre")
    print("\nHow long do you want you Manga be?")
    print("1. Short\n2. Medium\n3. Long")
    length_choice = input("Enter your choice (1/2/3) > ")

       #-- Layer 3.2
    if length_choice == "1" :
        print("You have selected -Short- length")
        print("\nWhat year do you want your Manga be")
        print("1. 1990-2000\n2. 2001-2015\n3. 2016-2025")
        year_choice = input("Enter your choice (1/2/3) > ")
        if year_choice == "2" :
            print("You have selected year 2001-2015")
            print("\nthere's 1 manga available in our gallery")
            print("-I want to eat your pancreas")
        else :
            print("Sorry there's no available Manga in our gallery this year")
    elif length_choice == "2" :
        print("You have selected -Medium- length")
        print("\nWhat year do you want your Manga be")
        print("1. 1990-2000\n2. 2001-2015\n3. 2016-2025")
        year_choice = input("Enter your choice (1/2/3) > ")
        if year_choice == "2" :
            print("You have selected year 2001-2015")
            print("\nthere's 2 manga available in our gallery")
            print("-Toradora\n-Golden Time")
        elif year_choice == "3" :
            print("You have selected year 2016-2025")
            print("\nthere's 2 manga available in our gallery")
            print("-The Girl I Like Forgot Her Glasses\n-Roshidere")
        else :
            print("Sorry there's no available Manga in our gallery this year")
    else : # choice 3
        print ("There's no available length in this Genre")
else:
    print("You didn't pick something in the choices given..")