import subprocess
import sqlite3
import os
import handler

#Create Lambda Function

class Script:
    defaultLambdaName = handler.get_root_func()
    nameLambda = input('Lambda function name: <' + defaultLambdaName + '>: ')
    defaultRuntime = 'nodejs8.10'
    runtime = input('Lambda function runtime <' + defaultRuntime + '>: ')
    defaultRole = 'arn:aws:iam::121703624033:role/lambda_basic_execution'
    role = input('Lambda function role <' + defaultRole + '>: ')
    defaultHandler = 'index'
    handler = input('Lambda function handler <' + defaultHandler + '>: ')
    defaultBucketName = "lambda-functions-kolserdav"
    bucketName = input("S3Bucket Lambda code name <" + defaultBucketName + ">: ")
    defaultKeyName = 'two-test-node.zip'
    keyName = input("S3Bucket Lambda code key <" + defaultKeyName + ">: ")
    result = ''
    s = '#'

    def script(self):
        if self.defaultLambdaName.index('.'):
            self.defaultLambdaName = self.defaultLambdaName.replace('.', '-')
        if self.nameLambda == '':
            self.nameLambda = self.defaultLambdaName
        if self.runtime == '':
            self.runtime = self.defaultRuntime
        if self.role == '':
            self.role = self.defaultRole
        if self.handler == '':
            self.handler = self.defaultHandler
        if self.bucketName == '':
            self.bucketName = self.defaultBucketName
        if self.keyName == '':
            self.keyName = self.defaultKeyName
        code = "S3Bucket=" + self.bucketName + ",S3Key=" + self.keyName
        call_body = 'aws lambda create-function --function-name ' + self.nameLambda + ' --runtime ' + self.runtime + \
            ' --role ' + self.role + ' --handler ' + self.handler + ' --code ' + code
        result = subprocess.check_output(call_body, shell=True)
        conn = sqlite3.connect('data.db')
        if conn:
            print('yes')
        else:
            print('no')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS stocks
                     (date text, trans text, symbol text, qty real, price real)''')
        c.execute("INSERT INTO stocks VALUES ('2006-01-05','sd','RHAT',100,35.14)")
        res = c.execute("SELECT * FROM stocks")
        conn.commit()
        c.close()
        res = conn.cursor()
        print('c: {0}', format(res))
        return 0


