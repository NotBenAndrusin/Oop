from EmployeeClass import Employee as e
from PayrollDeductionClass import PayrollDeductionTransaction as pdt

# employee instance
worker = e('Jimmy Smith', 58475, 'Information Systems', 'Developer', 6800.0)

# payroll deduction instances
deduction1 = pdt('food court', '8/14/2022', 22.50, 39119)
deduction2 = pdt('gift contribution', '8/12/2022', 25.00, 58475)
deduction3 = pdt('food court', '8/17/2022', 15.25, 21547)
deduction4 = pdt('vending machine', '8/22/2022', 3.00, 58475)
deduction5 = pdt('vending machine', '8/5/2022', 2.75, 58475)
deductions = [deduction1, deduction2, deduction3, deduction4, deduction5]

# calculate net pay
netPay = worker.getSalary()
for deduction in deductions:
    if deduction.getID() == worker.getID():
        netPay -= deduction.getChargeAmount()

# create report
print('*** Employee Pay ***')
print('Name:', worker.getName())
print('ID Number:', worker.getID())
print('Department:', worker.getDepartment())
print('Gross Pay:', '${:,.2f}'.format(worker.getSalary()))
print('Net Pay:', '${:,.2f}'.format(netPay))