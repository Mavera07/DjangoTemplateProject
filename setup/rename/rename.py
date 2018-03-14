import sys
import os

def replaceTextInDjangoFiles(projpath, oldtext, newtext):

    xfiles = [];xdirs = [];
    for (dirpath, dirnames, filenames) in os.walk(projpath):
        xfiles.extend(filenames)
        xdirs.extend(dirnames)
        if(".git" in xdirs): xdirs.remove(".git")
        break

    for xfile in xfiles:
        replaceTextInFile(projpath+"/"+xfile, oldtext, newtext)

    for xdir in xdirs:
        replaceTextInDjangoFiles(projpath+"/"+xdir, oldtext, newtext)


def replaceTextInFile(file_absolute_path, oldtext, newtext):
    with open(file_absolute_path, 'r') as f:
        filedata = f.read()    

    filedata = filedata.replace(oldtext, newtext)

    with open(file_absolute_path, 'w') as f:
        f.write(filedata)

def replaceApplicationName(projpath, newappname):
    os.rename(projpath+"/DjangoTemplateApplication",projpath+"/"+newappname)

def replaceProjectName(projpath, newprojname):
    parentpath = os.path.abspath(os.path.join(projpath, os.pardir))
    os.rename(projpath+"/DjangoTemplateProject",projpath+"/"+newprojname)
    os.rename(projpath, parentpath+"/"+newprojname)

def nthParent(path,n):
    result = os.sep.join(path.split(os.sep)[:-n])
    return result

currentfilepath = os.path.dirname(os.path.abspath(__file__))
projparentpath = print(nthParent(currentfilepath,3))

print(nthParent(currentfilepath,2))
print(nthParent(currentfilepath,3))
print(nthParent(currentfilepath,4))

#replaceTextInDjangoFiles(sys.argv[1], "DjangoTemplateProject" ,sys.argv[2])
#replaceTextInDjangoFiles(sys.argv[1], "DjangoTemplateApplication" ,sys.argv[3])
#replaceApplicationName(sys.argv[1], sys.argv[3])
#replaceProjectName(sys.argv[1], sys.argv[2])

