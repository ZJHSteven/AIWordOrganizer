from litellm import completion

response = completion(
    model="gemini/gemini-2.0-flash", 
    messages=[{"role": "user", "content": "write code for saying hi from LiteLLM"}]
)
print(response.choices[0].message.content)