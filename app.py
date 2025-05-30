import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Predicción de Partidos", layout="centered")

st.title("🔮 App de Predicción de Fútbol")

team_home = st.text_input("Equipo Local", "Real Madrid")
team_away = st.text_input("Equipo Visitante", "Girona")
avg_home = st.slider("Promedio de goles local", 0.0, 5.0, 2.1)
avg_away = st.slider("Promedio de goles visitante", 0.0, 5.0, 1.3)

if st.button("Predecir"):
    home_goals = np.random.poisson(avg_home, 10000)
    away_goals = np.random.poisson(avg_away, 10000)
    df = pd.DataFrame({"Local": home_goals, "Visitante": away_goals})

    home_wins = (df["Local"] > df["Visitante"]).mean()
    away_wins = (df["Visitante"] > df["Local"]).mean()
    draws = (df["Local"] == df["Visitante"]).mean()
    over_2_5 = (df["Local"] + df["Visitante"] > 2.5).mean()
    btts = ((df["Local"] > 0) & (df["Visitante"] > 0)).mean()

    st.subheader("📊 Predicciones:")
    st.write(f"🔹 Victoria local: {home_wins:.2%}")
    st.write(f"🔹 Empate: {draws:.2%}")
    st.write(f"🔹 Victoria visitante: {away_wins:.2%}")
    st.write(f"🔹 +2.5 goles: {over_2_5:.2%}")
    st.write(f"🔹 Ambos marcan: {btts:.2%}")
