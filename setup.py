import os
import subprocess
import importlib.util


class FunctionName:
    funcName = ''
    funcPath = ''
    em = ''
    rootScripts = ''

    def find_root_dir(self):
        abs_cwd = os.path.abspath('.')
        if abs_cwd.endswith('scripts'):
            self.em = '/../'
            parent_dir = os.path.realpath(abs_cwd + self.em)
            os.chdir(parent_dir)

    def get_module_import(self):
        func_full_name = self.funcPath + '/script.py'
        spec = importlib.util.spec_from_file_location("script", func_full_name)
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        script = foo.Script()
        script.script()

    def get_function_name(self):
        self.funcName = input('Script name: ')
        self.funcName = self.funcName.strip()
        self.rootScripts = os.path.abspath('./scripts')
        self.funcPath = self.rootScripts + "/" + self.funcName
        if os.path.isdir(self.funcPath):
            self.get_module_import()
            return 0
        else:
            print("Error: directory [" + self.funcName + "] in [" + self.rootScripts + "]  undefined")
            self.get_function_name()
        self.find_root_dir()



fN = FunctionName()
fN.get_function_name()







