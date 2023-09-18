#  .----------------. .----------------. .----------------.              .----------------. .----------------. .----------------. .----------------. .-----------------..----------------. 
# | .--------------. | .--------------. | .--------------. |            | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |
# | |      __      | | |   ______     | | |   ______     | |            | |  _________   | | |     ____     | | |  _______     | | |  _________   | | | ____  _____  | | |     ____     | |
# | |     /  \     | | |  |_   __ \   | | |  |_   __ \   | |            | | |  _   _  |  | | |   .'    `.   | | | |_   __ \    | | | |_   ___  |  | | ||_   \|_   _| | | |   .'    `.   | |
# | |    / /\ \    | | |    | |__) |  | | |    | |__) |  | |            | | |_/ | | \_|  | | |  /  .--.  \  | | |   | |__) |   | | |   | |_  \_|  | | |  |   \ | |   | | |  /  .--.  \  | |
# | |   / ____ \   | | |    |  ___/   | | |    |  ___/   | |            | |     | |      | | |  | |    | |  | | |   |  __ /    | | |   |  _|  _   | | |  | |\ \| |   | | |  | |    | |  | |
# | | _/ /    \ \_ | | |   _| |_      | | |   _| |_      | |            | |    _| |_     | | |  \  `--'  /  | | |  _| |  \ \_  | | |  _| |___/ |  | | | _| |_\   |_  | | |  \  `--'  /  | |
# | ||____|  |____|| | |  |_____|     | | |  |_____|     | |            | |   |_____|    | | |   `.____.'   | | | |____| |___| | | | |_________|  | | ||_____|\____| | | |   `.____.'   | |
# | |              | | |              | | |              | |            | |              | | |              | | |              | | |              | | |              | | |              | |
# | '--------------' | '--------------' | '--------------' |            | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |
#  '----------------' '----------------' '----------------'              '----------------' '----------------' '----------------' '----------------' '----------------' '----------------'      
#     _                                                    _                 _                                _                                  _    __  
#    | |                                                  (_)               (_)                              | |                                | |   \_\ 
#    | |__    _   _      __ _   ___   ___    ___     ___   _    __ _   ____  _    ___    _ __     ___      __| |   ___   _ __ ___     ___     __| |   ___ 
#    | '_ \  | | | |    / _` | / __| / __|  / _ \   / __| | |  / _` | |_  / | |  / _ \  | '_ \   / _ \    / _` |  / _ \ | '_ ` _ \   / _ \   / _` |  / _ \
#    | |_) | | |_| |   | (_| | \__ \ \__ \ | (_) | | (__  | | | (_| |  / /  | | | (_) | | | | | |  __/   | (_| | |  __/ | | | | | | | (_) | | (_| | |  __/
#    |_.__/   \__, |    \__,_| |___/ |___/  \___/   \___| |_|  \__,_| /___| |_|  \___/  |_| |_|  \___|    \__,_|  \___| |_| |_| |_|  \___/   \__,_|  \___|
#              __/ |                                                                                                                                      
#             |___/                                                                                                                                       
#   |------------------------------------------------------------------|
#   | PROGRMMATORE: Lombardi Michele                                   | 
#   | DATA CREAZIONE: 15/09/2023                                       |                                     
#   | DESCRIZIONE FILE: Classe creazione Tabellone                     |                         
#   |                                                                  |     
#   |------------------------------------------------------------------|
       
import random
import math 

import Partita as p

class Tabellone(object):

    def __init__(self, n_gioccatori, lista_squadre):
        self.numero_squadre = n_gioccatori

        

        random.shuffle(lista_squadre)  # Mescola la lista in modo casuale
        meta = len(lista_squadre) // 2  # Trova l'indice di metà della lista mescolata

        self.numero_partite = self.numero_squadre - 1
        self.numero_fasi =  math.ceil(math.log(self.numero_partite, 2)) #arrotondo in eccesso il log di 2 di numero partite 

        self.tabellone_dx =  [[] for _ in range(self.numero_fasi)]      #creo array di liste pe quanti fasi ci sono
        self.tabellone_sx = [[] for _ in range(self.numero_fasi)]       #creo array di liste pe quanti fasi ci sono

        # Dividi la lista mescolata in due parti
        self.tabellone_dx[0] = lista_squadre[:meta]         #fase 1 lista squadre
        self.tabellone_sx[0] = lista_squadre[meta:]         #fase 1 lista squadre


    def avvia_torneo(self):
        for i in range(self.numero_fasi-1):
            self.fase(i)

        f = p.Partita(self.tabellone_dx[self.numero_fasi-1][0],self.tabellone_sx[self.numero_fasi-1][0])
        print(f)
        print("FIN£ TORNEO")
            
    def fase(self, n):
        s = 0
        print("\n---\nFase Torne numero: " + str(n))

        for i in range(len(self.tabellone_dx[n]) // 2):

            pd = p.Partita(self.tabellone_dx[n][s],self.tabellone_dx[n][s+1])
            ps = p.Partita(self.tabellone_sx[n][s],self.tabellone_sx[n][s+1])

            print("\ngirone destra:")
            print(pd)
            pd.avvia()
            print("\ngirone sinistra:")
            print(ps)
            ps.avvia()

            

            s = s+2
        print("\nfine della fase " +str(n)+ "\n---\n")
        
        if n != self.numero_fasi-1:
            for item in self.tabellone_dx[n]:
                if item.get_state():
                    self.tabellone_dx[n+1].append(item)
            for item in self.tabellone_sx[n]:
                if item.get_state():
                    self.tabellone_sx[n+1].append(item)
        else:
            print("FINALE TORNEO")
        
