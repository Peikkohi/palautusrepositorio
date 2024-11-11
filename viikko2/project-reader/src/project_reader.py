from urllib import request
from project import Project

import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        parsed_toml = toml.loads(content)
        print(parsed_toml)
        tool_poetry = parsed_toml["tool"]["poetry"]

        name = tool_poetry["name"]
        description = tool_poetry["description"]
        license = tool_poetry["license"]
        authors = list(tool_poetry["authors"])
        dependencies = list(tool_poetry["dependencies"])
        dev_dependencies = list(tool_poetry["group"]["dev"]["dependencies"])

        # deserialisoi TOML-formaatissa oleva merkkijono
        # ja muodosta Project-olio sen tietojen perusteella
        return Project(
                name,
                description,
                license,
                authors,
                dependencies,
                dev_dependencies
                )
