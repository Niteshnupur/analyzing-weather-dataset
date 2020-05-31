# --------------
# Instructions

# Different functions that you would require to define for this project has been mentioned in the code block. All the parameters and the task, a function would do, have been mentioned there.


#Importing the modules
import pandas as pd
import numpy as np
from scipy.stats import mode 



# Load the weather_2012 data csv file and store it in weather variable. The path of the dataset has been stored in the variable path for you.


weather = pd.read_csv(path)

print(weather.head(5))



# Check the categorical and numerical variables. You can check it by calling categorical and numerical functions.

weather.select_dtypes("object").columns

print(weather.dtypes)

print(weather.select_dtypes("object"))


# for numerical variables

print(weather.select_dtypes("float"))


print(weather.select_dtypes("int"))

weather["Wind Spd (km/h)"].unique()


# Check the distribution of a specific value like the number of times the weather was exactly Cloudy in the given column. Feel free to check on other values. You can check it by calling the function clear with respective parameters.

weather["Weather"].value_counts()['Clear']


weather["Weather"].value_counts()['Cloudy']


# Find the number of times when the wind speed was exactly 4 km/h

weather["Wind Spd (km/h)"].value_counts()[4]




# By using the index of the value or name of the value you can check the number of counts. Now suppose you want to check some instances based on a specific condition like when the wind speed was above 35 and visibility was 25. You can directly check it by calling the function instances_based_condition with respective parameters and store the resulting dataframe in wind_speed_35_vis_25.

wind_speed_35_vis_25 = weather[(weather['Wind Spd (km/h)'] > 35) & (weather['Visibility (km)']== 25)]

print(wind_speed_35_vis_25)


# You have temperature data and want to calculate the mean temperature recorded by month. You can generate a pivot table that contains the aggregated values(like mean, max, min, sum, len) recorded by month. 

#You can call the function agg_values_ina_month with respective parameters.


weather['Date/Time'] = pd.to_datetime(weather['Date/Time'])

mean_dew_temperature = weather.pivot_table(values='Dew Point Temp (C)', index=weather['Date/Time'].dt.month, aggfunc=np.mean)

print(mean_dew_temperature)


# To groupby based on a column like you want to groupby on Weather column and then aggregate the mean values of each column for different types of weather using mean. 
# You can call the function group_values and store the resulting dataframe in mean_weather. Feel free to try on different aggregated functions like max, min, sum, len


mean_weather = weather.groupby("Weather").agg(np.mean)

print(mean_weather)






