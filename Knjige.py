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
