income = int(input('Enter your company income: '))
costs = int(input('Enter your company costs: '))

if income > costs:
    profit = income - costs
    print(f"Your business is flourishing! Your company income is {profit} dollars.")
elif income < costs:
    loss = costs - income
    print(f"Your business is losing money! Your company loss is {loss} dollars.")
elif income == costs:
    print("Your business has a balance between wins and losses! Congrats!")