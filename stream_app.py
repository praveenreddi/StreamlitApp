# import streamlit as st
# import requests
# import pandas as pd
# import openai



# openai.api_key = "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"


# def generate_response(user_input):
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=user_input,
#         max_tokens=100,
#         n=1,
#         stop=None,
#         temperature=0.7
#     )
#     return response.choices[0].text.strip()


# if st.button("Save Responses"):
#     responses = []
#     for input_text in st.session_state.user_inputs:
#         response = generate_response(input_text)
#         responses.append(response)
#     df = pd.DataFrame({"User Input": st.session_state.user_inputs, "Bot Response": responses})
#     df.to_csv("responses.csv", index=False)
#     st.success("Responses saved successfully!")


# def main():
#     st.title("ChatGPT Bot")
#     if "user_inputs" not in st.session_state:
#         st.session_state.user_inputs = []
#     user_inputs = st.session_state.user_inputs
#     if st.button("Generate"):
#         response = generate_response(user_input)
#         st.text_area("Bot Response:", value=response, height=200)
#         st.session_state.user_inputs['name'] = 'John'

import streamlit as st
import openai
import pandas as pd

openai.api_key = "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"

st.title("ChatGPT Data Generation Bot")
data = []

user_query = st.text_input("Enter your query:")

if st.button("Generate Data"):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_query,
        max_tokens=100 
    )
    
    generated_data = response.choices[0].text
    
    data.append({"User Query": user_query, "Generated Data": generated_data})
    
    st.write("Generated Data:")
    st.write(generated_data)
if st.button("Save to CSV"):
    df = pd.DataFrame(data)
    df.to_csv("generated_data.csv", index=False)
    st.success("Data saved to generated_data.csv")