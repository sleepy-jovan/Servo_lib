class Servo:
    def Deg(self,deg,Deg):
        self.Degrice =  int(((((deg/90)+0.5)/20) * 65535))
        Deg = self.Degrice
        
        return Deg