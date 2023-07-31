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

            

    
