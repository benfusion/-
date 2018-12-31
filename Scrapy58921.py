# coding=UTF-8
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import csv
from urllib.parse import urljoin
import urllib
import pymysql

R = requests.Session()

db = pymysql.connect(host='localhost', user='root', passwd='Oracle19990112', db='movies_database',port=3306, charset='utf8')  # 在workbench自行创建数据库后连接成功

# 获取游标
cursor = db.cursor()

movie_data=['','','','','','','','','','','','','','']
print(len(movie_data))


def get_ticket(url):
    try:
        page = urllib.request.urlopen(url)
        html = page.read().decode(encoding='utf-8')
        pattern = re.compile(r'\(最新票房 (.+?)\)')
        movie_data[10]=pattern.findall(str(html))[0]                                                                    #电影票房存储在movie_data[10]中
        return pattern.findall(str(html))

    except:
        return '失败！！！！！！！！\n\n'
        exit()

def print_player(player_sum):
    if player_sum >= 3:
        print(player_list[0].get_text())  # 主演存储在player_list[0].get_text()中
        movie_data[4] = player_list[0].get_text()                                                                       # movie_data[4]中存储演员1
        print(player_list[1].get_text())
        #print(len(movie_data))
        movie_data[5] = player_list[1].get_text()                                                                       # movie_data[5]中存储演员2
        print(player_list[2].get_text())
        #print(len(movie_data))
        movie_data[6] = player_list[2].get_text()
        #print(len(movie_data))                                                                                          # movie_data[6]中存储演员3
    else:
        i = 0
        while (i <= player_sum - 1):
            print(player_list[i].get_text())
            movie_data[4+i] = player_list[i].get_text()
            #print(len(movie_data))
            # print(i)
            i += 1
        rest=3-i-1
        while((rest+1)!=0):
            movie_data[4 + i+rest] ='0'
            rest-=1




def print_director(director_sum):
    if director_sum >= 2:
        if ((director_list[0].get_text().find(' ') != -1) & (director_list[1].get_text().find(' ') != -1)):  # 因为爬取的网站导演数据中  在相应title中存储两个导演并用两个空格符隔开
            blank_seat = director_list[0].get_text().find(' ')                                               # eg<li><strong>导演：</strong><a href="/name/9310" title="俞白眉  邓超">俞白眉  邓超</a></li>
            print(director_list[0].get_text()[:blank_seat])                                                  # 而正常情况一般为一个title中之存储一个导演   故用if判断语句处理这种异常情况
            print(director_list[0].get_text()[blank_seat + 2:])
            print(director_list[1].get_text()[:blank_seat])
            print(director_list[1].get_text()[blank_seat + 2:])

        else:
            print(director_list[0].get_text())
            print(director_list[1].get_text())
            # 经测试，2015/12/17 15:12截止 58921.com的电影页面中，没有符合上述情况的导演数据排列         故可以考虑将次判断结构注释掉

    else:
        if (director_list[0].get_text().find(' ') != -1):
            blank_seat = director_list[0].get_text().find(' ')
            print(director_list[0].get_text()[:blank_seat])
            movie_data[2] = director_list[0].get_text()[:blank_seat]                                        #如果出现网页代码中导演1 导演2出现在同一标签中时作如左处理
            print(director_list[0].get_text()[blank_seat + 2:])
            movie_data[3] = director_list[0].get_text()[blank_seat + 2:]                                    #movie_data[2]中存储导演1  movie_data[3]中存储导演2
        else:
            print(director_list[0].get_text())
            movie_data[2]=director_list[0].get_text()                                                       #只有一个导演的情况下movie_data[2]中存储导演1 movie_data[2]中存储空字符串
            print(len(movie_data))
            movie_data[3]='0'
            print(len(movie_data))


def print_type(type_sum):
    if type_sum >= 3:
        print(type_list[0].get_text())# 主演存储在player_list[0].get_text()中
        print(type_list[1].get_text())
        print(type_list[2].get_text())
        movie_data[11] = type_list[0].get_text()
        movie_data[12] = type_list[1].get_text()
        movie_data[13] = type_list[2].get_text()
    else:
        i = 0
        while (i <= type_sum - 1):
            print(type_list[i].get_text())
            movie_data[11 + i] = type_list[i].get_text()
            # print(len(movie_data))
            # print("i am here  asshole 5789")
            # print(i)
            i += 1
        rest = 3 - i - 1
        while ((rest+1) != 0):
            movie_data[11 + i + rest] = '0'
            rest -= 1



j = 0
'''log_in()'''
year = 2015
movie_sum = 0
fail_sum = 0
host = 'http://58921.com'
m=0
while (year != 2019):

    if (year == 2015):
        year_page = 16
    if (year == 2016):
        year_page = 19
    if (year == 2017):
        year_page = 19
    if (year == 2018):
        year_page = 19

    while (j <= year_page):
        if (j == 0):
            page_url = ("http://58921.com/alltime/" + str(year))
        else:
            page_url = ("http://58921.com/alltime/" + str(year))
            str1 = '?page='
            str2 = str(j)
            page_url = page_url + str1 + str2

        Cookie = {'Hm_lvt_e71d0b417f75981e161a94970becbb1b': '1545562259, 1545645424',
                  ' DIDA642a4585eb3d6e32fdaa37b44468fb6c': 'tpeluumqiu25hl55laa3947fk1',
                  'remember':'0',
                  'time': 'MTEzNTI2LjIxNjM0Mi4xMDI4MTYuMTA3MTAwLjExMTM4NC4yMDc3NzQuMTE5OTUyLjExMTM4NC4xMDQ5NTguMTEzNTI2LjExMTM4NC4xMTM1MjYuMTE1NjY4LjExMTM4NC4xMTU2NjguMTE1NjY4LjExMzUyNi4xMjIwOTQuMA % 3D % 3D',
                  'Hm_lpvt_e71d0b417f75981e161a94970becbb1b': '1545646661'}
        R = requests.get(page_url, cookies=Cookie)
        # print(type(R))
        print(R)
        # if has Chinese, apply decode()
        R.encoding = R.apparent_encoding
        html = R.text  # http://58921.com/?page=1&1                     urllib.request.urlopen(request)
        # print(html)                                                   #可查看html中的内容

        soup = BeautifulSoup(html, features='lxml')
        # print (soup.prettify())                  #格式化打印soup对象内容

        # 电影条目在58921.com中术语的类别 tr class有两种  分别为odd （奇数）和 even （偶数）
        j += 1
        i = 0
        tr_oddlist = soup.find_all('tr', attrs={'class': re.compile("(odd)|()")})
        for trtag in tr_oddlist:
            print('当前排行页面为:%d'%(j))
            print("当前爬取页面为：%s" % page_url)
            i += 1
            movie_num = (20 * (j - 1) + i + movie_sum)
            tdlist = trtag.find_all('td')                            # 在每个tr_odd标签下,查找所有的td标签
            print(tdlist[0].string)                                  # 年度排名         爬虫成功
            print(tdlist[1].string)                                  # 历史排名         爬虫成功
            if (tdlist[2].string == None):
                print("第%d 个电影爬取失败" % movie_num)
                continue

            print(tdlist[2].string)                                  # 电影名称          爬虫成功
            movie_data[1] = tdlist[2].string                                                                            #movie_data[1]：电影名称
            movie_url = trtag.find('a').get('href')                  # movie_url形如 /film/4211
            movie_data[0]=movie_url                                                                                     #movie_data[0]:电影具体页面url
            moviepage = urljoin(host, movie_url)
            # print(movie_url)
            print(moviepage)  # 电影具体页面进入成功
            moviepage_html = urlopen(moviepage).read().decode('utf-8')  # http://58921.com/+movie_url
            page_soup = BeautifulSoup(moviepage_html, features='lxml')
            # print (page_soup.prettify())                               #此处可看到具体网页的具体格式
            media_infor_board = page_soup.find('ul',
                                               class_='dl-horizontal content_view_fields content_view_film_fields')
            media_list = media_infor_board.find_all('li')

            if (len(media_list) != 7):
                print("第%d 个电影爬取失败" % movie_num)
                fail_sum += 1
                continue
            # print(media_list[0])
            # print(media_list[1])
            print(media_list[1].get_text())
            director_list = media_list[1].find_all(href=re.compile("/name/"))  # 返回所有href属性包含/name/的标签
            director_sum = len(director_list)
            if(director_sum==0):
                print("第%d 个电影爬取失败" % movie_num)
                fail_sum += 1
                continue
            print_director(director_sum)                                       # 导演            爬虫成功
            # print(media_list[2])                                              查看主演部分html代码
            # print(media_list[2].get_text())
            player_list = media_list[2].find_all(href=re.compile("/name/"))    # 返回所有href属性包含/name/的标签
            player_sum = len(player_list)
            print("演员总数为：%d" % player_sum)
            print_player(player_sum)                                           # 主演           爬虫成功

            # print(media_list[2].get_text())
            # print(media_list[3])                                            #查看上映时间部分html代码
            print(media_list[3].get_text()[5:])                               # 上映时间       爬虫成功
            if(media_list[3].get_text()[5:]==''):
                print('i am here!!!!assssshole!!!!!')
                print("第%d 个电影爬取失败" % movie_num)
                fail_sum += 1
                continue

            divided_time_list=media_list[3].get_text()[5:].split('-')

            print(divided_time_list[0])
            print(divided_time_list[1])
            print(divided_time_list[2])
            movie_data[7] = divided_time_list[0]
            '''try:
                movie_data[8]
            except IndexError:
                print(movie_data)'''
            print(movie_data[8])
            movie_data[8] = divided_time_list[1]
            movie_data[9] = divided_time_list[2]

            print(media_list[4].get_text()[3:])                             # 片长           爬虫成功
            print(media_list[5].get_text()[8:])                             # 制作国家/地区  爬虫成功
            print(media_list[6].get_text())
            type_list = media_list[6].find_all(href=re.compile("/tag/film/"))  # 返回所有href属性包含/name/的标签
            type_sum = len(type_list)
            print_type(type_sum)                                            # 类型           爬虫成功
            print(moviepage)
            movie_ticket_page = str(moviepage) + str("/boxoffice")
            # print(movie_ticket_page)                                      #此处为实时票房具体所在页面
            print(get_ticket(movie_ticket_page))                            # 票房             爬虫成功
            print("第%d 个电影爬取成功" % movie_num)
            k=0
            print("开始打印 movie_data序列")

            m += 1
            while(k<14):
                print(movie_data[k])
                k+=1
            print("movie_data序列开始插入到数据库中")
            print(m)
            # 插入数据                                                         #插入成功
            sql_insert = '''insert into movies_table(movies_url,movies_name,movies_director01,movies_director02,movies_actor01,movies_actor02,movies_actor03,movies_year,movies_month,movies_day,movies_boxoffice,movies_type01,movies_type02,movies_type03) values ( '%s', '%s', '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s' )'''

            try:  # 传的值要求严格符合要求     values（1,2,3,4）  values（'m',2,3,4）    ( '%s', '%s', %.2f )
                # 执行sql
                data = (
                movie_data[0], movie_data[1], movie_data[2], movie_data[3], movie_data[4], movie_data[5], movie_data[6], movie_data[7],
                movie_data[8], movie_data[9], movie_data[10], movie_data[11], movie_data[12], movie_data[13])
                cursor.execute(sql_insert % data)
                db.commit()
                print("插入数据成功")
            except:
                # 发生异常
                print('这里错了')
                db.rollback()


            with open("after_movies.csv", 'a') as f:  # 采用b的方式处理可以省去很多问题
                writer = csv.writer(f)
                writer.writerow(movie_data)
            movie_data = ['', '', '', '', '', '', '', '', '', '', '','','','']

            print(len(movie_data))

            print("\n\n\n")

    movie_sum = movie_num
    if j > year_page:
        j = 0
    year += 1

print("爬取失败电影数目为：%d" % fail_sum)

#关闭连接
db.close()

