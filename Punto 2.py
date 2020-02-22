#Implementación Clases Objeto Algebraico.

class Polinomio:
    def __init__(self,Coeficientes = []):
        self.Coeficientes = Coeficientes[:]

    def Suma (self,Pol):
        coef_r = [a+b for a,b in zip(self.Coeficientes, Pol.Coeficientes)]
        
        if len(self.Coeficientes) < len(Pol.Coeficientes):
            coef_r+ Pol.Coeficientes[len(self.Coeficientes):]

        if len(self.Coeficientes) > len(Pol.Coeficientes):
            coef_r+ self.Coeficientes[len(Pol.Coefientes):]
               
        return Polinomio(coef_r)


    def Resta(self, Pol):
    
    def Multi(self,Pol):
    
    def escalar(self,num):

    def evaluar(self,num)





Pol1  = Polinomio([1,2,3])
Pol2 = Polinomio([2,3,4])

a = Pol1.Suma(Pol2)
print(a.Coeficientes)