import sys
import os

def getBowerInstalledApps(bower_absolute_path):
    with open(bower_absolute_path, 'r') as f:
        packages = f.readlines()

    bower_installed_apps = ""
    for package in packages:
        bower_installed_apps += "'"+ package.strip() +"',\n    "
    bower_installed_apps = bower_installed_apps[:-5]

    return bower_installed_apps

def replaceTextInFile(file_absolute_path, oldtext, newtext):
    with open(file_absolute_path, 'r') as f:
        filedata = f.read()

    filedata = filedata.replace(oldtext, newtext)

    with open(file_absolute_path, 'w') as f:
        f.write(filedata)

def nthParent(path,n):
    result = os.sep.join(path.split(os.sep)[:-n])
    return result


bower_installed_apps_mark = "'bower_installed_apps_mark',"

currentfilepath = os.path.dirname(os.path.abspath(__file__))
projpath = nthParent(currentfilepath,2)
bower_absolute_path = projpath + "/resources/bower.txt"
djangosettings_absolute_path = projpath + "/djangotemplateproject/settings.py"

bower_installed_apps = getBowerInstalledApps(bower_absolute_path)
replaceTextInFile(djangosettings_absolute_path,bower_installed_apps_mark,bower_installed_apps)


