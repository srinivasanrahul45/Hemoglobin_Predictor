# To Create dummy date (use in case of inavilability of data) 

import random

start = [11, 5 ,2006]
end = [4, 12, 2010]
interval = [20, 26, 23, 19, 29]

def giveDate(previous):
    inter = random.choice(interval)
    previous[0] = previous[0] + inter
    if previous[0] > 30:
        previous[0] = previous[0] - 30
        previous[1] = previous[1] + 1
    if previous[1] > 12:
        previous[1] = previous[1] - 12
        previous[2] = previous[2] + 1
    if previous[0] <= 0:
        previous[0] = 1
    if previous[1] <= 0:
        previous[1] = 1
    return previous
    

with open("Date.csv", "a") as file:
    while start[2] <= 2012:
        start = giveDate(start)
        file.writelines(f"{start[0]},{start[1]},{start[2]}\n")
        
    file.close()