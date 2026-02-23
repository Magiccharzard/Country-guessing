import streamlit as st
import random

st.set_page_config(page_title="Guess The Country", page_icon="🌍")

st.title("🌍 Guess The Country Game")

# -----------------------------
# Country Data
# -----------------------------
countries = {
    "Easy": [
        {"name": "United States", "hint": "Located in North America."},
        {"name": "France", "hint": "Home of the Eiffel Tower."},
        {"name": "Japan", "hint": "Island nation in East Asia."},
        {"name": "Brazil", "hint": "Largest country in South America."}
    ],
    "Medium": [
        {"name": "Hungary", "hint": "Landlocked country in Central Europe."},
        {"name": "Thailand", "hint": "Famous for Bangkok and tropical beaches."},
        {"name": "Peru", "hint": "Home to Machu Picchu."},
        {"name": "Norway", "hint": "Known for fjords."}
    ],
    "Hard": [
        {"name": "Kyrgyzstan", "hint": "Mountainous country in Central Asia."},
        {"name": "Slovenia", "hint": "Small European country near Italy and Croatia."},
        {"name": "Benin", "hint": "West African country on the Gulf of Guinea."},
        {"name": "Laos", "hint": "Landlocked country in Southeast Asia."}
    ]
}

# -----------------------------
# Difficulty Selection
# -----------------------------
difficulty = st.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"])

# -----------------------------
# Initialize Game State
# -----------------------------
if "secret_country" not in st.session_state:
    st.session_state.secret_country = None
    st.session_state.hint = ""
    st.session_state.attempts = 0
    st.session_state.game_over = False

# -----------------------------
# Start Game Button
# -----------------------------
if st.button("Start New Game"):
    chosen = random.choice(countries[difficulty])
    st.session_state.secret_country = chosen["name"]
    st.session_state.hint = chosen["hint"]
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.rerun()

# -----------------------------
# Game Logic
# -----------------------------
if st.session_state.secret_country and not st.session_state.game_over:

    st.write("💡 Hint:", st.session_state.hint)

    guess = st.text_input("Enter your guess:")

    if st.button("Submit Guess"):
        st.session_state.attempts += 1

        if guess.strip().lower() == st.session_state.secret_country.lower():
            st.success(
                f"Correct! 🎉 It was {st.session_state.secret_country}. "
                f"You guessed it in {st.session_state.attempts} attempts!"
            )
            st.session_state.game_over = True
        else:
            st.warning("Not correct. Try again!")

# -----------------------------
# Play Again
# -----------------------------
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.secret_country = None
        st.session_state.hint = ""
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.rerun()
