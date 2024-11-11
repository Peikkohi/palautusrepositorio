class Project:
    def __init__(self,
            name,
            description,
            license,
            authors,
            dependencies,
            dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_multiple(self, values):
        return "\n- " + "\n- ".join(values) if len(values) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Description: {self.description or '-'}\n"
            f"License: {self.license or '-'}\n\n"
            f"Authors: {self._stringify_multiple(self.authors)}\n\n"
            f"Dependencies: {self._stringify_multiple(self.dependencies)}\n\n"
            f"Development dependencies:"
            f"{self._stringify_multiple(self.dev_dependencies)}"
        )
