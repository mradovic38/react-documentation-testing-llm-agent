import os
from openai import OpenAI


class Model:
    def __init__(self,
                 api_key,
                 model_name="deepseek-reasoner",
                 base_url="https://api.deepseek.com"):

        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model_name = model_name


    def generate(self, prompt_path, output_file):
        try:
            with open(prompt_path, "r") as prompt_file:
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant"}, # DeepSeek R1 was trained like this
                        {"role": "user", "content": prompt_file.read()},
                    ],
                    stream=False
                )

            content = response.choices[0].message.content

            with(open(output_file, "w")) as f:
                f.write(content)


        except Exception as e:
            print(f"Failed to read {prompt_path}: {e}")