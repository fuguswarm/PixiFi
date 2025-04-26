import streamlit as st
from recommender.tool import recommend

# --- Password Gate ---
st.set_page_config(page_title="DeFi Protocol Recommender", layout="wide")
st.title("🔒 Secure Access")

PASSWORD = "maniakugel18"  # <<< Set your password here
password_input = st.text_input("Enter the access password:", type="password")

if password_input != PASSWORD:
    st.warning("Please enter the correct password to access the app.")
    st.stop()

# --- Main App Content ---
st.title("🔍 DeFi Protocol Recommender")
st.markdown("Enter a DeFi project, theme, or keyword like 'liquid staking on Arbitrum' to get enriched real-time protocol info.")

user_input = st.text_input("💬 Your favorite project or theme:")
if st.button("🔎 Recommend"):
    if not user_input:
        st.warning("Please enter a valid prompt.")
    else:
        with st.spinner("Looking for protocols..."):
            result = recommend(user_input)
        st.success("✅ Here are your protocol recommendations:")
        st.markdown(result, unsafe_allow_html=True)
