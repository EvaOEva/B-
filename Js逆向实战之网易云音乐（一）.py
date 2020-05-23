import base64
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
    first_param = '{"/api/nuser/account/get":{},"/api/music-vip-membership/front/vip/info":{},"/api/purchased/redvip/vipstatus":{}}'
    second_param = '010001'
    third_param = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    forth_param = '0CoJUm6Qyw8W8jud'
    def catch_comments(self,page):
        for i in range(0,page):
            self.params['params'] = self.get_params()
            print(self.params['params'])

    def get_params(self):
        return self.AES_encrypt(self.AES_encrypt(self.first_param,self.forth_param,'0102030405060708').decode('utf-8'),'yS6rw8kKNHHLAjzW','0102030405060708').decode('utf-8')

    def AES_encrypt(self,text,key,iv):
        text += (16 - len(text) % 16) * chr(len(text) % 16)
        return base64.b64encode(AES.new(key.encode('utf-8'),AES.MODE_CBC,iv.encode('utf-8')).encrypt(text.encode('utf-8')))

if __name__ == '__main__':
    WangyiComments().catch_comments(1)
