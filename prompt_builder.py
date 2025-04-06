import os

def _format_code(code, fname):
    return f'# `{fname}`\n\n'  + f'```{fname.split('.')[-1]}\n' + code + '```\n\n'

class PromptBuilder:
    def __init__(self, package_dir):
        self.package_dir = package_dir

    def build(self, template_path, output_path):

        combined_code = ""

        # Load package.json on top
        try:
            with open(os.path.join(self.package_dir, "package.json"), "r") as f:
                combined_code += _format_code(f.read(), "package.json")
        except Exception as e:
            print(f"Failed to read package.json: {e}")

        # Walk through lib to load .ts and .js files
        for dirpath, _, filenames in os.walk(os.path.join(self.package_dir, "lib")):
            for filename in filenames:
                if filename.endswith(".ts") or filename.endswith(".js"):
                    file_path = os.path.join(dirpath, filename)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            code = f.read()
                            combined_code += _format_code(code, filename)

                    except Exception as e:
                        print(f"Failed to read {file_path}: {e}")

        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()

        # Replace the <code> tag
        filled_content = template_content.replace("<code>", combined_code)

        # Save the new file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(filled_content)


if __name__ == "__main__":
    pb = PromptBuilder("node_modules/@rescui/use-glow-hover")
    pb.build(template_path='prompt_templates/doc_prompt_template.txt', output_path='prompts/doc_prompt.txt')