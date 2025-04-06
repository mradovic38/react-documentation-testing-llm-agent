import re

def process_documentation(response_content, output_file):
    pattern = r'```md(.*?)```'
    matches = re.findall(pattern, response_content, re.DOTALL)

    with open(output_file, 'w') as f:
        f.write('\n'.join(matches))

def process_tests(response_content, output_file): # TODO - implement
    pass