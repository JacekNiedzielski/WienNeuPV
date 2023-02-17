import math

class Timber:
    def __init__(self, strength_class):
        self.strength_class = strength_class
        self._get_attributes()
    
    def _get_attributes(self):
        
        if self.strength_class == "C14":
            #Strength parameters in MPa
            self.fmk = 14.0
            self.ft0k = 8.0
            self.ft90k = 0.4
            self.fc0k = 16.0
            self.fc90k = 2.0
            self.fvk = 1.7
            #Stiffness parameters in MPa
            self.E0mean = 7000
            self.E005 = 4700 
            self.E90mean = 230
            self.Gmean = 440
            #Density in kg/m3
            self.pk = 290
            self.pmean = 350
        
        elif self.strength_class == "C16":
            #Strength parameters in MPa
            self.fmk = 16.0
            self.ft0k = 10.0
            self.ft90k = 0.5
            self.fc0k = 17.0
            self.fc90k = 2.2
            self.fvk = 1.8
            #Stiffness parameters in MPa
            self.E0mean = 8000
            self.E005 =  5400
            self.E90mean = 270
            self.Gmean = 500
            #Density in kg/m3
            self.pk = 310 
            self.pmean = 370
        
        elif self.strength_class == "C18":
            #Strength parameters in MPa
            self.fmk = 18.0
            self.ft0k = 11.0
            self.ft90k = 0.5
            self.fc0k = 18.0
            self.fc90k = 2.2
            self.fvk = 2.0
            #Stiffness parameters in MPa
            self.E0mean = 9000
            self.E005 = 6000
            self.E90mean = 300
            self.Gmean = 560
            #Density in kg/m3
            self.pk = 320
            self.pmean = 380

        elif self.strength_class == "C20":
            #Strength parameters in MPa
            self.fmk = 20.0
            self.ft0k = 12.0
            self.ft90k = 0.5
            self.fc0k = 19.0
            self.fc90k = 2.3
            self.fvk = 2.2
            #Stiffness parameters in MPa
            self.E0mean = 9500
            self.E005 = 6400
            self.E90mean = 320
            self.Gmean = 590
            #Density in kg/m3
            self.pk = 330
            self.pmean = 390

        elif self.strength_class == "C22":
            #Strength parameters in MPa
            self.fmk = 22.0
            self.ft0k = 13.0
            self.ft90k = 0.5
            self.fc0k = 20.0
            self.fc90k = 2.4
            self.fvk = 2.4
            #Stiffness parameters in MPa
            self.E0mean = 10000
            self.E005 = 6700
            self.E90mean = 330
            self.Gmean = 630
            #Density in kg/m3
            self.pk = 340
            self.pmean = 410

        elif self.strength_class == "C24":
            #Strength parameters in MPa
            self.fmk = 24.0
            self.ft0k = 14.0
            self.ft90k = 0.5
            self.fc0k = 21.0
            self.fc90k = 2.5
            self.fvk = 2.5
            #Stiffness parameters in MPa
            self.E0mean = 11000
            self.E005 = 7400
            self.E90mean = 370
            self.Gmean = 690
            #Density in kg/m3
            self.pk = 350 
            self.pmean = 420

        elif self.strength_class == "C27":
            #Strength parameters in MPa
            self.fmk = 27.0
            self.ft0k = 16.0
            self.ft90k = 0.6
            self.fc0k = 22.0
            self.fc90k = 2.6
            self.fvk = 2.8
            #Stiffness parameters in MPa
            self.E0mean = 11000
            self.E005 = 8000
            self.E90mean = 380
            self.Gmean = 720
            #Density in kg/m3
            self.pk = 370
            self.pmean = 450

        elif self.strength_class == "C30":
            #Strength parameters in MPa
            self.fmk = 30.0
            self.ft0k = 18.0
            self.ft90k = 0.6
            self.fc0k = 23.0
            self.fc90k = 2.7
            self.fvk = 3.0
            #Stiffness parameters in MPa
            self.E0mean = 12000
            self.E005 = 8000
            self.E90mean = 400
            self.Gmean = 750
            #Density in kg/m3
            self.pk = 380
            self.pmean = 460

        elif self.strength_class == "C35":
            #Strength parameters in MPa
            self.fmk = 35.0
            self.ft0k = 21.0
            self.ft90k = 0.6
            self.fc0k = 25.0
            self.fc90k = 2.8
            self.fvk = 3.4
            #Stiffness parameters in MPa
            self.E0mean = 13000
            self.E005 = 8700
            self.E90mean = 430
            self.Gmean = 810
            #Density in kg/m3
            self.pk = 400
            self.pmean = 480

        elif self.strength_class == "C40":
            #Strength parameters in MPa
            self.fmk = 40.0
            self.ft0k = 24.0
            self.ft90k = 0.6
            self.fc0k = 26.0
            self.fc90k = 2.9
            self.fvk = 3.8
            #Stiffness parameters in MPa
            self.E0mean = 14000
            self.E005 = 9400
            self.E90mean = 470
            self.Gmean = 880
            #Density in kg/m3
            self.pk = 420
            self.pmean = 500

        elif self.strength_class == "C45":
            #Strength parameters in MPa
            self.fmk = 45.0
            self.ft0k = 27.0
            self.ft90k = 0.6
            self.fc0k = 27.0
            self.fc90k = 3.1
            self.fvk = 3.8
            #Stiffness parameters in MPa
            self.E0mean = 15000
            self.E005 = 10000
            self.E90mean = 500
            self.Gmean = 940
            #Density in kg/m3
            self.pk = 440
            self.pmean = 520

        elif self.strength_class == "C50":
            #Strength parameters in MPa
            self.fmk = 50.0
            self.ft0k = 30.0
            self.ft90k = 0.6
            self.fc0k = 29.0
            self.fc90k = 3.2
            self.fvk = 3.8
            #Stiffness parameters in MPa
            self.E0mean = 16000
            self.E005 = 10700
            self.E90mean = 530 
            self.Gmean = 1000
            #Density in kg/m3
            self.pk = 460
            self.pmean = 550

        elif self.strength_class == "D30":
            #Strength parameters in MPa
            self.fmk = 30.0
            self.ft0k = 18.0
            self.ft90k = 0.6
            self.fc0k = 23.0
            self.fc90k = 8.0
            self.fvk = 3.0
            #Stiffness parameters in MPa
            self.E0mean = 10000
            self.E005 = 8000
            self.E90mean = 640
            self.Gmean = 600
            #Density in kg/m3
            self.pk = 530
            self.pmean = 640

        elif self.strength_class == "D35":
            #Strength parameters in MPa
            self.fmk = 35.0
            self.ft0k = 21.0
            self.ft90k = 0.6
            self.fc0k = 25.0
            self.fc90k = 8.4
            self.fvk = 3.4
            #Stiffness parameters in MPa
            self.E0mean = 10000
            self.E005 = 8700
            self.E90mean = 690
            self.Gmean = 650
            #Density in kg/m3
            self.pk = 560
            self.pmean = 670

        elif self.strength_class == "D40":
            #Strength parameters in MPa
            self.fmk = 40.0
            self.ft0k = 24.0
            self.ft90k = 0.6
            self.fc0k = 26.0
            self.fc90k = 8.8
            self.fvk = 3.8
            #Stiffness parameters in MPa
            self.E0mean = 11000
            self.E005 = 9400
            self.E90mean = 750
            self.Gmean = 700
            #Density in kg/m3
            self.pk = 590
            self.pmean = 700

        elif self.strength_class == "D50":
            #Strength parameters in MPa
            self.fmk = 50.0
            self.ft0k = 30.0
            self.ft90k = 0.6
            self.fc0k = 29.0
            self.fc90k = 9.7
            self.fvk = 4.6
            #Stiffness parameters in MPa
            self.E0mean = 14000
            self.E005 = 11800
            self.E90mean = 930 
            self.Gmean = 880
            #Density in kg/m3
            self.pk = 650
            self.pmean = 780

        elif self.strength_class == "D60":
            #Strength parameters in MPa
            self.fmk = 60.0
            self.ft0k = 36.0
            self.ft90k = 0.7
            self.fc0k = 32.0
            self.fc90k = 10.5
            self.fvk = 5.3
            #Stiffness parameters in MPa
            self.E0mean = 17000
            self.E005 = 14300
            self.E90mean = 1130 
            self.Gmean = 1060
            #Density in kg/m3
            self.pk = 700
            self.pmean = 840

        elif self.strength_class == "D70":
            #Strength parameters in MPa
            self.fmk = 70.0
            self.ft0k = 42.0
            self.ft90k = 0.9
            self.fc0k = 34.0
            self.fc90k = 13.5
            self.fvk = 6.0
            #Stiffness parameters in MPa
            self.E0mean = 20000
            self.E005 = 16800
            self.E90mean = 1330
            self.Gmean = 1250
            #Density in kg/m3
            self.pk = 900
            self.pmean = 1080


class TimberRectangleCS(Timber):

    def __init__(self, strength_class, width, height):
        super().__init__(strength_class)
        
        self.width = width
        self.height = height
        
        self.area = self._getarea()
        
        self.I_y = self._getMomentOfInertia()[0]
        self.I_z = self._getMomentOfInertia()[1]

        self.W_y = self._getBendingIndex()[0]
        self.W_z = self._getBendingIndex()[1]

        self.i_y = math.sqrt(self.I_y / self.area)
        self.i_z = math.sqrt(self.I_z / self.area)

    def _getarea(self):
        return self.width * self.height / 1000000 
    
    def _getMomentOfInertia(self):
        I_y = self.width * self.height**3 / 12 / 1000000000000
        I_z = self.height * self.width**3 / 12 / 1000000000000
        return I_y, I_z
    
    def _getBendingIndex(self):
        W_y = self.width * self.height**2 / 6 / 1000000000
        W_z = self.height * self.width**2 / 6 / 1000000000
        return W_y, W_z

    