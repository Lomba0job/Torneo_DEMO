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
#   | DESCRIZIONE FILE: Necessario per testare le funzionalità         |                         
#   |                   inserite nel proggramma                        |     
#   |------------------------------------------------------------------|
       
import Osquadra as o
import Creazione_Tabellone as c


def main():
    lista_s = []

    for i in range(12):
        nome = "squadra" + str(i)
        s = o.Oggetto_Squadra(nome)
        lista_s.append(s)

    t = c.Tabellone(len(lista_s), lista_s)
    t.avvia_torneo()

if __name__ == "__main__":
    main()


    """
    OUTPUT
    
---
Fase Torne numero: 0

girone destra:
squadra10  vs squadra8
vinto: squadra8

girone sinistra:
squadra1  vs squadra6
vinto: squadra1

girone destra:
squadra4  vs squadra2
vinto: squadra4

girone sinistra:
squadra9  vs squadra7
vinto: squadra9

girone destra:
squadra11  vs squadra5
vinto: squadra5

girone sinistra:
squadra0  vs squadra3
vinto: squadra0

fine della fase 0
---


---
Fase Torne numero: 1

girone destra:
squadra8  vs squadra4
vinto: squadra4

girone sinistra:
squadra1  vs squadra9
vinto: squadra1

fine della fase 1
---


---
Fase Torne numero: 2

girone destra:
squadra4  vs squadra5
vinto: squadra4

girone sinistra:
squadra1  vs squadra0
vinto: squadra0

fine della fase 2
---

squadra4  vs squadra0
FIN£ TORNEO
"""