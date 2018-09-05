import requests
import handler


class Script():
    defaultUrl = 'ip.uyem.ru'

    def script(self):
        if not self.defaultUrl.find('https') + 1:
            self.defaultUrl = 'https://' + self.defaultUrl
            print(self.defaultUrl)
        url = input('Request url <' + self.defaultUrl + '>: ')
        if url == '':
            url = self.defaultUrl
        if not url.find('https') + 1:
            self.defaultUrl = url
            self.script()
        response = requests.get(url)
        print(self.defaultUrl)
        file = open(handler.find_root_dir() + '/scripts/resources/test.html', 'w')
        file.write(response.content.decode('utf-8'))

