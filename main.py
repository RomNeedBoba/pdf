from fasthtml.common import *
from pathlib import Path

app, rt = fast_app()

@rt("/")
def get():
    html = Path("main.html").read_text()
    return NotStr(html)  # NotStr = don't escape, output raw HTML

serve()
