import streamlit as st

# Title of the app
st.title("User Information Form")

# Create a form
with st.form(key='user_form'):
    # Input fields
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=0, max_value=120)
    feedback = st.text_area("Feedback")
    
    # Submit button
    submit_button = st.form_submit_button(label='Submit')

# Display the submitted data
if submit_button:
    st.success("Form submitted successfully!")
    st.write("Name:", name)
    st.write("Email:", email)
    st.write("Age:", age)
    st.write("Feedback:", feedback)
