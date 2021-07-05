import csv 

def saveAsCSV(items): # Comma-Separated Values, CSV 
  with open('data.csv', newline='', mode='a') as data:
    item1 = items["item1"]
    item2 = items["item2"]
    writer = csv.writer(data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)  
    writer.writerow([item1, item2])