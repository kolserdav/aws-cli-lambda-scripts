import os


def find_root_dir():
    abs_cwd = os.path.abspath('.')
    if abs_cwd.endswith('scripts'):
        self.em = '/../'
        parent_dir = os.path.realpath(abs_cwd + self.em)
        os.chdir(parent_dir)
        return parent_dir
    return abs_cwd


def get_root_func():
    return os.path.basename(find_root_dir())

