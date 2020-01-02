'''
curl "https://www.v2ex.com/?tab=play" -H "authority: www.v2ex.com" -H "cache-control: max-age=0" -H "upgrade-insecure-requests: 1" -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36" -H "sec-fetch-user: ?1" -H "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" -H "sec-fetch-site: same-origin" -H "sec-fetch-mode: navigate" -H "referer: https://www.v2ex.com/?tab=creative" -H "accept-encoding: gzip, deflate, br" -H "accept-language: zh-CN,zh;q=0.9,pl;q=0.8,zh-HK;q=0.7" -H "cookie: __cfduid=d614fcdd7d64ba896b75a268044e414961575507531; _ga=GA1.2.1040342795.1575507523; PB3_SESSION=^\^"2^|1:0^|10:1577773924^|11:PB3_SESSION^|40:djJleDoxMjQuMjA0LjQxLjIyNjo3OTQ1ODc3OA==^|af07afbf59e0ab1aa25c1ebd430fc525e822642bea6b182612766a39dc96aff2^\^"; V2EX_REFERRER=^\^"2^|1:0^|10:1577936223^|13:V2EX_REFERRER^|16:YWx3YXlzaGVyZQ==^|ce1a8dbe68613aa78234c19f14a0bcb963a765b829b064811ad75c73495a1ab8^\^"; V2EX_LANG=zhcn; V2EX_TAB=^\^"2^|1:0^|10:1577950661^|8:V2EX_TAB^|8:cGxheQ==^|9fb555fa9fb76649eb3b4805b983dd249ffaf44a29a47f54c875bda2ce123f7f^\^"" --compressed
'''
import re

def requets_url(html):
    url=re.search('''curl\s*[\'\"](.*?)[\'\"]\s*-H''',html).group(1)
    return url

def  requets_headers(html):

    headersall = {}
    header_s=re.findall('''-H\s*[\'\"](.*?)[\'\"]''',html)
    for he in header_s:
        header_key=he.split(": ")[0]
        header_value=he.split(": ")[1]
        headersall[header_key]=header_value
    return headersall


def  Requets_headers(html):
    headers=requets_headers(html)
    if "cookie" in headers:
        del headers['cookie']
    else:
        del headers['Cookie']

    return  headers

def  Requets_cookie(html):
    headers = requets_headers(html)
    cookie=headers['cookie'] if "cookie" in headers else headers['Cookie']
    cookies={}
    cooklist=cookie.split(";")
    for i in cooklist:
        cookie_key=i.split("=")[0].replace(" ",'')
        cookie_value=i.split("=")[1].replace(" ",'')
        cookies[cookie_key]=cookie_value
    return cookies

def post_data(html):
    data=re.search('''--data.*[\'\"](.*?)--compressed''',html,re.DOTALL).group(1)
    print(data)

def  finish(html):
    pac='''import requests'''
    cookies=Requets_cookie(html)
    headers=Requets_headers(html)
    url='''"'''+requets_url(html)+'''"'''
    response='''requests.get(url=url, headers=headers, cookies=cookies, verify=False)'''

    all_code=pac+"\n"+"cookies"+"=%s"%cookies+"\n"+"headers"+"=%s"%headers+"\n"+"url"+"=%s"%url+"\n"+"response"+"=%s"%response+"\n"+'''print(response.text)'''
    print(all_code)











if __name__ == '__main__':
    html=str(input("请输入curl:"))
    # Requets_headers(html)
    # Requets_cookie(html)
    finish(html)
    # post_data(html)
