import streamlit as st
import random

st.title("🔢 Indovina il Numero")

if 'segreto' not in st.session_state:
    st.session_state.segreto = random.randint(1, 100)
    st.session_state.tentativi = 0

scelta = st.number_input("Inserisci un numero tra 1 e 100", min_value=1, max_value=100, step=1)

if st.button("Verifica"):
    st.session_state.tentativi += 1
    if scelta < st.session_state.segreto:
        st.warning("Troppo basso! ⬇️")
    elif scelta > st.session_state.segreto:
        st.error("Troppo alto! ⬆️")
    else:
        st.success(f"BRAVO! Indovinato in {st.session_state.tentativi} tentativi! 🎉")
        if st.button("Gioca ancora"):
            del st.session_state.segreto
