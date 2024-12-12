import openai

openai.api_key = "Azure_Openai_Key"
openai.api_type = 'azure'
openai.api_version = "2023-05-15"
openai.api_base = "https://ai-upskilling.openai.azure.com/"
deployment_name = "gpt-4o-batch3"

# add your completion code
prompt = "Complete the following: Once upon a time there was a"
messages = [{"role": "user", "content": prompt}]

# make completion
completion = client.chat.completions.create(model='text-embedding-batch3', messages=messages)

# print response
print(completion.choices[0].message.content)
