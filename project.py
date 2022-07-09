#Creating Employee class
class Employee:
 #initializing attributes of the class
    def __init__(self,StaffID,LastName,FirstName,RegHours,HourlyRate,OTMultiple,TaxCredit,StandardBand):
        #Assigning values to attributes
        self.StaffID=StaffID
        self.LastName=LastName
        self.FirstName=FirstName
        self.RegHours=RegHours
        self.HourlyRate=HourlyRate
        self.OTMultiple=OTMultiple
        self.TaxCredit=TaxCredit
        self.StandardBand=StandardBand
    #Creating the `computePayment` method     
    def computePayment(self,TotalTime,Date):
