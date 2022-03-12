import os.path


def read_markdown(name: str):
    file = "markdown/" + name + '.md'
    if os.path.exists(file):
        f = open(file)
        return f.read()
    else:
        return ""
