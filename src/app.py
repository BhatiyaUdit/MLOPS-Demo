import streamlit as st


def submit(sl, pl, sw, pw):
    print("Clicked", sl, pl, sw, pw)
    pass


st.title("Stream Lit application")

sepal_len = st.number_input("Sepal Length in cm", max_value=8)
petal_len = st.number_input("Petal Length in cm", max_value=8)
sepal_wid = st.slider("Sepal width", min_value=4, max_value=8)
petal_wid = st.slider("Petal width", min_value=4, max_value=8)

# print(sepal_len, petal_len, sepal_wid, petal_wid)

if st.button("Submit for Prediction", on_click=submit, args=(sepal_len,petal_len, sepal_wid, petal_wid)):
    st.write("Predicted Species is:: ", "HELLLLLLL000000000000")


