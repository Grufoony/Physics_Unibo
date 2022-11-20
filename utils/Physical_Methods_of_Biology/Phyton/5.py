import numpy as np

n = 100

doors = [0, 1, 0] # 0 is no good, 1 is good

win_without_switch = 0
win_with_switch = 0

for i in range(n):
    np.random.shuffle(doors)
    initial_choice = np.random.choice(doors)
    if doors[initial_choice] == 1:
        win_without_switch += 1
    else:
        win_with_switch += 1

percentage_without_switch = win_without_switch / n * 100
percentage_with_switch = win_with_switch / n * 100
print("Win without switch: %5.2f" % percentage_without_switch)
print("Win with switch: %5.2f" % percentage_with_switch)