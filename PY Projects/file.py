directory = "C:/Users/hjas/Projects/personal/romina_projects/PY Projects"


def read_file(fileName):
    file = open(directory + "/" + fileName)
    lines = file.read().split("\n")
    return lines
