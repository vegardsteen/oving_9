# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:54:03 2021

@author: vegar
"""

class Spm:
    
    def __init__ (self, tekst, alt, svar):
        self.tekst = tekst
        self.alt = alt
        self.svar = svar
             
    def __str__(self):
        oppgave = f"{self.tekst} \n"
        for index, verdi in enumerate(self.alt):
            #index += 1
            oppgave += f"{index}) {verdi} \n"
            
        return oppgave
    
    def sjekk_svar(self, riktig_svar):
        if riktig_svar == self.svar:
            return True
        else:
            False  
            
    def korrekt_svar(self):
        print("\nRiktig svar er alternaltiv", self.svar, "\n")
    
alt_1 = ["Bergen", "Oslo", "Trondheim"]
alt_2 = ["London", "Liverpool", "Birmingham"]
alt_3 = ["Göteborg", "Töckfors", "Stockholm"]

tekst_1 = "Hva er hovedstaten i Norge?"
tekst_2 = "Hva er hovedstaden i England"
tekst_3 = "Hva er hovedstaten i Sverige?"


if __name__ == "__main__":
    
    spm_1 = Spm(tekst_1, alt_1, 2)
    print(spm_1, )
    bruker_svar = int(input("Hvilket alternaltiv er riktig? "))
    if spm_1.sjekk_svar(bruker_svar):
        print("Riktig svar! \n")
    else:
        print("Feil, riktig svar er 2. Oslo. \n")

    spm_1.korrekt_svar()
    
    spm_2 = Spm(tekst_2, alt_2, 1)
    print(spm_2)
    bruker_svar = int(input("Hvilket alternaltiv er riktig? "))
    if spm_2.sjekk_svar(bruker_svar):
        print("Riktig svar! \n")
    else:
        print("Feil, riktig svar er 1. London.\n")
    
    spm_3 = Spm(tekst_3, alt_3, 3)
    print(spm_3)
    bruker_svar = int(input("Hvilket alternaltiv er riktig? "))
    if spm_3.sjekk_svar(bruker_svar):
        print("Riktig svar! \n")
    else:
        print("Feil, riktig svar er 3. Stockholm. \n")


