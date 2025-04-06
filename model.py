import os
from openai import OpenAI


class Model():
    def __init__(self, model_name="deepseek-reasoner", api_key=os.getenv("DEEPSEEK_API_KEY"),
                 base_url="https://api.deepseek.com"):
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model_name = model_name


    def generate_response(self, prompt_path):
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant"}, # DeepSeek R1 was trained like this
                {"role": "user", "content": prompt_path},
            ],
            stream=False
        )
response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)