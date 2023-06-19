import streamlit
import pandas
import snowflake.connector
import requests

###############################################
# Build Menu
###############################################

streamlit.header('Menu from our Healty Kitchen')
streamlit.text(' 🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# let's put a pick list here so visitor can pick pick fruit they want
fruits_selected = streamlit.multiselect("Pick some fruit:",list(my_fruit_list.index),['Avocado','Strawberries'])
sreamlit.header(fruits_selected)
fruits_to_show =my_fruit_list.loc[fruits_selected]


# Now display  the table on the page
##streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)


streamlit.header('Fruityvice fruit advice')

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
streamlit.text(fruityvice_response.json())
# Make it look prettier
#following line take the semi structurd json file and convert into flat table.
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#dislpay data in tabluar format
streamlit.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)
streamlit.dataframe(my_data_row)

# prompt user to add new food
fruit_to_add = streamlit.text_input('what fruit would you like to add?')
mysql = f"INSERT INTO fruit_load_list (fruit_name)  VALUES ('{fruit_to_add}')"
streamlit.text(mysql)
my_cur.execute(mysql)
streamlit.text(f"Thank for adding {fruit_to_add}")



