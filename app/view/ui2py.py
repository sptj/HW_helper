import os
def ui_document_transfor():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    command='pyside-uic '+current_dir+'\layout.ui'+' -o '+current_dir+'\layout.py'
    # print command
    os.system(command)
    # with open(current_dir+'\layout.py', 'r') as r:
    #     lines = r.readlines()
    # with open(current_dir+'\layout.py', 'w') as w:
    #     for l in lines:
    #         w.write(l.replace('PySide', 'PyQt4'))
if __name__=="__main__":
    ui_document_transfor()