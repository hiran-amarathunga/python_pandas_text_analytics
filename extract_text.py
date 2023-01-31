import re
import pandas as pd

cols=['Name','Age','Country of Origin']     # Columns of output file
occupation_list=['engineer','student','manager','doctor']     # Pre-defined occupation list

#df=pd.DataFrame(columns=cols)
records=[]   # Filtered records from text file
matched_occupations=[]   # Matching occupations from the list and text file

#fh = open(r"sample_text.txt", "r").read()
#match = re.findall("name is\s.*",fh)
with open ('sample_text.txt', 'rt') as myfile:
    for line2 in myfile:
        #print(line2)
        user = re.search('(?<=name\sis\s)(\w+)',line2)  # Extracting name
        #print(user.group())
        country = re.search('(?<=from\s)(\w+)',line2)  # Extracting country
        #print(country.group())
        age = re.search('(\w+\syear\s)(\w+)',line2)  # Extractinf age
        age2=age.group()
        age3=age2.split(" ")
        #print(age3[0])
        records.append([user.group(),age3[0],country.group()])  # Enter into the array list
        #Stats capturing occupation
        lowered_line2=line2.lower()
        for loop_word in occupation_list:
                if loop_word in lowered_line2:
                    matched_occupations.append([user.group(),loop_word])  # Checking matched occupations
                    break
        #End capturing occupation
print(matched_occupations)
df = pd.DataFrame(records, columns=cols)   # Enter array list into pandas dataframe
final=df[::-1]  # Reverse the order
final.to_csv('output_new.csv',index=False) 
final.head()
