import streamlit as st

# st.write("Hello world")

st.title("Hello Streamlit-er 👋")
k = st.text_input("Enter your prompt: ")
print(k)

if k:
    st.title(f'Hi {k}, Welcome to Streamlit!!')

st.markdown(
    """ 
    This is a playground for you to try Streamlit and have fun. 

    **There's :rainbow[so much] you can build!**
    
    We prepared a few examples for you to get started. Just 
    click on the buttons above and discover what you can do 
    with Streamlit. 
    """
)

if st.button("Send balloons!"):
    st.balloons()



















