import subprocess
import os
import importlib.util
import time
import handler

#Put Bucket Function


class Script():



    defaultBucketName = "lambda-functions-kolserdav"
    defaultPublish = 'y'
    defaultKeyName = ''
    defaultZipFile = ''
    zipFile = ''
    publish = ''
    nameLambda = ''
    bucketName = ''
    keyName = ''
    result = ''

    def script(self):
        root_scripts = handler.find_root_dir()
        root_dir_name = os.path.basename(root_scripts)
        self.defaultKeyName = root_dir_name
        self.defaultZipFile = root_scripts + '/' + self.defaultKeyName
        self.nameLambda = input('Key object: <' + root_dir_name + '>: ')
        if root_dir_name.index('.'):
              self.defaultKeyName = root_dir_name.replace('.', '-')
        self.zipFile = input('Source file <' + self.defaultZipFile + '>: ')
        self.bucketName = input("S3Bucket name <" + self.defaultBucketName + ">: ")
        if self.nameLambda == '':
            self.nameLambda = self.defaultKeyName
        if self.zipFile == '':
            self.zipFile = self.defaultZipFile
            self.result = 's3'
        if self.bucketName == '':
            self.bucketName = self.defaultBucketName
        bucket_request = "aws s3api put-object --acl public-read --bucket " + self.bucketName + ' --key ' + \
                         self.nameLambda + ' --body ' + self.zipFile + ' --content-type text/html'
        if not subprocess.check_output(bucket_request, shell=True):
            return print('Main bucket no get bucket request from subprocess check output [Error}: 010')

        return 0


