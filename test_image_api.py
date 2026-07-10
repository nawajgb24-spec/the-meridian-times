import os

from google import genai


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("=" * 60)
print("Testing Gemini Image Generation...")
print("=" * 60)

try:

    response = client.models.generate_images(
        model="gemini-2.5-flash-image",
        prompt="A cinematic newspaper style image of a modern city skyline at sunrise"
    )

    print("SUCCESS")
    print(type(response))

except Exception as e:

    print("FAILED")
    print(e)
