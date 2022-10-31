import streamlit as st
import pandas as pd
#'https://raw.githubusercontent.com/dataprofessor/data/master/iris.csv'

# ตั้งชื่อ App  เป็น Text ตัวใหญ่
st.title('🎈 Cartoon (LMH)')
# เป็น Text แบบธรรมดา
st.write("Hello Botnoi Voice")

st.sidebar.subheader('Input')
# create input box: st.text_input('ชื่อTitle เหนือbox','ค่าdefult ที่อยากให้แสดง')
url_input = st.sidebar.text_input('URL', '')

#st.subheader('Output')
#st.write('The Github URL of your data is', url_input)
# at.if(ใส่ได้ 1 parameter เท่านั้นจึ่งใช้ f string ช่วย)
#st.warning(f"The Github URL of your data is: {url_input}")

if url_input:
    st.subheader('Output')
    st.warning(f'The Github URL of your data is: {url_input}')
    df = pd.read_csv(url_input)
    st.write(df)
    # check column names ก่อนโดยปริ้นออกมาดู
    column_names = df.columns
    #st.write(column_names[-1])
    # เตรียมข้อมูล และ display bar chart
    df2 = df.groupby(column_names[-1]).mean()
    st.write(df2)
    st.bar_chart(df2)

else:
	st.subheader('Enter your input')
	st.error('👈 Awaiting your input')

