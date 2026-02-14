import streamlit as st
import random

# Налаштування сторінки (те, що відображається на вкладці браузера)
st.set_page_config(page_title="Важливе питання ❤️", page_icon="💖")

# Стилізація кнопок через CSS
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

# Головний заголовок
st.title("У мене є до тебе питання... 🥰")

# Використовуємо session_state, щоб зафіксувати відповідь
if 'accepted' not in st.session_state:
    st.session_state.accepted = False

if not st.session_state.accepted:
    # Гіфка з котиком або серцем перед питанням
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHYxcXNsc3JpZXR3eXJmZHZ4eG55eHh4eHh4eHh4eHh4eHh4eHgmZXA9djFfaW50ZXJuYWxfZ2lmX2J5X2lkJmN0PXM/3ov9jS6vH7heL97p7O/giphy.gif")
    
    st.subheader("Ти будеш моїм валентином? ❤️")
    
    col1, col2 = st.columns(2)

    with col1:
        if st.button("ТАК! ✨"):
            st.session_state.accepted = True
            st.rerun()

    with col2:
        # Список жартівливих відповідей для кнопки "Ні"
        no_texts = ["Ні", "Впевнений?", "Нітуда попі", "Узясь попі", "Ніт"]
        
        # Кожне натискання на "Ні" просто випадково змінює текст на кнопці
        if st.button(random.choice(no_texts)):
            st.toast("Ой, кнопка зламалася, спробуй іншу! 😂")

else:
    # Екран після натискання "ТАК"
    st.balloons() # Запуск віртуальних кульок на весь екран
    st.success("УРААА! Я знала! ❤️❤️❤️")
    
    # Святкова гіфка
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHYxcXNsc3JpZXR3eXJmZHZ4eG55eHh4eHh4eHh4eHh4eHh4eHgmZXA9djFfaW50ZXJuYWxfZ2lmX2J5X2lkJmN0PXM/KztT2c4u8mYYUiCi7W/giphy.gif")
    
    st.markdown("### Офіційно: ти мій найкращий Валентин! 😘")
    
    if st.button("Почати спочатку 🔄"):
        st.session_state.accepted = False
        st.rerun()