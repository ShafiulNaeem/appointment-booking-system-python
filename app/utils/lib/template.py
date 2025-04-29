import os
import re

TEMPLATE_DIR = "templates"

def render_template(template_path, context={}):
    full_path = os.path.join(TEMPLATE_DIR, template_path)
    if not os.path.exists(full_path):
        return error404()

    with open(full_path, "r", encoding="utf-8") as file:
        content = file.read()

    content = _replace_variables(content, context)
    content = _process_content(content, context)
    return content

def _process_content(content,context):
    content = _process_includes(content, context)
    content = _process_extend(content, context)
    return content

def _process_extend(content,context):
    extend_pattern = r"""@extend\(['"]([^'"]+)['"]\)"""
    extends = re.findall(extend_pattern, content)

    if not extends:
        return content

    for extend_file in extends:
        content = content.replace(f"@extend('{extend_file}')", "")
        extend_path = os.path.join(os.getcwd(), extend_file)
        if os.path.exists(extend_path):
            with open(extend_path, "r", encoding="utf-8") as f:
                extend_content = f.read()
                
            extend_content = _process_includes(extend_content, context)
            extend_content = extend_content.replace(f"@section('content')", content)
        else:
            extend_content = content.replace(f"@section('content')", f"<!-- Missing include: {extend_file} -->")

    return extend_content

def _process_includes(content,context):
    include_pattern = r"""@include\(['"]([^'"]+)['"]\)"""
    includes = re.findall(include_pattern, content)
    
    for include_file in includes:
        include_path = os.path.join(os.getcwd(), include_file)
        if os.path.exists(include_path):
            with open(include_path, "r", encoding="utf-8") as f:
                include_content = f.read()

            include_content = _replace_variables(include_content, context)
            content = content.replace(f"@include('{include_file}')", include_content)
        else:
            content = content.replace(f"@include('{include_file}')", f"<!-- Missing include: {include_file} -->")

    return content

def _replace_variables(content, context):
    for key, value in context.items():
        # print(f"Replacing {{{{ {key} }}}} with {value}")
        content = content.replace(f"{{{{ {key} }}}}", str(value))
    return content

def error404():
    full_path = os.path.join(os.getcwd(), 'templates/error/error-404.html')
    if not os.path.exists(full_path):
        return "<!-- Missing include: error-404.html -->"

    with open(full_path, "r", encoding="utf-8") as file:
        content = file.read()
        content = _process_content(content, {"title": "404 Not Found"})
    return content
