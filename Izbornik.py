import sys
def main():             

      biblioteka=Biblioteka(["Programiranje u Pythonu","Harry Potter i kamen mudraca","Družba Pere Kvržice","Pale sam na svijetu"]) 

      clan=Clan() 

      ok=False 

      while ok==False: 

            print(""" ======BIBLIOTEKA======= 

                  1. Prikaži dostupne knjige 

                  2. Podigni knjigu

                  3. Vrati knjigu 

                  4. Zatvori program 

                  """) 

            izbor=int(input("Izaberi opciju:")) 

            if izbor==1: 

                        biblioteka.dostupneKnjigePrikaz() 

            elif izbor==2: 

                        biblioteka.posudiKnjigu(clan.zatrazenaKnjiga()) 

            elif izbor==3: 

                        biblioteka.dodajKnjigu(clan.vratiKnjigu()) 

            elif izbor==4:
                        sys.exit() 
