import sys

class Biblioteka: 

      def __init__(self,listaKnjiga):

            self.dostupneKnjige=listaKnjiga 

  

      def dostupneKnjigePrikaz(self): 

                   print("Dostupne knjige u knjižnici:") 

                   for knjiga in self.dostupneKnjige: 

                         print(knjiga) 

      def posudiKnjigu(self,zatrazenaKnjiga): 

            if zatrazenaKnjiga in self.dostupneKnjige: 

                  print("Zatražena knjiga je upravo posuđena.") 

                  self.dostupneKnjige.remove(zatrazenaKnjiga) 

            else: 

                  print("Nažalost, knjiga je već posuđena.") 

                   

      def dodajKnjigu(self,vracenaKnjiga): 

            self.dostupneKnjige.append(vracenaKnjiga) 

            print("Knjiga je vraćena.")

class Clan: 

      def zatrazenaKnjiga(self): 

            print("Napišite ime knjige koju želite podignuti: ") 

            self.knjiga=input() 

            return self.knjiga 

  

      def vratiKnjigu(self): 

            print("Napišite ime knjige koju želite vratiti: ") 

            self.knjiga=input() 

            return self.knjiga 


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


main() 

