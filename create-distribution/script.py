import handler
import subprocess

#Function Create Distribution


class Script():

    def script(self):
        name_bucket = input('Website bucket name: ')
        web_site = "http://" + name_bucket + ".s3-website-us-west-2.amazonaws.com"
        aws = "aws cloudfront create-distribution --distribution-config file://scripts/resources/example-config.json"
        subprocess.call(aws, shell=True)


