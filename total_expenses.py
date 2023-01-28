import json
# Calculate the total expenses
def total_expenses(monthly_expenses: dict) -> int:
    """
    Calculate the total expenses
    Args:
        monthly_expenses: dictionary of monthly expenses
    Returns:
        total_expenses: total expenses
    """
    
    n=0
    for i in y.values():
        n+=i

    return n
f=open('data.json', mode='r')
f=f.read()
y=json.loads(f)
print(total_expenses(y))
