def find_root_dir(self):
    abs_cwd = os.path.abspath('.')
    if abs_cwd.endswith('scripts'):
        self.em = '/../'
        parent_dir = os.path.realpath(abs_cwd + self.em)
        os.chdir(parent_dir)
    return 0


def get_root_func():
    return os.path.basename(handler.find_root_dir())
