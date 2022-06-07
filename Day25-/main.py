from unittest.mock import patch
import pandas as pd
import os
import pathlib


p = pathlib.Path(__file__).parent.absolute()

new_path = os.path.join(p, "2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")

data = pd.read_csv(new_path)
data = data.get('Primary Fur Color') 
print(type(data))
fur_color = data.groupby(['Primary Fur Color']).count()

//*[@id="mount_0_0_lu"]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div

print(fur_color)

# print(data[data['Primary Fur Color'] == "Gray"])
# print(data[data['Primary Fur Color'] == "Black"])
# print(data[data["Primary Fur Color"] == "Cinnamon"])



##################
#color  # count