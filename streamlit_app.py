import streamlit as streamlit
import pandas as pandas

my_fruit_listreamlit = pandas.read_csv("https://uni-lab-files.s3.us-westreamlit-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfastreamlit Menu')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Eggs')
streamlit.text('🥑🍞 Avocado Toastreamlit')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

streamlit.dataframe(my_fruit_listreamlit)

streamlit.write('Welcome to my parents new healthy diner. We are excited to have you here. Please select your order from the menu below.')

menu = ['Salad', 'Soup', 'Sandwich', 'Burger', 'Pizza']
option = streamlit.selectbox('Menu', menu)

streamlit.write('You selected:', option)

if option == 'Salad':
    streamlit.write('You selected the salad. This is a great choice. It is very healthy and low in calories.')
elif option == 'Soup':
    streamlit.write('You selected the soup. This is a great choice. It is very healthy and low in calories.')
elif option == 'Sandwich':
    streamlit.write('You selected the sandwich. This is a great choice. It is very healthy and low in calories.')
elif option == 'Burger':
    streamlit.write('You selected the burger. This is not a great choice. It is very unhealthy and high in calories.')
elif option == 'Pizza':
    streamlit.write('You selected the pizza. This is not a great choice. It is very unhealthy and high in calories.')

streamlit.write('Thank you for visiting our diner. We hope you enjoyed your meal. Please come again soon.')
