import openai

def generate_script(topic, api_key):
    openai.api_key = api_key

    prompt = f"""Create an engaging YouTube video script (approx. 200 words) on the topic: "{topic}". 
Use a hook, informative body, and a strong closing. Keep it conversational and interesting."""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a YouTube scriptwriter."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.8
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        print("Script generation error:", e)
        return "Script generation failed."
