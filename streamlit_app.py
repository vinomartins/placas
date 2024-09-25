import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
 
def calculaPontuacao(placa):
    return 'teste'

st.text_input("Insira o número da placa", key="placa")
if st.button("Calcular pontuação"):
    calculaPontuacao(int(st.session.placa))