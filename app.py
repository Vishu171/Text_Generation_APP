from langchain.chat_models import AzureChatOpenAI
import openai
import streamlit as st
# Set the OpenAI library configuration using the retrieved environment variables

st.header("AI-Powered Text Generation App")
st.write("I will assist you.....Happy to Help")
# Initialize an instance of AzureChatOpenAI using the specified settings
# chat_llm = AzureChatOpenAI(
#     openai.api_type = st.secrets["AZURE_OPENAI_API_TYPE"],
#    openai.api_base = st.secrets["AZURE_OPENAI_API_BASE"],
#    openai.api_version = st.secrets["AZURE_OPENAI_API_VERSION"],
#    openai.api_key = st.secrets["AZURE_OPENAI_API_KEY"],
#     deployment_name="gpt-4o-batch3"
# )
chat_llm = AzureChatOpenAI(
    openai_api_version=st.secrets["AZURE_OPENAI_API_VERSION"],
    openai_api_key=st.secrets["AZURE_OPENAI_API_KEY"],
    openai_api_base=st.secrets["AZURE_OPENAI_API_BASE"],
    openai_api_type=st.secrets["AZURE_OPENAI_API_TYPE"],
    deployment_name="gpt-4o-batch3"  
)
str_Input = st.text_input("Post Your Queries:")

# Print the response from AzureChatOpenAI for the same question
st.write("AzureOpenAI ChatLLM Response: ", chat_llm.predict(str_Input))
