import streamlit as st

# Components
st.header("This is Header")
st.text("this is text")
st.markdown('''
```python
print('Hello World')
```            
''')

st.markdown('''
```sql
select * from student
```            
''')

st.success('Data was saved successully ')
st.info('Data was saved successully ')
st.warning('Data was saved successully ')
st.error('Data was saved successully ')


# image
img_path = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png"
st.image(img_path , width=250)

# form
# st.checkbox("Show/Hide")
# st.radio("Select Gender : ",('Male','Female'))

# form action
if st.checkbox("Show/Hide"):
    st.text('Show the text')

gender = st.radio("Select Gender : ",('Male','Female'))
if gender == 'Male':
    st.success("Male")
else:
    st.info('Female')


# form select
st.selectbox("Programming Languages",["python","js","php","ruby"])
st.multiselect("Programming Languages",["python","js","php","ruby"])