

def replaceProjectName(path, projname):
    pass

def replaceApplicationName():
    pass

def replaceTextInDjangoFiles(path):
    focusFiles = [];focusDirs = [];
    for (dirpath, dirnames, filenames) in os.walk(path):
        focusFiles.extend(filenames)
        focusDirs.extend(dirnames)
        break    

    pass

def replaceTextInFile(file_absolute_path, oldtext, newtext):
    with open(file_absolute_path, 'r') as f:
        filedata = f.read()    

    filedata = filedata.replace(oldtext, newtext)

    with open(file_absolute_path, 'w') as f:
        f.write(filedata)

