# Python Script to convert date in .csv to date format of MS Excel 

data = ""

with open("ToConvert.csv", "r") as file:
    data = file.read()
    print(data)
    file.close()
    
with open("ConvertedToDate.txt", "w") as file2:
    file2.write(data.replace(",","-"))
    file2.close()