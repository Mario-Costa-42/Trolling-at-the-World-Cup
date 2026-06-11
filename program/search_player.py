from openai import OpenAI
import re

client = OpenAI(api_key="YOUR_API_KEY")

def find_instagram_username(person_name):
    response = client.responses.create(
        model="gpt-5",
        tools=[{"type": "web_search"}],
        input=f"""
        Find the official Instagram account of the famous person "{person_name}".
        Return ONLY the Instagram username without @, URL, explanation, or extra text.
        If no official account exists, return NOT_FOUND.
        """
    )

    result = response.output_text.strip()

    # Clean possible @ symbol if returned
    result = re.sub(r'^@', '', result)

    return result

if __name__ == "__main__":
    name = input("Famous person: ")
    username = find_instagram_username(name)
    print(username)