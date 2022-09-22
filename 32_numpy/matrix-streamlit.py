# streamlit run streamlitDemo.py

import streamlit as st
import numpy as np

col1, col2 = st.columns([3, 1])

with col1:
    st.subheader('A matrix is a rectangular arrangement of numbers into rows and columns.')

with col2:
    st.subheader("Matrix A")
    A = np.array([[3, 6, 7], [5, -3, 0]])
    st.dataframe(A)
    st.write('For example, matrix A has two rows and three columns.')
    
st.markdown("""---""")

col1, col2 = st.columns([3, 1])
with col1:
    st.subheader("Matrix Multipication")
    A = np.array([[3, 6, 7], [5, -3, 0]])
    B = np.array([[1, 1], [2, 1], [3, -3]])
    C = A.dot(B)
    st.write("Matrix A")
    st.dataframe(A)
    st.write("Matrix B")
    st.dataframe(B)
with col2:
    st.write("A x B")
    st.dataframe(C)  
st.markdown("""---""")    

col1, col2 = st.columns([3, 1])
with col1:
    st.subheader("Negative of Matrix")
    A = np.array([[3, 6, 7], [5, -3, 0]])
    C = np.negative(A)
    st.write("Matrix A")
    st.dataframe(A)
with col2:
    st.write("Negative of A")
    st.dataframe(C)      


