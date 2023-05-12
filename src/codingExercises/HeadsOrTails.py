import random

while True:
    quarter = random.randint(1, 2)
    quarter_side = ''
    if quarter == 1:
        quarter_side = 'Heads'
    elif quarter == 2:
        quarter_side = 'Tails'
    print(quarter_side)