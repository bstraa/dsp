import csv
import re
import pandas as pd

def inpt(file):
    with open(file) as f:
        f = pd.read_csv(f)
        return f

def emailList(dataf):
    email = dataf[' email']
    email = [e for e in email]
    match_list = set()
    for item in email:
        match = re.search('@\S+', item)
        if match:
            match_list.add(match.group())
    print match_list
    return email
    
def writeToCSV(email):
    out = ''
    for e in email:
        out += e + '\n'
    email = [out]
    with open('emails.csv', 'wb') as outcsv:
        wr = csv.writer(outcsv)
        wr.writerow(email)

def main():
    file = 'faculty.csv'
    dataf = inpt(file)
    emailList(dataf)
    email = emailList(dataf)
    writeToCSV(email)
    
if __name__ == '__main__':
    main()
