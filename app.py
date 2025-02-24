import streamlit as st
import uvicorn
from fastapi import FastAPI

app = FastAPI()

st.set_page_config(page_title="Form Generator", layout="centered")

# Apply custom CSS
st.markdown(
    """
    <style>
    .stTextInput {
        border-radius: 10px;
        border: 2px solid rgb(12, 61, 83);
        padding: 8px;
        background-color:rgb(221, 238, 246);
    }
    .stButton>button {
        background-color:rgb(12, 61, 83);
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color:rgb(141, 187, 5);
    }
    .sttitle {
        color:rgb(80, 177, 222);
    }
    </style>
    """,
    unsafe_allow_html=True
)

def generate_form(fields):
    st.write("### Dynamic Form")
    form_data = {}
    for field in fields:
        form_data[field] = st.text_input(f"Enter {field}:")
    if st.button("Submit"):
        st.write("### Submitted Data:")
        st.json(form_data)

st.title("Dynamic Form Generator")
st.write("Gernate your form dynamically ")

fields_input = "Name, Last Name, Age,Email, Education, Skill"
field_list = [f.strip() for f in fields_input.split(",") if f.strip()]
generate_form(field_list)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
