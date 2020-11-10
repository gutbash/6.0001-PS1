# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 13:27:30 2020

@author: 4gutz
"""

#static information
down_payment_rate = 0.25
annual_savings_rate = 0.04



#calculate down payment
def best_savings_rate():
    
    #get user data
    print('Please enter the following information...')
    
    total_cost = float(1000000)
    annual_salary = float(input('Annual Salary: '))
    semi_annual_raise = float(0.07)
    
    #calculate down payment on house
    down_payment = total_cost * down_payment_rate
    #calculate monthly salary from annual
    salary_monthly = annual_salary / float(12)
    
    #calculate monthly accumulation
    print('Thank you. Calculating...')

    lst = list(range(1,10001))
    left = 0
    right = len(lst)-1
    mid = (right + left) // 2
    
    iteration = 0
    for i in lst:
        #state counter variables
        current_savings = 0
        months = 0
        iteration += 1
        while current_savings < down_payment:
            
            perc = i * 0.00001
            monthly_salary_rate = perc
            monthly_salary_saved = salary_monthly * monthly_salary_rate
            
            #adds interest earned
            current_savings += (current_savings * annual_savings_rate) / float(12)
            #adds base salary saved
            current_savings += monthly_salary_saved
            #adds to month count
            months += 1
            
            
            #check if 6 months has passed, raises salary if true
            if months % 6 == 0:
                
                #increases salary
                annual_salary += annual_salary * semi_annual_raise
                #recalculates monthly salary
                salary_monthly = annual_salary / float(12)
                #recalculates salary savings
                monthly_salary_saved = salary_monthly * monthly_salary_rate
        print(current_savings)
        if months <= 36:
            return i
        
    return

#start program
print(best_savings_rate())
