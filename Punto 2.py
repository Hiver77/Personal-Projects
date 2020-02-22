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
        
        coef_r  = [a-b for a,b in zip(self.Coeficientes, Pol.Coeficiente)]
        if len(self.Coeficientes) < len(Pol.Coeficientes):
            coef_r+= [-v for v in Pol.Coeficientes[len(self.Coeficientes):]]
        else: 
            coef_r+=self.Coeficientes[len(Pol.Coeficientes)]

        return Polinomio(coef_r)


    def Multi(self,Pol):

        r= [0]*(len(self.Coeficientes)+len(Pol.Coeficientes)-1)
        for sgrado, scoef in enumerate(self.Coeficientes):
            for grado, coef in enumerate(Pol.Coeficientes):
                coef_r[sgrado+ogrado]+= scoef*coef

        return Polinomio(coef_r)

    def escalar(self,num):

        return Polinomio([num*coef for coef in self.Coeficientes])

    def evaluar(self,num):





Pol1  = Polinomio([1,2,3])
Pol2 = Polinomio([2,3,4])

a = Pol1.Suma(Pol2)
print(a.Coeficientes)