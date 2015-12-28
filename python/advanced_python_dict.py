import csv
import re
import pandas as pd
from collections import defaultdict

def input(file):
    with open(file) as f:
        f = pd.read_csv(file)
        return f



def out_df(f):
    new_cols = ['Name', 'Degree', 'Title', 'Email']
    f.columns = new_cols
#     print(f)
    
    new_name_list = []
    for name in f['Name']:
        name = name.split()
        new_name_list.append(name[-1])
        
    new_title_lst = []
    for title in f['Title']:
        title = title.split()
        if len(title) == 4:
            new_title_str = ' '.join(title[:2])
            new_title_lst.append(new_title_str)
        if len(title) == 3:
            new_title_str = ''.join(title[0])
            new_title_lst.append(new_title_str)
            
    f['Title'] = new_title_lst
    more_cols = ['Name', 'Degree', 'Title', 'Email']
    f.columns = more_cols
    f = f.set_index('Name')
    final_dict = defaultdict(list)
    for keys, values in f.items():
        keys = keys.split()
        keys = (keys[-1], keys[0])
        final_dict[keys].append(values.values())
    print(final_dict)

    
    
def main():
    file = 'faculty.csv'
    input(file)
    f = input(file)
    print(out_df(f))

    
if __name__ == '__main__':
    main()
