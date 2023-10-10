import streamlit as st
import pandas as pd
from faker import Faker

fake = Faker()

columns = ['name', 'salary', 'address', 'pincode', 'contact','text']

st.title('Synthetic Data Generator')

st.header('Columns')
st.write(columns)

if st.button('Generate Data'):

  # Generate dataframe
  df = pd.DataFrame(columns=columns, index=range(200))

  for i in range(200):
    df.loc[i, 'name'] = fake.name()
    df.loc[i, 'salary'] = fake.random_int(min=10000, max=100000) 
    df.loc[i, 'address'] = fake.address()
    df.loc[i, 'pincode'] = fake.postcode()
    df.loc[i, 'contact'] = fake.phone_number()
    df.loc[i, 'text'] = fake.text()

  # Download CSV
  st.download_button(
    "Download CSV",
    df.to_csv(),
    file_name='data.csv'
  )

st.info('200 rows of synthetic data generated and downloaded!')
