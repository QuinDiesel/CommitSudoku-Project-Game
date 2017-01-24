import pygame

def question():
    #dit zoekt waar de speler zich bevind
    player_position = int(input("What catagorie are you in?: 0=Red, 1=Yellow, 2=Blue, 3=Green \n Select the number of catagorie? "))
    catagorie = 0

    #score per catagorie zodat je geen zelfde vragen krijgt
    red_score = 0
    yellow_score = 0
    blue_score = 0
    green_score = 0

    #catagorie indeling
    if player_position == 0:
        print("Catagorie Red: Entertainment")
        catagorie += 0

    elif player_position == 1:
        print("Catagorie Yellow: History")
        catagorie += 1

    elif player_position == 2:
        print("Catagorie Blue: Sport")
        catagorie += 2

    elif player_position == 3:
        print("Catagorie Green: Geography")
        catagorie += 3

    if player_position == 0 and red_score == 0:
        print("Question R1: Which artwork is called the Dutch version of the Sistine Chapel? \n 1. Chapelprison \n 2. De Markthal \n 3. Ark the Rotterdam")
        answer = int(input(""))
        if answer == 2:
            print("That is correct")
            red_score = red_score + 1
        else:
            print("That is wrong")

    if player_position == 0 and red_score == 1:
        print("Question R2: What is the name of the cultural and culinary exploration of Rotterdam? \n 1. Drive & Eat \n 2. Bicycle Diner \n 3. Bike & Bite")

    if player_position == 1 and yellow_score == 0:
        print("Question Y1: What does the abbreviation of the NRC newspaper stands for? \n 1. Nieuw Rotterdam Chronicle \n 2. Nieuwe Rotterdamsche Courant \n 3. Nieuwe Rotterdamse Coöperatie")
        answer = int(input(""))
        if answer == 2:
            print("That is correct")
            yellow_score = yellow_score + 1
        else:
            print("That is wrong")

    if player_position == 1 and yellow_score == 1:
        print("Question Y2: During the Second World War, what was the only road for the Germans to reach the center? \n 1. De nieuwe Binnenweg \n 2. Maasbrug \n 3. Koninginnenbrug")
        answer = int(input(""))
        if answer == 2:
            print("That is correct")
            yellow_score = yellow_score - 1
        else:
            print("That is wrong")

    if player_position == 2 and blue_score == 0:
        print("Question B1: What is the name of the sportcentre next to De Kuip? \n 1. Fit for Free Rotterdam \n 2. Basic Fit Rotterdam \n 3. Topsportcentrum Rotterdam")
        answer = int(input(""))
        if answer == 3:
            print("That is correct")
            blue_score = blue_score + 1
        else:
            print("That is wrong")

    if player_position == 2 and blue_score == 1:
        print("Question B2: What kind of sport is most practiced in Rotterdam? \n 1. Fitness \n 2. Football \n 3. Basketball")
        answer = int(input(""))
        if answer == 1:
            print("That is correct")
            blue_score = blue_score - 1
        else:
            print("That is wrong")

    if player_position == 3 and green_score == 0:
        print("Question G1: What is the name of the most famous houses in Rotterdam? \n 1. The kubuswoningen \n 2. The havenhuizen \n 3. The bijenkorf ")
        answer = int(input(""))
        if answer == 1:
            print("That is correct")
            green_score = green_score + 1
        else:
            print("That is wrong")

    if player_position == 3 and green_score == 1:
        print("Question G2: What is the oldest bridge in Rotterdam? \n 1. The Willemsbrug\n 2. The Koninginnebrug\n 3. The van Briennenoordbrug")
        answer = int(input(""))
        if answer == 2:
            print("That is correct")
            green_score = green_score - 1
        else:
            print("That is wrong")
question()

