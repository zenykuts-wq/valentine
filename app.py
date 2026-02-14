import streamlit as st
import random

st.set_page_config(page_title="Важливе питання ❤️", page_icon="💖")

st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3.5em;
        font-size: 1.2rem;
        font-weight: bold;
    }
    /* Стиль для кнопки ТАК */
    div.stButton > button:first-child {
        background-color: #ff4d6d;
        color: white;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("У мене є до тебе питання... 🥰")

if 'accepted' not in st.session_state:
    st.session_state.accepted = False

if not st.session_state.accepted:
    st.image("https://i.pinimg.com/originals/d0/95/8a/d0958a757cbe2dbd3ae0fc8f2abf1813.gif")
    
    st.subheader("Ти будеш моїм валентином? ❤️")
    
    col1, col2 = st.columns(2)

    with col1:
        if st.button("ТАК! ✨"):
            st.session_state.accepted = True
            st.rerun()

    with col2:
        no_texts = ["Ні", "Впевнений?", "Нітуда попі", "Узясь попі", "Ніт"]
        
        if st.button(random.choice(no_texts)):
            st.toast("Ой, кнопка зламалася, спробуй іншу! 😂")

else:
    st.balloons() 
    st.success("УРААА! Я знала! ❤️❤️❤️")
    
    st.image("https://i.pinimg.com/originals/47/76/2f/47762f6dd3cbc225eb7edd98d15e7950.gif")
    
    st.markdown("### Офіційно: ти мій найкращий Валентин! 😘")
    
    if st.button("Почати спочатку 🔄"):
        st.session_state.accepted = False
        st.rerun()