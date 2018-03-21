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

def replaceApplicationName(projpath, oldappname, newappname):
    xdirs = [];
    for (dirpath, dirnames, filenames) in os.walk(projpath):
        xdirs.extend(dirnames)
        if(".git" in xdirs): xdirs.remove(".git")
        break
    
    for xdir in xdirs:
        replaceApplicationName(projpath+"/"+xdir,oldappname,newappname)
        if(xdir == oldappname):
            os.rename(projpath+"/"+oldappname,projpath+"/"+newappname)

    # os.rename(projpath+"/"+oldappname,projpath+"/"+newappname)

def replaceProjectName(projpath, oldprojname, newprojname):
    projparentpath = os.path.abspath(os.path.join(projpath, os.pardir))
    os.rename(projpath+"/"+oldprojname,projpath+"/"+newprojname)
    os.rename(projpath, projparentpath+"/"+newprojname)

def nthParent(path,n):
    result = os.sep.join(path.split(os.sep)[:-n])
    return result


initialProjectName  = "djangotemplateproject"
initialApplicationName = "djangotemplateapplication"

newProjectName = sys.argv[1]
newApplicationName = sys.argv[2]

currentfilepath = os.path.dirname(os.path.abspath(__file__))
projpath = nthParent(currentfilepath,2)

replaceTextInDjangoFiles(projpath, initialProjectName ,newProjectName)
replaceTextInDjangoFiles(projpath, initialApplicationName ,newApplicationName)
replaceApplicationName(projpath, initialApplicationName, newApplicationName)
replaceProjectName(projpath, initialProjectName, newProjectName)

