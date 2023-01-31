import pandas as pd

new_text_file=[]  # Array list of final data format
over_30_years=[]  # Array list of members over 30 years
over_30_years.append("----------------------------")
over_30_years.append("Members over 30 years of age")
over_30_years.append("----------------------------")
asian_countries_list=['Malaysia','Thailand','India','Cambodia','Indonesia']
asian_countries=[]  # Matched asian countries
asian_countries.append("----------------------------")
asian_countries.append("Members from Asian Countries")
asian_countries.append("----------------------------")
unmatched_occupations=[]  # Unmatched occupations from previous list
unmatched_occupations.append("----------------------")
unmatched_occupations.append("Exceptions: Occupation")
unmatched_occupations.append("----------------------")

new_df = pd.read_csv('output_csv.csv')  # Read edited .csv file
new_df.head()

# Function to left align data text
def make_lalign_formatter(df, cols=None):
    if cols is None:
       cols = df.columns[df.dtypes == 'object'] 
    return {col: f'{{:<{df[col].str.len().max()}s}}'.format for col in cols}

# Creating sentences
for i in range(0,len(new_df.index)):
    #print(new_df.iloc[i,0])
    new_text_file.append("My occupation is "+str(new_df.iloc[i,3])+", My name is "+str(new_df.iloc[i,0])+", I am from "+str(new_df.iloc[i,2])+", I am "+str(new_df.iloc[i,1])+" year old.")
    print(new_text_file[i])
    if(new_df.iloc[i,1]>=30):
        over_30_years.append(new_df.iloc[i,0])   # Check over 30 year members
    if new_df.iloc[i,2] in asian_countries_list:
        asian_countries.append(new_df.iloc[i,0])   # Check asian countries list
    for m in range (0,len(matched_occupations)):   # Check occupations from previous list and newly entered one
        if ((new_df.iloc[i,0]==matched_occupations[m][0]) and (new_df.iloc[i,3]!=matched_occupations[m][1])):
                    unmatched_occupations.append("Member "+str(new_df.iloc[i,0])+" is a "+str(matched_occupations[m][1])+", but entered "+str(new_df.iloc[i,3])+" as occupation.")
for j in range (0,len(over_30_years)):
    print(over_30_years[j])
for k in range (0,len(asian_countries)):
    print(asian_countries[k])
for n in range (0,len(unmatched_occupations)):
    print(unmatched_occupations[n])
new_df=pd.DataFrame(new_text_file)
#new_df.head()
with open('output_text_final.txt', 'w') as final_text:
    dfAsString = new_df.to_string(header=False, index=False, formatters=make_lalign_formatter(new_df), justify='left')
    final_text.write(dfAsString)  # Write final text file
