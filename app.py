from langchain.chat_models import AzureChatOpenAI
import openai


# # Retrieve Azure OpenAI specific configuration from environment variables
# OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
# OPENAI_API_TYPE = os.getenv("AZURE_OPENAI_API_TYPE")
# OPENAI_API_BASE = os.getenv("AZURE_OPENAI_API_BASE")
# OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

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
    deployment_name="testing"  
)

# Print the response from AzureChatOpenAI for the same question
print("AzureOpenAI ChatLLM Response: ", chat_llm.predict("what is the weather in mumbai today?"))
