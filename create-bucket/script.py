import handler
import os
import subprocess

class Script():
    bucketName = ''
    def script(self):
        root_project = handler.find_root_dir()
        self.bucketName = input('Bucket name <' + os.path.basename((root_project)) + '>: ')
        req = "aws s3api create-bucket --bucket " + self.bucketName + " --acl public-read --create-bucket-configuration LocationConstraint=us-west-2"
        subprocess.call(req, shell=True)
        reqWeb = "aws s3api put-bucket-website --bucket " + self.bucketName + " --website-configuration file://scripts/resources/conf-wnsite.json"
        subprocess.call(reqWeb, shell=True)




