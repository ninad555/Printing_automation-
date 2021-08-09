import os


class get_path:
    def __init__(self):
        path = os.getcwd()
        self.absolute_path = str(path.replace("\\", "\\\\"))

    def get_project_root(self):

      return self.absolute_path