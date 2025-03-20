import streamlit as st
from src.llm.llm_service import query_llm

# Available models
models = ["gemma2-9b-it", "llama-3.3-70b-versatile", "mistral-saba-24b", "deepseek-r1-distill-llama-70b"]

# Streamlit UI
st.title("Model testing App")
st.write("Select a model, enter your query, and get a response!")

# Model selection
selected_model = st.selectbox("Choose a model:", models)

# User input for query
query = st.text_area("Enter your query:")

# Submit button
if st.button("Get Response"):
    if not query.strip():
        st.warning("Please enter a query!")
    else:
        st.write(f"### Response from {selected_model}:")
        
        try:
            is_streaming = selected_model == "gemma2-9b-it"
            with st.spinner("⏳ Processing..."):
                 response = query_llm(selected_model,query,is_streaming)
            st.write(response)
            st.success("✅ Response completed!")

        except Exception as e:
            st.error(f"⚠️ Error: {e}")

