from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
load_dotenv()
agent = Agent(model=Groq(id="llama-3.2-90b-vision-preview"))

image_url = input("Please enter the URL of the image: ")

# Ensure the URL is valid (basic check)
if image_url.startswith("http://") or image_url.startswith("https://"):
    # Use the provided image URL in the agent response
    agent.print_response(
        "Tell me about this image",
        images=[image_url],
        stream=True,
    )
else:
    print("Invalid URL. Please provide a valid image URL.")