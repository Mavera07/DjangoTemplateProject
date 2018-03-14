import sys
import os

def replaceTextInFile(file_absolute_path, oldtext, newtext):
    with open(file_absolute_path, 'r') as f:
        filedata = f.read()    

    filedata = filedata.replace(oldtext, newtext)

    with open(file_absolute_path, 'w') as f:
        f.write(filedata)

def nthParent(path,n):
    result = os.sep.join(path.split(os.sep)[:-n])
    return result


#initialDatabaseName  = "psqldb"
#initialUserName = "psqluser"
#initialPassword = "psql1234"
#initialHost = "psql_container"
#initialPort = "5432"
initialPostgresContainer = "psql_container"
newPostgresContainer = sys.argv[1]

currentfilepath = os.path.dirname(os.path.abspath(__file__))
projpath = nthParent(currentfilepath,2)
projname = os.path.basename(projpath)

djangosettingspath = projpath+"/"+projname+"/settings.py"
dockerfilepostgrespath = projpath+"/setup/docker/Dockerfile-postgres"
deploymentstartshpath = projpath+"/setup/docker/start.sh"

replaceTextInFile(djangosettingspath, initialPostgresContainer, newPostgresContainer)
replaceTextInFile(dockerfilepostgrespath, initialPostgresContainer, newPostgresContainer)
replaceTextInFile(deploymentstartshpath, initialPostgresContainer, newPostgresContainer)
