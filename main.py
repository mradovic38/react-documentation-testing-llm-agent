from prompt_builder import PromptBuilder


def main():
    pb = PromptBuilder(package_dir="node_modules/@rescui/use-glow-hover")
    pb.build(template_path="prompt_templates/doc_prompt_template.txt", output_path="prompts/doc_prompt.txt")




if __name__ == '__main__':
    main()