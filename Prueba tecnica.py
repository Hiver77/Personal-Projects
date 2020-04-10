import numpy as np

#Se crea un diccionario que contendrá la posición de cada ficha

Fichas = ['Torre','Caballo','Alfín','Reina','Rey']
Tablero = {}

for fich in Fichas:
    Tablero[fich] = np.zeros(shape=(8,8))

#Posición Aleatoria
Pi = np.random.randint(0,8)
Pj = np.random.randint(0,8)

#Posición Posibles movimientos
for fich in Fichas:    
     
    for i in range(0,8):
            for j in range(0,8):
                if fich == 'Torre':
                    if (i==Pi) or (j==Pj):
                        Tablero[fich][i][j] = 1
                
                if fich == 'Caballo':
                    if (((i-Pi)**2)+((j-Pj)**2))==5:
                        Tablero[fich][i][j] = 1
                        
                if fich == 'Alfín':
                    if (np.abs(i-Pi)==np.abs(j-Pj)):
                        Tablero[fich][i][j] = 1
                        
                if fich == 'Reina':
                    if ((i==Pi) or (j==Pj) or (np.abs(i-Pi)==np.abs(j-Pj))):
                        Tablero[fich][i][j] = 1
                        
                if fich == 'Rey':
                    if ((np.abs(i-Pi)<=1) and (np.abs(j-Pj)<=1)):
                        Tablero[fich][i][j] = 1
                
    Tablero[fich][Pi][Pj] = 8  


print(Tablero)

#holaa