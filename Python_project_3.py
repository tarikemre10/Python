print("Welcome to full adder")
#I use a while for when my calculation has done but I do not select 2 my code should repeat
select=1
while select!=2:
    #Until I select Quit my loop will execute
    print("(1) Compute and Display the Outputs")
    print("(2) Quit")

    select = int(input("You choose: "))
    #I assign empty values to sum and c_out because if they do not have a variable in the end my code will return error.
    SUM=""
    C_OUT=""
    #I assign a lenght variable and create a code for length like a function for checking the digit of my input.
    lenght=0
    #I assigned this because if and only if my exceptions wont execute my calculation should execute
    calculate=False

    if select==1:

        selbase = int(input("Which base will you use to enter data lines (base 16/8/2)? "))

        input1=input("Please enter an input: ")
        
        if input1 == "A" or input1 == "B" or input1 == "C" or input1 == "D" or input1 == "E" or input1 == "F":                
                print("This hexadecimal notation cannot be represented as 3 digits.")
        else:
            #This is the function which I calculate the digit
            for i in input1:
                lenght=lenght+1

            if selbase == 2:
                #If my code do not has 3 digit my code wont execute
                if lenght==3:
                    A=int(input1[0])
                    B=int(input1[1])
                    C_IN=int(input1[2])
                    calculate=True
                else:
                    print("Please enter a valid 3 digit number!")
                         
            elif selbase == 8 or selbase ==16:
                #It is same calculation for 8 and 16 digits

                if lenght == 1 and int(input1)<8 and int(input1)>=0:
                    input2 = int(input1)
                    C_IN=int(input2)%2
                    input2=int(input2/2)
                    B=input2%2
                    input2=int(input2/2)
                    A=input2%2
                    input2=int(input2/2)
                    calculate=True
                    
                elif int(input1)>7:                
                    print("This number cannot be represented in 3 digit!")

                else:
                    #It must be a 1 digit number for calculate it.
                    print("Please enter a 1 digit number!")
                
            else:
                print("Please enter a valid number!")
    #If you select 2 code will end
    elif select==2:
        print("You have chosen option 2")
        print("bye")

    else:
        print("Please enter a valid number!")

    #It is our bit translating calculations.
    if calculate:    
        if A == 0:
            if B == 0:
                if C_IN == 0:
                    SUM = 0
                    C_OUT = 0
                elif C_IN == 1:
                    SUM = 1
                    C_OUT = 0
            elif B == 1: 
                if C_IN == 0:
                    SUM = 1
                    C_OUT = 0
                elif C_IN == 1:
                    SUM = 0
                    C_OUT = 1
        elif A == 1:
            if B == 0:
                if C_IN == 0:
                    SUM = 1
                    C_OUT = 0
                elif C_IN == 1:
                    SUM = 0
                    C_OUT = 1
            elif B == 1:
                if C_IN == 0:
                    SUM = 0
                    C_OUT = 1
                elif C_IN == 1:
                    SUM = 1
                    C_OUT = 1
        #Lastly it prints sum and c_out values.
        print("sum: "+ str(SUM),"C_OUT: "+ str(C_OUT))


