from langchain.chat_models import AzureChatOpenAI
import openai
import streamlit as st
# Set the OpenAI library configuration using the retrieved environment variables
openai.api_type = AZURE_OPENAI_API_KEY
openai.api_base = AZURE_OPENAI_API_BASE
openai.api_version = AZURE_OPENAI_API_VERSION
openai.api_key = AZURE_OPENAI_API_KEY

# Initialize an instance of AzureChatOpenAI using the specified settings
chat_llm = AzureChatOpenAI(
    openai_api_version=OPENAI_API_VERSION,
    openai_api_key=OPENAI_API_KEY,
    openai_api_base=OPENAI_API_BASE,
    openai_api_type=OPENAI_API_TYPE,
    deployment_name="gpt-4o-batch3"
)

str_Input = st.text_input("Write your qusetion")

# Print the response from AzureChatOpenAI for the same question
print("AzureOpenAI ChatLLM Response: ", chat_llm.predict(str_Input)
