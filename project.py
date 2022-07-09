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
       #Returning the values in the specified format as given in the assignment

        return {'name':self.FirstName + " " + self.LastName,
              "Date":Date,"Regular Hours Worked":Reg_hours,'Overtime Hours Worked':overtime_hours,
               "Regular Rate":self.HourlyRate,"Overtime Rate":overtime_rate,"Regular Pay":regular_pay,
               "Overtime Pay":overtime_pay,
               "Gross Pay":gross_pay,"Standard Rate Pay":standard_pay,"Higher Rate Pay":higher_pay,"Standard Tax":standard_tax,
               "Higher Tax":higher_tax,"Total Tax":total_tax,"Tax Credit":self.TaxCredit,"Net Tax":net_tax,"PRSI":prsi,"Net Deductions":
               net_deductions,"Net Pay":net_pay}

        #Running tests
    #Net pay cannot exceed gross pay
    def testNetLessEqualGross(self):
        e=Employee(12345,"Green","joe",37,16,1.5,72,710)
        pi=e.computePayment(1,'31/10/2021')
        return self.assertLessEqual(pi['NetPay'],pi['GrossPay'])
    
    #Overtime pay or overtime hours cannot be negative
    def testOvertimePayNegative(self):
        e=Employee(12345,"Green","joe",37,16,1.5,72,710)
        pi=e.computePayment(1,'31/10/2021')
        return self.assertLess(0,pi['Overtime Pay'])
    
    #Regular Hours Worked cannot exceed hours worked
    def testRegHoursGreaterHoursWorked(self):
        e=Employee(12345,"Green","joe",37,16,1.5,72,710)
        pi=e.computePayment(1,'31/10/2021')
        return self.assertLess(pi['Regular Hours Worked'],pi['Regular Hours worked']+pi['Overtime Hours Worked'])
    
    #Higher Tax cannot be negative
    def testHigherTaxNegative(self):
        e=Employee(12345,"Green","joe",37,16,1.5,72,710)
        pi=e.computePayment(1,'31/10/2021')
        return self.assertLess(0,pi['Higher Tax'])
    
    #Net Pay cannot be Negative
    def NetPayNegative(self):
        e=Employee(12345,"Green","joe",37,16,1.5,72,710)
        pi=e.computePayment(1,'31/10/2021')
        return self.assertLess(0,pi['Net Pay'])
