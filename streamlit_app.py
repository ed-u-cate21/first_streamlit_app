# packages to import
import streamlit 

#Adding the title 
streamlit.title('My Mom\'s Healthy New Diner')

# Build the menu items
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 4 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
import pandas 

# Build a fruit chart from csv on aws
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


#Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)


#New section to display the fruityvice API response 
streamlit.header('Fruityvice Fruit Advice')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")


## Clean the text up for normalized text display
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Creates the results into a dataframe table
streamlit.dataframe(fruityvice_normalized)
