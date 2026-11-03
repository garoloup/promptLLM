import base64
import os
from langchain_openai import ChatOpenAI
 
 
# Clé API pour l'accès aux modèles de langage
api_key = 'dummy_for_ollama'
# defini dans var env OPENAI_API_KEY
 
prompt = """ Comment compiler en c++ ? """
 
def encode_image(image_path):
    """Encode the image to base64."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
 
# Path to your image
# image_path = r'maquettes_templates_LEGOS\JPEG\Splash screen.jpg'
 
# Getting the base64 string
#base64_image = encode_image(image_path)
 
# # Define the messages for the chat
# messages_pix = [
#     {
#         "role": "user",
#         "content": [
#             {"type": "text", "text": "What's in this image?"},
#             {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
#         ]
#     }
# ]
 
# Define the messages for the chat
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": f"{prompt}"},
        ]
    }
]
 
# Utilisation du modèle ChatOpenAI pour une autre analyse
openAI_model = ChatOpenAI(
#    model="gpt-5-mini",
#    model="llama3.2",
    model="gemma4:e4b",
#    model="gemini-flash-latest",
    streaming=False,
    # base_url="https://api.openai.com/v1", # valeur par defaut pour OpenAI
    base_url="http://localhost:11434/v1", # valeur par defaut pour Ollama
    #base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    #api_key=os.environ["GEMINI_API_KEY"],

    temperature=0,
    api_key=api_key
)


 
# Make the request to the ChatOpenAI model
response = openAI_model.invoke(
    input=messages
)
 
# Check the response
if not response.content:
    print("Request failed")
 
print(response.content)
 