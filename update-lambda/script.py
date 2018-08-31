import subprocess
import os
import importlib.util
import time
import handler

#Update Lambda Function


class Script():

    #TO DO ''

    rootScripts = handler.find_root_dir()
    defaultLambdaName = os.path.basename(rootScripts)
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
        self.nameLambda = input('Lambda function name: <' + self.defaultLambdaName + '>: ')
        if self.defaultLambdaName.index('.'):
            self.defaultLambdaName = self.defaultLambdaName.replace('.', '-')
        self.zipFile = input('Zip file <' + self.defaultZipFile + '>: ')
        self.publish = input('Publish function <' + self.defaultPublish + '>: ')
        self.bucketName = input("S3Bucket Lambda code name <" + self.defaultBucketName + ">: ")
        self.keyName = input("S3Bucket Lambda code key <" + self.defaultKeyName + ">: ")
        if self.nameLambda == '':
            self.nameLambda = self.defaultLambdaName
        if self.zipFile == '':
            self.zipFile = self.defaultZipFile
            self.result = 's3'
        if self.defaultPublish == '':
            self.publish = self.defaultPublish
        if self.publish.lower() == 'y':
            self.publish = '--publish'
        else:
            self.publish = '--no-publish'
        if self.bucketName == '':
            self.bucketName = self.defaultBucketName
        if self.keyName == '':
            self.keyName = self.defaultKeyName
        bucket_request = "aws s3api put-object --acl private --bucket " + self.bucketName + ' --key ' + \
                         self.nameLambda + '.zip' + ' --body ' + self.zipFile
        if not subprocess.check_output(bucket_request, shell=True):
            return print('Main bucket no get bucket request from subprocess check output [Error}: 010')
        call_body_zip = 'aws lambda update-function-code --function-name ' + self.nameLambda + ' --zip-file ' + self.zipFile + \
            ' ' + self.publish
        call_body_s3 = 'aws lambda update-function-code --function-name ' + self.nameLambda + ' --s3-bucket ' + self.bucketName + \
            ' --s3-key ' + self.keyName + ' ' + self.publish
        if self.result == 's3':
            result = subprocess.call(call_body_s3, shell=True)
        else:
            result = subprocess.call(call_body_zip, shell=True)

        return 0


