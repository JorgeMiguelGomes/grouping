# -*- coding: utf-8 -*-

# import libraries 

import pandas as pd 

# Read CSV file and assign it to 

df = pd.read_csv("sample_csv.csv") # See Read.me for structure


print(df.info()) #optional 

# Sort list members by groups. Change 'Sector' for the name of the column in your csv file

sorting = (df.groupby('sector').pipe(lambda d: d.sample(frac=1))
   .assign(group=lambda d: d.groupby('sector').cumcount().add(1))
   .sort_values(by=['group', 'sector']) 
	)


print(sorting) #optional

# Save to CSV

sorting.to_csv("sample_final_result.csv")