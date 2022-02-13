income = int(input('Enter your company income: '))
costs = int(input('Enter your company costs: '))

if income > costs:
    profit = income - costs
    profitability = profit / income
    print(f"Your business is flourishing! Your company income is {profit} dollars and profitability is {profitability:.2f}.")
    staff = int(input('How many employees does your business have? '))
    profit_per_person = profit / staff
    print(f"It's {profit_per_person:.2f} dollars for a person!")
elif income < costs:
    loss = costs - income
    print(f"Your business is losing money! Your company loss is {loss} dollars.")
elif income == costs:
    print("Your business has a balance between wins and losses! Congrats!")