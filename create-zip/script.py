import subprocess
import os
import handler


class Script:
    rootPath = handler.find_root_dir()
    scriptsPath = rootPath + '/scripts/'
    defaultZipFileName = (os.path.basename(rootPath)) + '.zip'
    nameZip = input('Zip file name <' + defaultZipFileName + '>: ')
    code_body = ''

    def create_body(self, body, list, i = 0):
        if i < len(list):
            if (os.path.isdir(self.scriptsPath + list[i])):
                self.code_body = body + ' -x ' + list[i] + "/\*"
                self.create_body(self.code_body, list, i + 1)
            else:
                self.create_body(self.code_body, list, i + 1)
        else:
            return 0

    def script(self):
        if self.nameZip == '':
            self.nameZip = self.defaultZipFileName
        if not self.nameZip.endswith('.zip'):
            self.nameZip = self.nameZip + '.zip'
        os.chdir(self.rootPath)
        self.code_body = 'zip -r ' + self.nameZip + " .  -x scripts/\*"
        list_dir = os.listdir(self.scriptsPath)
        self.create_body(self.code_body, list_dir)
        subprocess.call(self.code_body, shell=True)
        return 0


