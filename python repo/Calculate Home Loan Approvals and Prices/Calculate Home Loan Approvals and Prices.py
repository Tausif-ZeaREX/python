def calculate_max_home_loan():
    salary = float(input('Input Your Household pre-tax income: '))
    rate = float(input('Estimate your expected interest rate '))
    down = float(input('How much do you have available as downpayment ?'))

    max_monthly = (salary * 0.28) / 12
    print('\n The maximum monthly payment would be around', round(max_monthly, 2))
    interest_variable = pow((1 + rate/1200), 360)
    rate_math = ((interest_variable/(interest_variable - 1)) * (rate / 1200)) 
    max_loan = max_monthly / rate_math
    print('The maximum youre likely to be approved for is around', round(max_loan), ' Based on  just salary')
    print('however, to avoid PMI and have a 20% down payment, the max you would want to borrow would be ', round(down * 5))

calculate_max_home_loan()