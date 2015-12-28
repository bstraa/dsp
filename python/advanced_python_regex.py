import csv
import re
import pandas as pd
from collections import defaultdict

'''Completed 05b -python-advanced.md'''

def inpt(file):
    with open(file) as f:
        f = pd.read_csv(f)
        return f


def diffDegrees(dataf):
    cols = dataf.columns    
    degree = dataf[' degree']
    degree_dict = defaultdict(int)
    for d in degree:
        d = d.replace('.', '')
        d = d.lower().split()
        # print(d)
        for item in d:
            # print(item)
            degree_dict[item] += 1
    #     if d not in degree_dict.items():
    #         degree_dict[d] = 1
    #     elif d in degree_dict.items():
    #         degree_dict[d] += 1
    for k, v in degree_dict.items():
        print k, v
    print('length of dict: {}'.format(len(degree_dict)))
    
    # degree.replace('.', '')
    # for line in degree:
    #     line = line.translate(None, '.')

    
def diffTitles(dataf):
    title = dataf[' title']
    title_dict = defaultdict(int)
    for t in title:
        title_dict[t] += 1
    for k, v in title_dict.items():
        print(k, v)

def emailList(dataf):
    email = dataf[' email']
    email = [e for e in email]
    match_list = set()
    for item in email:
        match = re.search('@\S+', item)
        if match:
            # print match.group()
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

def createDicts(dataf):
    print(dataf)
    faculty_dict = {}
    last_name_lst = []
    name = dataf['name']
    for person in name:
        person = person.split()
        last_name = person[-1]
        last_name_lst.append(last_name)
    dataf['last_name'] = last_name_lst
    last_name = dataf['last_name']

    dataf.set_index('last_name').to_dict()
    print dataf
                
    
    
def main():
    file = 'faculty.csv'
    dataf = inpt(file)
    diffDegrees(dataf)
    diffTitles(dataf)
    emailList(dataf)
    email = emailList(dataf)
    writeToCSV(email)
    createDicts(dataf)
    
if __name__ == '__main__':
    main()
