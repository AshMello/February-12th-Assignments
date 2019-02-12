tip_percent = int(input('Enter a tip percentage '))
total = int(input('Enter your total '))
def tip_calculator(x, y):
    return  (x*y) / 100
total_tip = tip_calculator(tip_percent, total)
print(total_tip)