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
        #setting variables upfront to make the calculations more readable
        if TotalTime > self.RegHours:
            Reg_hours=self.RegHours
            overtime_hours=TotalTime-self.RegHours
        else:
            Reg_hours=TotalTime
            overtime_hours=0
            
        
        overtime_rate=int(self.HourlyRate*self.OTMultiple)
        regular_pay=self.HourlyRate*self.RegHours
        overtime_pay=int(overtime_hours*overtime_rate)
        gross_pay=overtime_pay+regular_pay
        if gross_pay > self.StandardBand:
            standard_pay=self.StandardBand
        else:
            standard_pay=gross_pay
        higher_pay=gross_pay-standard_pay
        standard_tax=int(standard_pay*0.2)
        higher_tax=higher_pay*0.4
        total_tax=standard_tax+higher_tax
        net_tax=round(total_tax-self.TaxCredit,2)
        prsi=0.04*gross_pay
        net_deductions=round(net_tax+prsi,2)
        net_pay=round(gross_pay-net_deductions,2)
