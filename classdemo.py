class Staff:
    def __init__(self,pPsosition,pName,pPay):
        self._position = pPsosition
        self.name = pName
        self.pay = pPay
        print('Creating stuff objects')
        
    def __str__(self):
        return "Position = %s , Name = %s , Pay = %d" %(self._position, self.name, self.pay )
        
        
    def calculatePay(self):
        promt = '\n Enter number of hours worked for %s: ' %(self.name)
        hours = input(promt)
        promt = 'Enter the hourly rate for %s: ' %self.name
        hourlyRate = input(promt)
        self.pay = int(hours)*int(hourlyRate)
        return self.pay

    @property
    def position(self):
        print('Getter Method')
        return self._position

    @position.setter
    def position(self, value):
        if value == 'Manager' or value == 'Basic':
            self._position = value
            
        
        else:
            print('Position is invalid. No changes made.')

class ManagmentStaff(Staff):       
    def __init__(self, pName, pPay, pAllowance, pBonus):
        super().__init__('Manager', pName, pPay)  
        self.allowance = pAllowance
        self.bonus = pBonus
        
    def calculatePay(self):
        basicPay = super().calculatePay()
        self.pay = basicPay + self.allowance
        return self.pay
    
    def calculatePerfBonus(self):
        promt = 'Enter performance grade for %s' %(self.name)
        grade = input(promt)
        if (grade == 'A'):
            self.bonus = 1000
        else:
            self.bonus = 0
        return self.bonus
    
class BasicStaff(Staff):
    def __init__(self, pName, pPay):
        super().__init__('Basic', pName, pPay)
    

    
