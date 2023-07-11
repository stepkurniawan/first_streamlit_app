import streamlit as st

st.title('My Parents New Healthy Diner')

st.header('Breakfast Menu')

st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Eggs')
st.text('🥑🍞 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

st.write('Welcome to my parents new healthy diner. We are excited to have you here. Please select your order from the menu below.')

menu = ['Salad', 'Soup', 'Sandwich', 'Burger', 'Pizza']
option = st.selectbox('Menu', menu)

st.write('You selected:', option)

if option == 'Salad':
    st.write('You selected the salad. This is a great choice. It is very healthy and low in calories.')
elif option == 'Soup':
    st.write('You selected the soup. This is a great choice. It is very healthy and low in calories.')
elif option == 'Sandwich':
    st.write('You selected the sandwich. This is a great choice. It is very healthy and low in calories.')
elif option == 'Burger':
    st.write('You selected the burger. This is not a great choice. It is very unhealthy and high in calories.')
elif option == 'Pizza':
    st.write('You selected the pizza. This is not a great choice. It is very unhealthy and high in calories.')

st.write('Thank you for visiting our diner. We hope you enjoyed your meal. Please come again soon.')
