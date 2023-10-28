list1 = [50,90,60]
list2 = [15,60,75]
list3 = [60,60,60]
listmidterm = [list1,list2,list3] 

def average(listmidterm) :
    listaverage = []
    for list1 in listmidterm:      
        midterm1 = list1[0] * 3/10 
        midterm2 = list1[1] * 3/ 10
        final = list1[2] * 4/ 10 
        toplam = midterm1 + midterm2 + final
        ortalama = toplam / 3
        listaverage.append(ortalama)
    return listaverage
print(average(listmidterm))

def normalize_grades (listaverage) :
    listincreasedgrades = []
    for i in listaverage:
        maxaverage = 0
        if i > maxaverage :
            i == maxaverage
    difference = 100 - maxaverage
    increasedgrade1 : listaverage[0] + difference
    increasedgrade2 : listaverage[1] + difference
    increasedgrade3 : listaverage[2] + difference
    listincreasedgrades.append(increasedgrade1,increasedgrade2,increasedgrade3)
    return listincreasedgrades

    def find_AA(listincreasedgrades) :
        AA = []
        AAgrades = 0
        for i in listincreasedgrades :
            if i > 90 :
                i == AAgrades 
            AA.append(AAgrades)    

        return AAgrades 


average(listmidterm(normalize_grades(listaverage)(find_AA(listincreasedgrades))))        

      


        
        


    
    

