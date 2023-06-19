import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

def  get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized
   
#Allow the end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
      mysql = f"INSERT INTO fruit_load_list (fruit_name)  VALUES ('{new_fuit}')"
      my_cur.execute(mysql)
      return "thanks for addming" +new_fruit

      
def  get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
      my_cur.execute("select * from fruit_load_list")
      return my_cur.fetchall()


###############################################
# Build Menu
###############################################

streamlit.header('Menu from our Healty Kitchen')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# let's put a pick list here so visitor can pick pick fruit they want
fruits_selected = streamlit.multiselect("Pick some fruit:",list(my_fruit_list.index),['Avocado','Strawberries'])
streamlit.header('List of fruits you have selected so far:')
fruits_to_show =my_fruit_list.loc[fruits_selected]

# Now display  the table on the page
streamlit.dataframe(fruits_to_show)

  
#New section to display fruityvice api response
streamlit.header('Fruityvice Fruit advice!')
try:
  fruit_choice = streamlit.text_input('what would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function =get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
   streamlit.error()


streamlit.header('The Fruit load list contains')
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)
# Allow the end user to add a fruit to the list

add_my_fruit =streamlit.text_input('What fruit youw you like to add?')
if streamlit.button('Add a fruit to the list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function  = insert_row_snowflake(add_my_fruit)
   streamlit.text(back_from_function)





