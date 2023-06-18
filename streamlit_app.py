import streamlit
import pandas
streamlit.header('reakfast Menu')
streamlit.text(' 🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

streamlit.header('Fruityvice fruit advice')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
# Make it look prettier
#following line take the semi structurd json file and convert into flat table.
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#dislpay data in tabluar format
streamlit.dataframe(fruityvice_normalized)

streamlit.header('Fruityvice Fruit advice!')
fruit_choice = streamlit.text_input('what would you like information about?','kiwi')
streamlit.write('The user entered',fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)





