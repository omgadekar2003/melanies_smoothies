# # Import python packages
# import streamlit as st

# # Write directly to the app
# st.title("🥤 Customize Your Smoothie! 🥤")

# st.write(
#     """Choose the fruits you want in your custom Smoothie!"""
# )

# # Select box for choosing favorite fruit
# option = st.selectbox(
#     'What is your favorite fruit?',
#     ('Banana', 'Strawberries', 'Peaches')
# )

# st.write('Your favorite fruit is:', option)

# #session = get_active_session()
# my_dataframe = session.table("smoothies.public.fruit_options")
# st.dataframe(data=my_dataframe, use_container_width=True)

# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session  # Import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")

st.write(
    """Choose the fruits you want in your custom Smoothie!"""
)

name_on_order = st.text_input("Name on Smoothie:")
st.write("The name on your Smoothie will be: ", name_on_order)
# Select box for choosing favorite fruit
# option = st.selectbox(
#     'What is your favorite fruit?',
#     ('Banana', 'Strawberries', 'Peaches')
# )

# st.write('Your favorite fruit is:', option)



# Initialize the Snowflake session
# Fetch data from the Snowflake table
# Display the data in a dataframe
cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    'Choose up to 5 Ingredients:',my_dataframe, max_selections =5)

if ingredients_list:
    #st.write(ingredients_list)
    #st.text(ingredients_list)
 
    ingredients_string = ''
    
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

    st.write(ingredients_string)
    
# 🥋 Build a SQL Insert Statement & Test It:    
    my_insert_stmt = """
    INSERT INTO smoothies.public.orders (ingredients, name_on_order)
    VALUES ('""" + ingredients_string + """', '""" + name_on_order + """')
"""

    st.write(my_insert_stmt)
   
        
    
#🥋 Insert the Order into Snowflake
    # if ingredients_string:
    #     session.sql(my_insert_stmt).collect()
    #     st.success('Your Smoothie is ordered!', icon="✅")
    time_to_insert = st.button('Submit Order')
   
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success(f'Your Smoothie is ordered,'+name_on_order+'!', icon="✅")
        st.stop()   


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#st.text(fruityvice_response.json())
fv_df=st.dataframe(data=fruityvice_response.json(),use_container_width=True)










