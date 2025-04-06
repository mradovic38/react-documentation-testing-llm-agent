from model import Model
from output_processing import process_documentation
from prompt_builder import PromptBuilder

import os
from dotenv import load_dotenv

DOC_PROMPT_PATH = "prompts/doc_prompt.txt"
TEST_PROMPT_PATH = "prompts/test_prompt.txt"

def main():
    load_dotenv()

    pb = PromptBuilder(package_dir="node_modules/@rescui/use-glow-hover")
    pb.build(template_path="prompt_templates/doc_prompt_template.txt", output_path=DOC_PROMPT_PATH)

    model = Model(api_key=os.getenv("DEEPSEEK_API_KEY"))

    doc_response = model.generate(prompt_path=DOC_PROMPT_PATH, output_file="outputs/doc_raw.txt")

    process_documentation(doc_response, "outputs/doc.md")

if __name__ == '__main__':
    main()