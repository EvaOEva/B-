import requests
import time
import os

class Imgae():
    url = 'https://image.baidu.com/search/acjson?'
    headers = {
        'Cookie': 'BDqhfp=%E5%B0%8F%E5%A7%90%E5%A7%90%26%260-10-1undefined%26%26357%26%262; BIDUPSID=563D14E7073C5F64AFEF648DA1CA2C7B; PSTM=1589038782; BAIDUID=4FCBA2C585E866BE607A9A50AC58905B:FG=1; cflag=13%3A3; BDUSS=EQtZXZHUFVkOEk5OTBZMjQ5YkdydVk3WXJuakVnd3VtU0lyZGdod3pGVn53OTVlRVFBQUFBJCQAAAAAAAAAAAEAAACVh9yV0aew1M6sxOEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH82t15%7ENrdeV; H_PS_PSSID=31658_1449_31671_21111_31069_31594_31606_31780_31270_31463_30823_26350; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; firstShowTip=1; indexPageSugList=%5B%22%E5%B0%8F%E5%A7%90%E5%A7%90%22%2C%22%E4%B8%AD%E5%9B%BD%E5%9C%B0%E5%9B%BE%E5%9B%BE%E7%89%87%E7%AE%80%E7%AC%94%E7%94%BB%22%2C%22%E4%B8%AD%E5%9B%BD%E5%9C%B0%E5%9B%BE%E5%9B%BE%E7%89%87%20%E6%B8%85%E6%99%B0%20%E6%94%BE%E5%A4%A7%E5%9B%BE%E7%89%87%22%2C%22%E4%B8%AD%E5%9B%BD%E5%9C%B0%E5%9B%BE%E5%9B%BE%E7%89%87%22%2C%22mysql%22%5D; cleanHistoryStatus=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=null',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }
    params = {
        'tn': 'resultjson_com',
        'ipn': 'rj',
        'ct': '201326592',
        'is': '',
        'fp': 'result',
        'queryWord': '小姐姐',
        'cl': '2',
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'adpicid': '',
        'st': '-1',
        'z': '',
        'ic': '0',
        'hd': '',
        'latest': '',
        'copyright': '',
        'word': '小姐姐',
        's': '',
        'se': '',
        'tab': '',
        'width': '',
        'height': '',
        'face': '0',
        'istype': '2',
        'qc': '',
        'nc': '1',
        'fr': '',
        'expermode': '',
        'force': '',
        'pn': '',
        'rn': '30',
        'gsm': '',
        'time': ''
    }
    image_list = []
    def catch_page(self,num):
        for i in range(0,num):
            self.params['time'] = int(time.time() * 1000)
            self.params['pn'] = i * 30
            res = requests.get(url = self.url,headers = self.headers,params = self.params)
            for j in range(0,len(res.json()['data']) - 1):
                self.image_list.append(res.json()['data'][j]['thumbURL'])
        self.write_image()

    def write_image(self):
        n = 1
        for i in self.image_list:
            img = requests.get(url = i)
            open(f'./img/{n}.jpg','wb').write(img.content)
            n += 1

if __name__ == '__main__':
    Imgae().catch_page(2)
