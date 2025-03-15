import streamlit as st
import requests

# Backend API URL (Replace with your Render API)
API_URL = "https://cybersecurity-bot-9a85.onrender.com"

st.title("🛡️ Cybersecurity Awareness Bot")
st.write("Ask me anything about cybersecurity!")

# Input box for user query
user_query = st.text_input("Type your question here:")

if st.button("Get Advice"):
    if user_query:
        response = requests.post(API_URL, json={"query": user_query}).json()
        st.write("🛠️ **Bot's Advice:**")
        st.success(response.get("response", "Error fetching response."))
    else:
        st.warning("Please enter a question.")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)),debug=True)
