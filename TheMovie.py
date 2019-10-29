import requests
from lxml import etree
import time
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Cookie': 'bid=hAEdbjYcGX8; __utmz=223695111.1561354567.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ct=y; __utmz=30149280.1561358923.2.2.utmcsr=movie.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/subject/26752088/comments; loc-last-index-location-id="118282"; ll="118282"; _vwo_uuid_v2=D0D8C7EB3554A599ADE60518126C26B73|7f8e9f93a3c5dc93ca40f8469266b6f9; trc_cookie_storage=taboola%2520global%253Auser-id%3D254c1dc2-0164-4ae2-b334-50d7a4df43b0-tuct40a025e; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1680265346.1561354567.1561448171.1561450198.5; __utmc=30149280; __utma=223695111.1763528297.1561354567.1561448171.1561450198.5; __utmb=223695111.0.10.1561450198; __utmc=223695111; __utmb=30149280.3.10.1561450198; push_doumail_num=0; push_noty_num=0; _pk_id.100001.4cf6=bcae4dc39f34fce0.1561354567.5.1561450576.1561448171.; dbcl2="190616662:oiPEX857mCc"'
}


def get_html(url):
#     r = requests.get(url,headers = headers)
#     # r.encoding = r.apparent_encoding
#     html = etree.HTML(r.text())
    r = requests.get(url,headers = headers).text
    # r.encoding = r.apparent_encoding
    html = etree.HTML(r)
    return html

def get_info(html):
    # ad = html.xpath('//span[@class="comment-info"]/a/text()')

    comments = html.xpath('//div[@class="comment"]/p/span/text()')
    weighs = html.xpath('//span[@class="comment-vote"]/span/text()')
    times = html.xpath('//span[@class="comment-info"]/span[@class="comment-time "]/text()')
    stars = html.xpath('//div[@class = "comment-item"]/div[2]/h3/span[2]/span[2]/@title')
    # st = html.xpath('//span[@class="comment-info"]/span[@class="allstar40-rating "]/text()')


    # ti = str(ti).replace('\n                    ',"")
    # time = html.xpath('//span[@class="comment-time "]/span/text()')
    link = html.xpath('//span[@class="comment-info"]/a/@href')

    # print(link)

    # people = requests.get(link).text
    # html2 = etree.HTML(people)
    # loc =html2.xpath('//div[@class="user-info"]/a/text()')
    # print(loc)
    return comments, weighs,times,stars




def get_url(page):
    url = 'https://movie.douban.com/subject/26752088/comments?start=' + str(20 * page) + '&amp;limit=20&amp;sort=time&amp;status=P'
    # time.sleep(random.random())
    time.sleep(1)
    return url

with open("C:\\Users\\HP\\Desktop\\电影分析1.txt",'w',encoding='utf_8',newline='')as f:
    for page in range(1, 10):  # 访问下一页
        # imgs,charts = get_info(get_html(get_url(page)))
        comments, weighs, times, stars = get_info(get_html(get_url(page)))
        writer=csv.writer(f)
        for i in range(len(comments)-1):
            writer.writerow([comments[i]])

with open("C:\\Users\\HP\\Desktop\\电影分析2.xls",'w',encoding='utf_8',newline='')as f:
    for page in range(1, 10):  # 访问下一页
        # imgs,charts = get_info(get_html(get_url(page)))
        comments, weighs, times, stars = get_info(get_html(get_url(page)))
        writer=csv.writer(f)
        for i in range(len(comments)-1):
            writer.writerow([stars[i]+'\t'+time[i]])
            writer.writerow([ stars[i]],2)






