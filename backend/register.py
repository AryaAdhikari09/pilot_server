import streamlit as st
import requests

# Set the base URL for your Node.js server
BASE_URL = 'http://localhost:3000'

# Streamlit app for user registration
st.title('User Registration')

# Register user
st.header('Register')
register_email = st.text_input('Register Email')
register_password = st.text_input('Register Password', type='password')

if st.button('Register'):
    response = requests.post(f'{BASE_URL}/register', json={
        'email': register_email,
        'password': register_password
    })

    if response.status_code == 201:
        st.success('User registered successfully!')
        # Display a button to go to the login page
        if st.button('Go to Login'):
            # Redirect to the login page
            st.experimental_set_query_params(page='login')
    else:
        st.error(response.json().get('message', 'Registration failed.'))
