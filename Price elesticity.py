import pandas as pd
data = pd.DataFrame({"Demand": [20, 30, 31, 33, 30, 33, 35], 
                     "Price": [2000, 1800, 1850, 1700, 1800, 1700, 1600]})
print(data)

data["% Change in Demand"] = data["Demand"].pct_change()
data["% Change in Price"] = data["Price"].pct_change()
print(data)

data["Price Elasticity"] = data["% Change in Demand"] / data["% Change in Price"]
print(data)
