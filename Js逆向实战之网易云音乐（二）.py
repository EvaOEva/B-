import base64
import requests
from Crypto.Cipher import AES

class WangyiComments():
    url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_545350509?csrf_token='
    headers = {
        'referer': 'https://music.163.com/song?id=545350509',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    params = {
        'params': None,
        'encSecKey': None
    }
    hotComments_names,hotComments_contents,hot_list = [],[],None
    originComments_names,originComments_contents,origin_list = [],[],None
    first_param = None
    second_param = '010001'
    third_param = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    forth_param = '0CoJUm6Qyw8W8jud'
    def catch(self,page):
        self.params['encSecKey'] = '88d26c5b79f4a3172b544f7fd713463b4f175b117115f6abae2c83bc5fb24659575ad936a6e854a05e78fe9f91aa65b65db01c8ed6d3bb29cd1cef86be1329de39a1cadf160b28db71cc050451a5574cecaf39f1e8272195194c516d2180827377d8ce72ffe1b59543c236a6a29ecbe14023d23d067896d0d5435b9062078b79'
        # self.catch_hotComments()
        self.catch_originComments(page)
        self.print_data()

    def catch_hotComments(self):
        self.params['params'] = self.get_params(0)
        res = requests.post(url = self.url,headers = self.headers,params = self.params)
        for data in res.json()['hotComments']:
            self.hotComments_names.append(data['user']['nickname'])
            self.hotComments_contents.append(data['content'])
        self.hot_list = list(zip(self.hotComments_names,self.hotComments_contents))

    def catch_originComments(self,page):
        for i in range(0,page):
            self.params['params'] = self.get_params(i)
            res = requests.post(url=self.url, headers=self.headers, params=self.params)
            for data in res.json()['comments']:
                self.originComments_names.append(data['user']['nickname'])
                self.originComments_contents.append(data['content'])
        self.origin_list = list(zip(self.originComments_names,self.originComments_contents))

    def print_data(self):
        for data in self.origin_list:
            print(data)

    def get_params(self,page):
        if page == 0:
            self.first_param = '{rid: "R_SO_4_545350509", offset: "0", total: "true", limit: "20"}'
        else:
            self.first_param = '{rid: "R_SO_4_545350509", offset: "%s", total: "false", limit: "20"}' % (page * 20)
        return self.AES_encrypt(self.AES_encrypt(self.first_param,self.forth_param,'0102030405060708').decode('utf-8'),'pmkRML01jzGN5l6l','0102030405060708').decode('utf-8')

    def AES_encrypt(self,text,key,iv):
        text += (16 - len(text) % 16) * chr(16 - len(text) % 16)
        return base64.b64encode(AES.new(key.encode('utf-8'),AES.MODE_CBC,iv.encode('utf-8')).encrypt(text.encode('utf-8')))

if __name__ == '__main__':
    WangyiComments().catch(2)
