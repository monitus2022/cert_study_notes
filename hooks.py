import re

def on_page_markdown(markdown, page, config, files):
    # Inserts a blank line between text/bold headers (like **Topics**) and lists
    markdown = re.sub(
        r'^(?!\s*[-+*]\s|\s*\d+\.\s|\s*$)(.+)\n(?=[-+\*]\s|\d+\.\s)',
        r'\1\n\n',
        markdown,
        flags=re.MULTILINE
    )
    return markdown