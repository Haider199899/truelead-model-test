import os
from groq import Groq
from dotenv import load_dotenv
# Load environment variables
load_dotenv()
# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def query_llm(selected_model, query, is_streaming):
    try:
        is_streaming = selected_model == "gemma2-9b-it"
        chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": query}
                ],
                model=selected_model,
                stream=is_streaming
        )

        # Display streamed response
        if is_streaming:
                response = ""
                for chunk in chat_completion:
                    if chunk.choices[0].delta.content:
                        response += chunk.choices[0].delta.content
                          # Update in real-time
                return response
    
            # Display normal response
        else:
                return chat_completion.choices[0].message.content
    except Exception as e:
           raise e
    
