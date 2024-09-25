import streamlit as st
import pandas as pd
import math 

st.write("""
# Jogo das placas
""")

def quadradoPerfeito(n):
    return math.floor(math.sqrt(n))**2 == float(n)

def palindromo(n):
    return str(n) == str(n)[::-1]

def calculaPontuacao(placa):
    points = placa
    if quadradoPerfeito(placa):
        st.info('Quadrado Perfeito! +5 pontos', icon=":material/thumb_up:")
        points += 5
    if palindromo(placa):
        st.info('Palindromo! +3 pontos', icon="ℹ️")
        points += 3
    st.title(points)


st.text_input("Insira o número da placa", key="placa")
if st.button("Calcular pontuação"):
    calculaPontuacao(int(st.session_state.placa))