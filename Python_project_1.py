#Tarık Emre Gündüz 280201075
import random
print("Welcome to Bunco Game")
print("")
#If I would not assign a value for point bunco and minibunco If I won't have any of them in the end programme return an error
#because I cannot return an undefined value.
roundnum=1
point=0
bunco = 0
minibunco = 0


#Round1
print("Round 1")

#Roll1
dicer1 = random.randint(1,6)
dicer2 = random.randint(1,6)
dicer3 = random.randint(1,6)
print("Roll 1")
input("Press enter to dice")
print(dicer1)
print(dicer2)
print(dicer3)
#bunco
if dicer1 == dicer2 == dicer3 == roundnum:
    point = point+21
    print("Bunco! You get 21 points. Congratulations!")
    bunco=bunco+1

#minibunco
elif dicer1==dicer2==dicer3:
    point = point+5
    print("Well done! It is a minibunco. You get 5 points.")
    minibunco=minibunco+1
#if matches 2 dice with round number
elif roundnum==dicer1 and roundnum==dicer2 or roundnum==dicer2 and roundnum==dicer3 or roundnum==dicer1 and roundnum==dicer3:
    point = point+2
    print("Two dice matches with round number. You get 2 points.")

#if matches 1 dice with round number
elif roundnum==dicer1 or roundnum==dicer2 or roundnum==dicer3:
    point = point+1
    print("You matched at least a dice with round number. You get 1 point.")

else:
    print("You could not get any point this round. Go to next round and try again.")
    roundnum=roundnum+1
print("")

#Roll2
if roundnum==1:
    dicer1 = random.randint(1,6)
    dicer2 = random.randint(1,6)
    dicer3 = random.randint(1,6)
    print("Roll 2")
    input("Press enter to dice")
    print(dicer1)
    print(dicer2)
    print(dicer3)
    #bunco
    if dicer1 == dicer2 == dicer3 == roundnum:
        point = point+21
        print("Bunco! You get 21 points. Congratulations!")
        bunco=bunco+1

    #minibunco
    elif dicer1==dicer2==dicer3:
        point = point+5
        print("Well done! It is a minibunco. You get 5 points.")
        minibunco=minibunco+1
    #if matches 2 dice with round number
    elif roundnum==dicer1 and roundnum==dicer2 or roundnum==dicer2 and roundnum==dicer3 or roundnum==dicer1 and roundnum==dicer3:
        point = point+2
        print("Two dice matches with round number. You get 2 points.")

    #if matches 1 dice with round number
    elif roundnum==dicer1 or roundnum==dicer2 or roundnum==dicer3:
        point = point+1
        print("You matched at least a dice with round number. You get 1 point.")

    else:
        print("You could not get any point this round. Go to next tour and try again.")
        roundnum=roundnum+1
    print("")

#Roll3
if roundnum==1:
    dicer1 = random.randint(1,6)
    dicer2 = random.randint(1,6)
    dicer3 = random.randint(1,6)
    print("Roll 3")
    input("Press enter to dice")
    print(dicer1)
    print(dicer2)
    print(dicer3)
    #bunco
    if dicer1 == dicer2 == dicer3 == roundnum:
        point = point+21
        print("Bunco! You get 21 points. Congratulations!")
        bunco=bunco+1

    #minibunco
    elif dicer1==dicer2==dicer3:
        point = point+5
        print("Well done! It is a minibunco. You get 5 points.")
        minibunco=minibunco+1
    #if matches 2 dice with round number
    elif roundnum==dicer1 and roundnum==dicer2 or roundnum==dicer2 and roundnum==dicer3 or roundnum==dicer1 and roundnum==dicer3:
        point = point+2
        print("Two dice matches with round number. You get 2 points.")

    #if matches 1 dice with round number
    elif roundnum==dicer1 or roundnum==dicer2 or roundnum==dicer3:
        point = point+1
        print("You matched at least a dice with round number. You get 1 point.")

    else:
        print("You could not get any point this round. Go to next tour and try again.")
    roundnum=roundnum+1
    
print("Your total point is", point)
print()
print()


#Round2
print("Round 2")
#Roll1
dicer1 = random.randint(1,6)
dicer2 = random.randint(1,6)
dicer3 = random.randint(1,6)
print("Roll 1")
input("Press enter to dice")
print(dicer1)
print(dicer2)
print(dicer3)
#bunco
if dicer1 == dicer2 == dicer3 == roundnum:
    point = point+21
    print("Bunco! You get 21 points. Congratulations!")
    bunco=bunco+1

#minibunco
elif dicer1==dicer2==dicer3:
    point = point+5
    print("Well done! It is a minibunco. You get 5 points.")
    minibunco=minibunco+1
#if matches 2 dice with round number
elif roundnum==dicer1 and roundnum==dicer2 or roundnum==dicer2 and roundnum==dicer3 or roundnum==dicer1 and roundnum==dicer3:
    point = point+2
    print("Two dice matches with round number. You get 2 points.")

#if matches 1 dice with round number
elif roundnum==dicer1 or roundnum==dicer2 or roundnum==dicer3:
    point = point+1
    print("You matched at least a dice with round number. You get 1 point.")

else:
    print("You could not get any point this round. Go to next round and try again.")
    roundnum=roundnum+1
print("")

#Roll2
if roundnum==2:
    dicer1 = random.randint(1,6)
    dicer2 = random.randint(1,6)
    dicer3 = random.randint(1,6)
    print("Roll 2")
    input("Press enter to dice")
    print(dicer1)
    print(dicer2)
    print(dicer3)
    #bunco
    if dicer1 == dicer2 == dicer3 == roundnum:
        point = point+21
        print("Bunco! You get 21 points. Congratulations!")
        bunco=bunco+1

    #minibunco
    elif dicer1==dicer2==dicer3:
        point = point+5
        print("Well done! It is a minibunco. You get 5 points.")
        minibunco=minibunco+1
    #if matches 2 dice with round number
    elif roundnum==dicer1 and roundnum==dicer2 or roundnum==dicer2 and roundnum==dicer3 or roundnum==dicer1 and roundnum==dicer3:
        point = point+2
        print("Two dice matches with round number. You get 2 points.")

    #if matches 1 dice with round number
    elif roundnum==dicer1 or roundnum==dicer2 or roundnum==dicer3:
        point = point+1
        print("You matched at least a dice with round number. You get 1 point.")

    else:
        print("You could not get any point this round. Go to next tour and try again.")
        roundnum=roundnum+1
    print("")

#Roll3
if roundnum==2:
    dicer1 = random.randint(1,6)
    dicer2 = random.randint(1,6)
    dicer3 = random.randint(1,6)
    print("Roll 3")
    input("Press enter to dice")
    print(dicer1)
    print(dicer2)
    print(dicer3)
    #bunco
    if dicer1 == dicer2 == dicer3 == roundnum:
        point = point+21
        print("Bunco! You get 21 points. Congratulations!")
        bunco=bunco+1

    #minibunco
    elif dicer1==dicer2==dicer3:
        point = point+5
        print("Well done! It is a minibunco. You get 5 points.")
        minibunco=minibunco+1
    #if matches 2 dice with round number
    elif roundnum==dicer1 and roundnum==dicer2 or roundnum==dicer2 and roundnum==dicer3 or roundnum==dicer1 and roundnum==dicer3:
        point = point+2
        print("Two dice matches with round number. You get 2 points.")

    #if matches 1 dice with round number
    elif roundnum==dicer1 or roundnum==dicer2 or roundnum==dicer3:
        point = point+1
        print("You matched at least a dice with round number. You get 1 point.")

    else:
        print("You could not get any point this round. Go to next tour and try again.")
    roundnum=roundnum+1
    
print("Your total point is", point)
print()
print()


#Round3
print("Round 3")
#roll1
dicer1 = random.randint(1,6)
dicer2 = random.randint(1,6)
dicer3 = random.randint(1,6)
print("Roll 1")
input("Press enter to dice")
print(dicer1)
print(dicer2)
print(dicer3)
#bunco
if dicer1 == dicer2 == dicer3 == roundnum:
    point = point+21
    print("Bunco! You get 21 points. Congratulations!")
    bunco=bunco+1

#minibunco
elif dicer1==dicer2==dicer3:
    point = point+5
    print("Well done! It is a minibunco. You get 5 points.")
    minibunco=minibunco+1
#if matches 2 dice with round number
elif roundnum==dicer1 and roundnum==dicer2 or roundnum==dicer2 and roundnum==dicer3 or roundnum==dicer1 and roundnum==dicer3:
    point = point+2
    print("Two dice matches with round number. You get 2 points.")

#if matches 1 dice with round number
elif roundnum==dicer1 or roundnum==dicer2 or roundnum==dicer3:
    point = point+1
    print("You matched at least a dice with round number. You get 1 point.")

else:
    print("You could not get any point this round. Go to next round and try again.")
    roundnum=roundnum+1
print("")

#roll2
if roundnum==3:
    dicer1 = random.randint(1,6)
    dicer2 = random.randint(1,6)
    dicer3 = random.randint(1,6)
    print("Roll 2")
    input("Press enter to dice")
    print(dicer1)
    print(dicer2)
    print(dicer3)
    #bunco
    if dicer1 == dicer2 == dicer3 == roundnum:
        point = point+21
        print("Bunco! You get 21 points. Congratulations!")
        bunco=bunco+1

    #minibunco
    elif dicer1==dicer2==dicer3:
        point = point+5
        print("Well done! It is a minibunco. You get 5 points.")
        minibunco=minibunco+1
    #if matches 2 dice with round number
    elif roundnum==dicer1 and roundnum==dicer2 or roundnum==dicer2 and roundnum==dicer3 or roundnum==dicer1 and roundnum==dicer3:
        point = point+2
        print("Two dice matches with round number. You get 2 points.")

    #if matches 1 dice with round number
    elif roundnum==dicer1 or roundnum==dicer2 or roundnum==dicer3:
        point = point+1
        print("You matched at least a dice with round number. You get 1 point.")

    else:
        print("You could not get any point this round. Go to next tour and try again.")
        roundnum=roundnum+1
    print("")

#roll3
if roundnum==3:
    dicer1 = random.randint(1,6)
    dicer2 = random.randint(1,6)
    dicer3 = random.randint(1,6)
    print("Roll 3")
    input("Press enter to dice")
    print(dicer1)
    print(dicer2)
    print(dicer3)
    #bunco
    if dicer1 == dicer2 == dicer3 == roundnum:
        point = point+21
        print("Bunco! You get 21 points. Congratulations!")
        bunco=bunco+1

    #minibunco
    elif dicer1==dicer2==dicer3:
        point = point+5
        print("Well done! It is a minibunco. You get 5 points.")
        minibunco=minibunco+1
    #if matches 2 dice with round number
    elif roundnum==dicer1 and roundnum==dicer2 or roundnum==dicer2 and roundnum==dicer3 or roundnum==dicer1 and roundnum==dicer3:
        point = point+2
        print("Two dice matches with round number. You get 2 points.")

    #if matches 1 dice with round number
    elif roundnum==dicer1 or roundnum==dicer2 or roundnum==dicer3:
        point = point+1
        print("You matched at least a dice with round number. You get 1 point.")

    else:
        print("You could not get any point this round. Go to next tour and try again.")
    roundnum=roundnum+1
    
print("Your total point is", point)
print()
print()


#Round4
print("Round 4")
#roll1
dicer1 = random.randint(1,6)
dicer2 = random.randint(1,6)
dicer3 = random.randint(1,6)
print("Roll 1")
input("Press enter to dice")
print(dicer1)
print(dicer2)
print(dicer3)
#bunco
if dicer1 == dicer2 == dicer3 == roundnum:
    point = point+21
    print("Bunco! You get 21 points. Congratulations!")
    bunco=bunco+1

#minibunco
elif dicer1==dicer2==dicer3:
    point = point+5
    print("Well done! It is a minibunco. You get 5 points.")
    minibunco=minibunco+1
#if matches 2 dice with round number
elif roundnum==dicer1 and roundnum==dicer2 or roundnum==dicer2 and roundnum==dicer3 or roundnum==dicer1 and roundnum==dicer3:
    point = point+2
    print("Two dice matches with round number. You get 2 points.")

#if matches 1 dice with round number
elif roundnum==dicer1 or roundnum==dicer2 or roundnum==dicer3:
    point = point+1
    print("You matched at least a dice with round number. You get 1 point.")

else:
    print("You could not get any point this round. Go to next round and try again.")
    roundnum=roundnum+1
print("")

#roll2
if roundnum==4:
    dicer1 = random.randint(1,6)
    dicer2 = random.randint(1,6)
    dicer3 = random.randint(1,6)
    print("Roll 2")
    input("Press enter to dice")
    print(dicer1)
    print(dicer2)
    print(dicer3)
    #bunco
    if dicer1 == dicer2 == dicer3 == roundnum:
        point = point+21
        print("Bunco! You get 21 points. Congratulations!")
        bunco=bunco+1

    #minibunco
    elif dicer1==dicer2==dicer3:
        point = point+5
        print("Well done! It is a minibunco. You get 5 points.")
        minibunco=minibunco+1
    #if matches 2 dice with round number
    elif roundnum==dicer1 and roundnum==dicer2 or roundnum==dicer2 and roundnum==dicer3 or roundnum==dicer1 and roundnum==dicer3:
        point = point+2
        print("Two dice matches with round number. You get 2 points.")

    #if matches 1 dice with round number
    elif roundnum==dicer1 or roundnum==dicer2 or roundnum==dicer3:
        point = point+1
        print("You matched at least a dice with round number. You get 1 point.")

    else:
        print("You could not get any point this round. Go to next tour and try again.")
        roundnum=roundnum+1
    print("")

#roll3
if roundnum==4:
    dicer1 = random.randint(1,6)
    dicer2 = random.randint(1,6)
    dicer3 = random.randint(1,6)
    print("Roll 3")
    input("Press enter to dice")
    print(dicer1)
    print(dicer2)
    print(dicer3)
    #bunco
    if dicer1 == dicer2 == dicer3 == roundnum:
        point = point+21
        print("Bunco! You get 21 points. Congratulations!")
        bunco=bunco+1

    #minibunco
    elif dicer1==dicer2==dicer3:
        point = point+5
        print("Well done! It is a minibunco. You get 5 points.")
        minibunco=minibunco+1
    #if matches 2 dice with round number
    elif roundnum==dicer1 and roundnum==dicer2 or roundnum==dicer2 and roundnum==dicer3 or roundnum==dicer1 and roundnum==dicer3:
        point = point+2
        print("Two dice matches with round number. You get 2 points.")

    #if matches 1 dice with round number
    elif roundnum==dicer1 or roundnum==dicer2 or roundnum==dicer3:
        point = point+1
        print("You matched at least a dice with round number. You get 1 point.")

    else:
        print("You could not get any point this round. Go to next tour and try again.")
    roundnum=roundnum+1
    
print("Your total point is", point)
print()
print()


#Round5
print("Round 5")
#roll1
dicer1 = random.randint(1,6)
dicer2 = random.randint(1,6)
dicer3 = random.randint(1,6)
print("Roll 1")
input("Press enter to dice")
print(dicer1)
print(dicer2)
print(dicer3)
#bunco
if dicer1 == dicer2 == dicer3 == roundnum:
    point = point+21
    print("Bunco! You get 21 points. Congratulations!")
    bunco=bunco+1

#minibunco
elif dicer1==dicer2==dicer3:
    point = point+5
    print("Well done! It is a minibunco. You get 5 points.")
    minibunco=minibunco+1
#if matches 2 dice with round number
elif roundnum==dicer1 and roundnum==dicer2 or roundnum==dicer2 and roundnum==dicer3 or roundnum==dicer1 and roundnum==dicer3:
    point = point+2
    print("Two dice matches with round number. You get 2 points.")

#if matches 1 dice with round number
elif roundnum==dicer1 or roundnum==dicer2 or roundnum==dicer3:
    point = point+1
    print("You matched at least a dice with round number. You get 1 point.")

else:
    print("You could not get any point this round. Go to next round and try again.")
    roundnum=roundnum+1
print("")

#roll2
if roundnum==5:
    dicer1 = random.randint(1,6)
    dicer2 = random.randint(1,6)
    dicer3 = random.randint(1,6)
    print("Roll 2")
    input("Press enter to dice")
    print(dicer1)
    print(dicer2)
    print(dicer3)
    #bunco
    if dicer1 == dicer2 == dicer3 == roundnum:
        point = point+21
        print("Bunco! You get 21 points. Congratulations!")
        bunco=bunco+1

    #minibunco
    elif dicer1==dicer2==dicer3:
        point = point+5
        print("Well done! It is a minibunco. You get 5 points.")
        minibunco=minibunco+1
    #if matches 2 dice with round number
    elif roundnum==dicer1 and roundnum==dicer2 or roundnum==dicer2 and roundnum==dicer3 or roundnum==dicer1 and roundnum==dicer3:
        point = point+2
        print("Two dice matches with round number. You get 2 points.")

    #if matches 1 dice with round number
    elif roundnum==dicer1 or roundnum==dicer2 or roundnum==dicer3:
        point = point+1
        print("You matched at least a dice with round number. You get 1 point.")

    else:
        print("You could not get any point this round. Go to next tour and try again.")
        roundnum=roundnum+1
    print("")

#roll3
if roundnum==5:
    dicer1 = random.randint(1,6)
    dicer2 = random.randint(1,6)
    dicer3 = random.randint(1,6)
    print("Roll 3")
    input("Press enter to dice")
    print(dicer1)
    print(dicer2)
    print(dicer3)
    #bunco
    if dicer1 == dicer2 == dicer3 == roundnum:
        point = point+21
        print("Bunco! You get 21 points. Congratulations!")
        bunco=bunco+1

    #minibunco
    elif dicer1==dicer2==dicer3:
        point = point+5
        print("Well done! It is a minibunco. You get 5 points.")
        minibunco=minibunco+1
    #if matches 2 dice with round number
    elif roundnum==dicer1 and roundnum==dicer2 or roundnum==dicer2 and roundnum==dicer3 or roundnum==dicer1 and roundnum==dicer3:
        point = point+2
        print("Two dice matches with round number. You get 2 points.")

    #if matches 1 dice with round number
    elif roundnum==dicer1 or roundnum==dicer2 or roundnum==dicer3:
        point = point+1
        print("You matched at least a dice with round number. You get 1 point.")

    else:
        print("You could not get any point this round. Go to next tour and try again.")
    roundnum=roundnum+1
    
print("Your total point is", point)
print()
print()

#Round6
print("Round 6")
#roll1
dicer1 = random.randint(1,6)
dicer2 = random.randint(1,6)
dicer3 = random.randint(1,6)
print("Roll 1")
input("Press enter to dice")
print(dicer1)
print(dicer2)
print(dicer3)
#bunco
if dicer1 == dicer2 == dicer3 == roundnum:
    point = point+21
    print("Bunco! You get 21 points. Congratulations!")
    bunco=bunco+1

#minibunco
elif dicer1==dicer2==dicer3:
    point = point+5
    print("Well done! It is a minibunco. You get 5 points.")
    minibunco=minibunco+1
#if matches 2 dice with round number
elif roundnum==dicer1 and roundnum==dicer2 or roundnum==dicer2 and roundnum==dicer3 or roundnum==dicer1 and roundnum==dicer3:
    point = point+2
    print("Two dice matches with round number. You get 2 points.")

#if matches 1 dice with round number
elif roundnum==dicer1 or roundnum==dicer2 or roundnum==dicer3:
    point = point+1
    print("You matched at least a dice with round number. You get 1 point.")

else:
    print("You could not get any point this round. Go to next round and try again.")
    roundnum=roundnum+1
print("")

#roll2
if roundnum==6:
    dicer1 = random.randint(1,6)
    dicer2 = random.randint(1,6)
    dicer3 = random.randint(1,6)
    print("Roll 2")
    input("Press enter to dice")
    print(dicer1)
    print(dicer2)
    print(dicer3)
    #bunco
    if dicer1 == dicer2 == dicer3 == roundnum:
        point = point+21
        print("Bunco! You get 21 points. Congratulations!")
        bunco=bunco+1

    #minibunco
    elif dicer1==dicer2==dicer3:
        point = point+5
        print("Well done! It is a minibunco. You get 5 points.")
        minibunco=minibunco+1
    #if matches 2 dice with round number
    elif roundnum==dicer1 and roundnum==dicer2 or roundnum==dicer2 and roundnum==dicer3 or roundnum==dicer1 and roundnum==dicer3:
        point = point+2
        print("Two dice matches with round number. You get 2 points.")

    #if matches 1 dice with round number
    elif roundnum==dicer1 or roundnum==dicer2 or roundnum==dicer3:
        point = point+1
        print("You matched at least a dice with round number. You get 1 point.")

    else:
        print("You could not get any point this round. Go to next tour and try again.")
        roundnum=roundnum+1
    print("")

#roll3
if roundnum==6:
    dicer1 = random.randint(1,6)
    dicer2 = random.randint(1,6)
    dicer3 = random.randint(1,6)
    print("Roll 3")
    input("Press enter to dice")
    print(dicer1)
    print(dicer2)
    print(dicer3)
    #bunco
    if dicer1 == dicer2 == dicer3 == roundnum:
        point = point+21
        print("Bunco! You get 21 points. Congratulations!")
        bunco=bunco+1

    #minibunco
    elif dicer1==dicer2==dicer3:
        point = point+5
        print("Well done! It is a minibunco. You get 5 points.")
        minibunco=minibunco+1
    #if matches 2 dice with round number
    elif roundnum==dicer1 and roundnum==dicer2 or roundnum==dicer2 and roundnum==dicer3 or roundnum==dicer1 and roundnum==dicer3:
        point = point+2
        print("Two dice matches with round number. You get 2 points.")

    #if matches 1 dice with round number
    elif roundnum==dicer1 or roundnum==dicer2 or roundnum==dicer3:
        point = point+1
        print("You matched at least a dice with round number. You get 1 point.")

    else:
        print("You could not get any point this round. Go to next tour and try again.")
    roundnum=roundnum+1

#This code will return us how much point, bunco and minibunco we have at the end.
input("Game is completed press enter to see results.")
print()
print()
print()
print()
print()
print("Your point is", str(point)+". Congratulations!")
print("You have", str(bunco),"bunco.")
print("You have", str(minibunco),"minibunco.")
print()
print()
print()
print()
