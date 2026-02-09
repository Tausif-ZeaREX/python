def compound_interest(P,r,n,t): 
    Amount = P * (pow((1 + r/n), n*t))
    interest = Amount - P
    print("Compound Interest is", interest)
    print("Initial Investment was", P)
    print("Total will be", Amount)

def comp_int_prompts():
      principle = int(input('Enter Initial Amount'))
      rate = (float(input('Enter Rate (%)')))/100
      n_input = (input('Enter compunding period (d for daily, m for monthly, a for anually :)'))
      if    n_input=='a':
             frequency = 1
      elif  n_input=='m':
             frequency = 12
      elif  n_input=='d':
             frequency = 365
      time    = float(input("Enter The Numbers of Years to grow :"))

      compound_interest(principle, rate, frequency, time)

comp_int_prompts()