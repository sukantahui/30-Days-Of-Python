# streamlit run streamlitDemo.py

import streamlit as st
import numpy as np

st.title('Learn using GUI')
A = np.array([[3, 6, 7], [5, -3, 0]])
B = np.array([[1, 1], [2, 1], [3, -3]])
C = A.dot(B)
st.write("Array A")
st.dataframe(A)

st.write("Array B")
st.dataframe(B)

if st.checkbox('Show Multipication'):
    st.subheader('AxB')
    st.write(C)

X = np.array([[2, 4], [5, 16]])
Y = np.array([[9, 13], [3, 6]])
Z = X + Y     

st.write("X") 
st.dataframe(X)
st.write("Y") 
st.dataframe(Y)
if st.checkbox('Show Addition'):
    st.subheader('X+Y')
    st.write(Z)
    
A = np.array([[1, 1], [2, 1], [3, -3]])
print("Before Transpose")
print(A)
print("After Transpose")
print(A.transpose())

b = np.array([[6,1,1], [4, -2, 5], [2,8,7]]) 
st.dataframe(b)
st.write(np.linalg.det(b))
st.write("6X(-2X7 - 5X8) - 1X(4X7 - 5X2) + 1X(4X8 - -2X2)")

a = np.array([[1,1,1],[0,2,5],[2,5,-1]]) 
st.write(a)
ainv = np.linalg.inv(a) 
st.write(ainv)

row = st.text_input('Row Height')
st.write('The current movie title is', row)