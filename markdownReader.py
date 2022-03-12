import code
import os.path


def read_markdown(name: str):
    file = "markdown/" + name + '.md'
    if os.path.exists(file):
        f = open(file, encoding='utf-8')
        return f.read()
    else:
        return ""

def read_markdown_list():
    file = 'markdown/mdlist.txt'
    if os.path.exists(file):
        lst = []
        sublst=  []
        for line in open(file, encoding='utf-8'):
            # line = f.readline()
            line = line.replace('\n','')
            if (line.startswith('--')):
                sublst.append(line.replace('-',''))
            else:
                if len(sublst) > 0:
                    lst.append(sublst)
                    sublst=[]
                lst.append(line)    

        if len(sublst) > 0:
                    lst.append(sublst)
                    sublst=[]

        print(lst)
        return lst        

    else:
        return ""