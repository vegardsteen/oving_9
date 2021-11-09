# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 22:31:39 2021

@author: vegar
"""

from klasse_spm import Spm

score1 = []
score2 = []

def quiz():
    with open("sporsmaalsfil.txt", "r", encoding = "UTF8") as fil:
        for linje in fil:
            linje = linje.split(":")
            alt = linje[2].replace("[", " ").replace("]", " ")
            spm = Spm(linje[0], alt.split(","), int(linje[1]))
            print(spm)
            
            bruker_svar1 = int(input("Velg alternaltiv for spiller 1: "))
            bruker_svar2 = int(input("Velg alternaltiv for spiller 2: "))
            
            spm.korrekt_svar()
    
            if spm.sjekk_svar(bruker_svar1):
                print("Spiller 1: riktig svar! \n")
                score1.append(1)
            else:
                print("Spiller 1: feil. \n")
                
            if spm.sjekk_svar(bruker_svar2):
                print("Spiller 2: riktig svar! \n")
                score2.append(1)
            else:
                print("Spiller 2: feil.\n")  

if __name__ == "__main__":
    quiz()
    print("Resultat.\n", "Spiller 1 fikk", len(score1), "poeng.")
    print("Spiller 2 fikk", len(score2), "poeng.")
