import requests
import threading,sys
class Main:
    def buff():
        cookies = {
            'PHPSESSID': 'bvhjvc2c00p521fj4irjq73601',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ar;q=0.4',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        }

        params = {
            'id': '16',
        }

        response = requests.get('http://pagepro.xyz/api/index.php', params=params, cookies=cookies, headers=headers, verify=False)
        print(response.json())
    def run_share():
                threa = 40
                while True:
                    t = threading.Thread(target=Main.buff)
                    t.start()
                    while threading.active_count() > threa:
                        t.join()
if __name__ == "__main__":
        Main.run_share()