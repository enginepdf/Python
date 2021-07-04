import csv 

def saveAsCSV(data): # Comma-Separated Values, CSV 
  with open('data.csv', newline='', mode='a') as data:
    item1 = data["item1"]
    item2 = data["item2"]
    writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)  
    writer.writerow([item1, item2])