print("Welcome to bowling game")
#- girdiğinde çıkıcak output
#10 üstü girilince 1. adımda error versin
#fonksiyonlar yazılsın
#10. adımda spare strike durumu arttırması analşz edilsin
atış = 10
BallscoreA=[]
BallscoreB=[]
TotalscoreA=["0"," "," "," "," "," "," "," "," "," "," ",]
TotalscoreB=[]
holdinglistA=0
holdinglistB=[]
holdA=False
sıtrayk=False

totalscoreStr="| "

strike=0

def spare():
    print("B.")

step=0
 
while step<10:
    validity=False
    print("Player A rolls...")
    while validity==False:
        pina1=int(input("Pins:"))  
    
        if pina1==10:
            sıtrayk=True
            strike+=1
            print("strike")
            validity=True
            
            holdA=True
            BallscoreA.append(str(pina1))
            
            
            

        else:
            pina2=int(input("Pins:"))


            
            if pina1+pina2==10:
                print("spare")
                spare()
                validity=True
                

            elif pina1+pina2<10:

                BallscoreA.append(str(pina1))
                BallscoreA.append(str(pina2))
                validity=True
                #
                if holdA==True:
                    if strike==1:
                        holdinglistA+=10+pina1+pina2
                        TotalscoreA[step]=str(int(TotalscoreA[step-1])+10+int(pina1)+int(pina2))
                        TotalscoreA[step+1]=str(int(TotalscoreA[step])+pina1+pina2)
                        totalscoreStr += str(TotalscoreA[step])+" | "
                        holdA=False
                        holdinglistA=0
                    elif strike==2:
                        holdinglistA+=10+pina1+pina2
                        TotalscoreA[step-1]=str(int(TotalscoreA[step-2])+20+int(pina1))
                        TotalscoreA[step]=str(int(TotalscoreA[step-1])+pina1+pina2)
                        totalscoreStr += str(TotalscoreA[step-1])+" | "
                        totalscoreStr += str(TotalscoreA[step])+" | "
                        holdA=False
                        holdinglistA=0

                        
                        TotalscoreA[step]=str(int(TotalscoreA[step-1])+10+int(pina1)+int(pina2))
                        TotalscoreA[step+1]=str(int(TotalscoreA[step])+pina1+pina2)
                        totalscoreStr += str(TotalscoreA[step])+" | "
                    else:
                        holdinglistA+=10+pina1+pina2
                        
                        TotalscoreA[step-2]=str(30)
                        TotalscoreA[step]=str(int(TotalscoreA[step-1])+20+pina1)
                        TotalscoreA[step+1]=str(int(TotalscoreA[step])+pina1+pina2)
                        totalscoreStr += str(TotalscoreA[step])+" | "
                        totalscoreStr += str(TotalscoreA[step-1])+" | "
                        holdA=False
                        holdinglistA=0

                else:
                    TotalscoreA[step+1]=str(int(TotalscoreA[step])+pina1+pina2)
                
                
            elif pina1+pina2>10:
                print("What? There is only 10 ball!")
                validity=False



            else:
                print("An invalid input")
                validity=False
    print(str(TotalscoreA))
    print("Ball Scores: " + str(BallscoreA)) 
    
    print("Total Scores:")
    if holdA==False:
        totalscoreStr += str(TotalscoreA[step+1])+" | "
    a = (10-(step+1))*"  | "
    print(holdinglistA)
    print(totalscoreStr+a)
    step+=1


