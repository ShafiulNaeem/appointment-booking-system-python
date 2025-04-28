import os
import re

TEMPLATE_DIR = "templates"

def render_template(template_path, context={}):
    full_path = os.path.join(TEMPLATE_DIR, template_path)

    if not os.path.exists(full_path):
        return "Template not found", 404

    with open(full_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Handle {% include "shared/header.html" %}
    # content = _process_includes(content)

    # Handle {{ title }} replacement
    content = _replace_variables(content, context)
    # print(content)

    return content

# def _process_includes(content):
#     include_pattern = r'{% include ["\'](.+?)["\'] %}'
#     includes = re.findall(include_pattern, content)

#     for include_file in includes:
#         include_path = os.path.join(TEMPLATE_DIR, include_file)
#         if os.path.exists(include_path):
#             with open(include_path, "r", encoding="utf-8") as f:
#                 include_content = f.read()
#             content = content.replace(f'{% include "{include_file}" %}', include_content)
#             content = content.replace(f"{% include '{include_file}' %}", include_content)
#         else:
#             content = content.replace(f'{% include "{include_file}" %}', f"<!-- Missing include: {include_file} -->")
#     return content

def _replace_variables(content, context):
    for key, value in context.items():
        content = content.replace(f"{{{{ {key} }}}}", str(value))
    return content
