import requests
import handler

#Function Write File


class Script():
    defaultUrl = 'ip.uyem.ru'

    def script(self):

        file_read = open(handler.find_root_dir() + '/scripts/resources/TestBook.djvu', 'rb')
        data = file_read.read()
        print(type(data))
        file_write = open(handler.find_root_dir() + '/scripts/resources/test1.html', 'w')
        #file_write.write(data)
        print(type(data))

