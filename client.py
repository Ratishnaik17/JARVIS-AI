'''from openai import OpenAI
client= OpenAI(
    api_key="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"
)
completion= client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ]
)
print(completion.choices[0].message.content)'''
import google.generativeai as genai

try:
    # Configure the API key
    genai.configure(api_key="AIzaSyBGIVpoBoqBAgiRbEEJAof9XMrxk-ZJ14g")

    # Create a model instance
    model = genai.GenerativeModel('gemini-2.0-flash')

    # Generate the response
    response = model.generate_content("Explain how AI works in a few words")

    # Print the response
    print(response.text)

except Exception as e:
    print(f"An error occurred: {str(e)}")