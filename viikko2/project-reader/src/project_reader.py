from urllib import request
from project import Project
import toml



class ProjectReader:
    
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_toml = toml.loads(content)
        new_toml = toml.dumps(parsed_toml)
        arr = new_toml.split("\n\n")

        name = arr[1].splitlines()[1].split('"')[1]
        
        description = arr[1].splitlines()[3].split('"')
        if description[1] == '"':
            description = "-"
        else:
            description = description[1]

        dependency_block = arr[2].splitlines()
        dependencies = []

        for line in dependency_block[1:len(dependency_block)]:
            dependencies.append(line.split(' =')[0])

        dev_dep_block = arr[3].splitlines()
        dev_dependencies = []

        for line in dev_dep_block[1:len(dev_dep_block)]:
            dev_dependencies.append(line.split(" =")[0])
        

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies)
