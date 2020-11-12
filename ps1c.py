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
    
    high = 10000
    low = 0
    current_savings = 0
    months = 0
    iteration = 0
    monthly_salary_rate = 0
    

    #get user data
    print('Please enter the following information...')
    
    total_cost = float(1000000)
    annual_salary_input = float(input('Annual Salary: '))
    annual_salary = annual_salary_input
    semi_annual_raise = float(0.07)
    
    down_payment = total_cost * down_payment_rate #calculate down payment on house
    salary_monthly = annual_salary / float(12) #calculate monthly salary from annual
    
    
    epsilon_chk = current_savings - down_payment >= 100 and current_savings - down_payment <= 0

    #calculate monthly accumulation
    print('Thank you. Calculating...')

    while not epsilon_chk and not months == 36:

        annual_salary = annual_salary_input
        months = 0
        current_savings = 0

        guess = float(high + low) / 2.0

        monthly_salary_rate = guess * 0.01
        monthly_salary_saved = salary_monthly * monthly_salary_rate

        while not current_savings >= down_payment:

            current_savings += (current_savings * annual_savings_rate) / float(12) #adds interest earned
            current_savings += monthly_salary_saved #adds base salary saved
            
            #check if 6 months has passed, raises salary if true
            if not months == 0 and months % 6 == 0:
                
                annual_salary += annual_salary * semi_annual_raise #increases salary
                salary_monthly = annual_salary / float(12) #recalculates monthly salary
                monthly_salary_saved = salary_monthly * monthly_salary_rate #recalculates salary savings
            
            months += 1 #adds to month count
        
        iteration += 1

        epsilon = current_savings - down_payment
        epsilon_chk
        print(months, monthly_salary_rate, current_savings, epsilon)

        if months < 36:
            high = guess
        elif months > 36:
            low = guess
        else:
            continue

    if monthly_salary_rate * 100 > 100:
        return 'It is not possible to pay the down payment in three years.'
    else:
        return f'after {iteration} iterations, if you saved %{monthly_salary_rate * 100} of ${salary_monthly} at ${monthly_salary_saved} for {months} months, you would have ${current_savings} with an epsilon of {epsilon}'

#start program
print(best_savings_rate())
