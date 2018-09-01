import subprocess
import os
import importlib.util
import time
import handler

#Put Bucket Function


class Script():


    defaultKeyName = defaultLambdaName + '.zip'
    defaultZipFile = rootScripts + '/' + defaultKeyName
    defaultBucketName = "lambda-functions-kolserdav"
    defaultPublish = 'y'
    zipFile = ''
    publish = ''
    nameLambda = ''
    bucketName = ''
    keyName = ''
    result = ''

    def script(self):
        root_scripts = handler.find_root_dir()
        root_dir_name = os.path.basename(root_scripts)
        self.nameLambda = input('File .zip body name: <' + root_dir_name + '>: ')
        if root_dir_name.index('.'):
              self.nameLambda = root_dir_name.replace('.', '-')
        self.zipFile = input('Zip file <' + self.defaultZipFile + '>: ')
        self.bucketName = input("S3Bucket Lambda code name <" + self.defaultBucketName + ">: ")
        self.keyName = input("S3Bucket Lambda code key <" + self.defaultKeyName + ">: ")
        if self.nameLambda == '':
            self.nameLambda = root_dir_name
        if self.zipFile == '':
            self.zipFile = self.defaultZipFile
            self.result = 's3'
        if self.bucketName == '':
            self.bucketName = self.defaultBucketName
        bucket_request = "aws s3api put-object --acl private --bucket " + self.bucketName + ' --key ' + \
                         self.nameLambda + '.zip' + ' --body ' + self.zipFile
        if not subprocess.check_output(bucket_request, shell=True):
            return print('Main bucket no get bucket request from subprocess check output [Error}: 010')

        return 0


