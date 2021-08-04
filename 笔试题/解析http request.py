class request:
    def __init__(self):
        self.func = None
        self.url = None
        self.protocol = None
        self.body = None

    def decode(self, s):
        s_item = s.strip().split('\n')
        self.func, self.url, self.protocol = s_item.pop(0).strip().split(" ")
        self.body = s_item.pop(-1)
        header = {}
        for i in range(len(s_item)):
            if ':' in s_item[i]:
                key_value_list = s_item[i].split(':')
                key = key_value_list[0].strip()
                val = key_value_list[1].strip()
                header[key] = val
        print(header)
        print(header['authority'])
        return None


s = '''
POST http://127.0.0.1:8080/ccc/im/getActiveSession HTTP/1.1\n
authority: local.ccclogic.pstn.avc.qcloud.com
pragma: no-cache
cache-control: no-cache
sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"
accept: application/json, text/plain, */*
x-csrf-token: 0.6048526539993266
sec-ch-ua-mobile: ?0
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55
tccc-starttime: 1627275955425
origin: https://local.tccc.qcloud.com
sec-fetch-site: same-site
sec-fetch-mode: cors
sec-fetch-dest: empty
referer: https://local.tccc.qcloud.com/
accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
cookie: a=1; b=2;
Content-Type: application/json

{"clientType":"1","nonce":"01FBGK93705TM91JF7DY5A1SMH","requestId":"01FBGK93705TM91JF7DY5A1SMH","timestamp":"1627275955424","featureToggles":[],"staff":{"userId":"123","sdkAppId":"1400264214"},"instanceId":"1400255946","sdkAppId":"1400264214"}"
'''

re = request()
re.decode(s)
