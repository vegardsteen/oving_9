# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:36:10 2021

@author: vegar
"""


with open("sporsmaalsfil.txt", "r", encoding = "UTF8") as fil:
    
    tekst = []
    fasit = []
    alt = []   
    
    for linje in fil: 
             
        splitrow = linje.split(":")                           
        tekst.append(splitrow[0])        
        fasit.append(splitrow[1])  
        for i in range(len(fasit)):
            fasit[i] = int(fasit[i])      
            
        alternaltiver = splitrow[2].strip("[").split(",")        
        alt.append(alternaltiver)
          
score1 = 0
score2 = 0


from klasse_spm import Spm


if __name__ == "__main__":
   
    spm_1 = Spm(tekst[0], alt[0], fasit[0])
    print(spm_1)
    bruker_svar1 = int(input("Velg alternaltiv for spiller 1: "))
    bruker_svar2 = int(input("Velg alternaltiv for spiller 2: "))
    
    spm_1.korrekt_svar()
    
    if spm_1.sjekk_svar(bruker_svar1):
        print("Spiller 1: riktig svar! \n")
        score1 += 1
    else:
        print("Spiller 1: feil. \n")
        
    if spm_1.sjekk_svar(bruker_svar2):
        print("Spiller 2: riktig svar! \n")
        score2 += 1
    else:
        print("Spiller 2: feil.\n")        
        
    spm_2 = Spm(tekst[1], alt[1], fasit[1])
    print(spm_2)
    bruker_svar1 = int(input("Velg alternaltiv for spiller 1: "))
    bruker_svar2 = int(input("Velg alternaltiv for spiller 2: "))
    
    spm_2.korrekt_svar()
    
    if spm_2.sjekk_svar(bruker_svar1):
        print("Spilelr 1: riktig svar! \n")
        score1 += 1
    else:
        print("Spiller 1: feil. \n")
        
    if spm_2.sjekk_svar(bruker_svar2):
        print("Spiller 2: riktig svar! \n")
        score2 += 1
    else:
        print("Spiller 2: feil. \n")
        
     
    spm_3 = Spm(tekst[2], alt[2], fasit[2])
    print(spm_3)
    bruker_svar1 = int(input("Velg alternaltiv for spiller 1: "))
    bruker_svar2 = int(input("Velg alternaltiv for spiller 2: "))
    
    spm_3.korrekt_svar()
    
    if spm_3.sjekk_svar(bruker_svar1):
        print("Spilelr 1: riktig svar! \n")
        score1 += 1
    else:
        print("Spiller 1: feil.\n") 
        
    if spm_3.sjekk_svar(bruker_svar2):
        print("Spiller 2: riktig svar! \n")
        score2 += 1
    else:
        print("Spiller 2: feil.\n") 
  
    spm_4 = Spm(tekst[3], alt[3], fasit[3])
    print(spm_4)
    bruker_svar1 = int(input("Velg alternaltiv for spiller 1: "))
    bruker_svar2 = int(input("Velg alternaltiv for spiller 2: "))
    
    spm_4.korrekt_svar()
    
    if spm_4.sjekk_svar(bruker_svar1):
        print("Spilelr 1: riktig svar! \n")
        score1 += 1
    else:
        print("Spiller 1: feil.\n")
        
    if spm_4.sjekk_svar(bruker_svar2):
        print("Spiller 2: riktig svar! \n")
        score2 += 1
    else:
        print("Spiller 2: feil.\n") 
  
    spm_5 = Spm(tekst[4], alt[4], fasit[4])
    print(spm_5)
    bruker_svar1 = int(input("Velg alternaltiv for spiller 1: "))
    bruker_svar2 = int(input("Velg alternaltiv for spiller 2: "))
    
    spm_5.korrekt_svar()
    
    if spm_5.sjekk_svar(bruker_svar1):
        print("Spilelr 1: riktig svar! \n")
        score1 += 1
    else:
        print("Spiller 1: feil.\n")
        
    if spm_5.sjekk_svar(bruker_svar2):
        print("Spiller 2: riktig svar! \n")
        score2 += 1
    else:
        print("Spiller 2: feil.\n") 
  
    
    spm_6 = Spm(tekst[5], alt[5], fasit[5])
    print(spm_6)
    bruker_svar1 = int(input("Velg alternaltiv for spiller 1: "))
    bruker_svar2 = int(input("Velg alternaltiv for spiller 2: "))
    
    spm_6.korrekt_svar()
    
    if spm_6.sjekk_svar(bruker_svar1):
        print("Spilelr 1: riktig svar! \n")
        score1 += 1
    else:
        print("Spiller 1: feil. \n")
        
    if spm_6.sjekk_svar(bruker_svar2):
        print("Spiller 2: riktig svar! \n")
        score2 += 1
    else:
        print("Spiller 2: feil.\n") 
    
    spm_7 = Spm(tekst[6], alt[6], fasit[6])
    print(spm_7)
    bruker_svar1 = int(input("Velg alternaltiv for spiller 1: "))
    bruker_svar2 = int(input("Velg alternaltiv for spiller 2: "))
    
    spm_7.korrekt_svar()
    
    if spm_7.sjekk_svar(bruker_svar1):
        print("Spilelr 1: riktig svar! \n")
        score1 += 1
    else:
        print("Spiller 1: feil.\n")
        
    if spm_7.sjekk_svar(bruker_svar2):
        print("Spiller 2: riktig svar! \n")
        score2 += 1
    else:
        print("Spiller 2: feil.\n") 
    
    
    
print("Spiller 1 fikk", score1, "poeng.")  
print("Spiller 2 fikk", score2, "poeng.")         
        
        