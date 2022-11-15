
import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
# Read the airline data into pandas dataframe


airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv',
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

print('Data downloaded and read into a dataframe!')

print(airline_data.head())
print("shape are as follows")
print(airline_data.shape)
print("data samples are as follows")
data = airline_data.sample(n=500, random_state=42)
print("Executed well")
print(data.shape)
print(type(airline_data.columns))

df_sample = data.sample(n=500)

print("SCATTER")
plt.scatter('Year', 'ArrDelay', data=df_sample)
plt.xlabel('Year')
plt.ylabel('Arrival Delay')
print(plt.show)

