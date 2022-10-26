
# writing a csv file
import csv
import pandas as pd
data = {"Name": ["A", "D", "C", "S", "K"], 
        "Age": [23, 21, 25, 23, 22]}
data = pd.DataFrame(data)
data.to_csv("age_data.csv", index=False)
print(data.head())


# reading a csv file
import pandas as pd
data = pd.read_csv("age_data.csv")
print(data.head())
