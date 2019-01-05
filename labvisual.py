#coding=UTF-8
import pymysql
import pyecharts
from pyecharts import Line
from pyecharts import WordCloud
from pyecharts import Funnel
import pdfkit

# 打开数据库 （如果连接失败会报错）
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='Oracle19990112', db='movies_database', charset="utf8")
# 获取游标对象
cursor = db.cursor()
# 编写sql查询操作语句
sql_select = '''select * from movies_table'''

#作为pdfkit方法的参数，列表里存储着需要报表的html文件名
pdflist=[]

five_top_name=[]
five_top_value=[]
six_top_name=[]
six_top_value=[]
seven_top_name=[]
seven_top_value=[]
eight_top_name=[]
eight_top_value=[]
fivemonth_ticket = [0,0,0,0,0,0,0,0,0,0,0,0]
sixmonth_ticket = [0,0,0,0,0,0,0,0,0,0,0,0]
sevenmonth_ticket = [0,0,0,0,0,0,0,0,0,0,0,0]
eightmonth_ticket = [0,0,0,0,0,0,0,0,0,0,0,0]
movies_url=[]
movies_name=[]
movies_name02=[]
movies_director01=[]
movies_director02=[]

movies_actor01=[]
movies_actor01_02=[]
movies_actor02=[]
movies_actor02_02=[]
movies_actor03=[]
movies_actor03_02=[]

movies_year=[]
movies_year02=[]
movies_month=[]
movies_day=[]

movies_boxoffice=[]
movies_boxoffice02=[]
movies_boxoffice03=[]

movies_type01=[]
movies_type01_02=[]
movies_type02=[]
movies_type02_02=[]
movies_type03=[]
movies_type03_02=[]

#将数据库中数据转移到14个列表中 对应movies_database数据库中movies_table 14个属性
try:
    # 执行sql语句
    cursor.execute(sql_select)
    # 获取所有记录列表
    result = cursor.fetchall()
    i=1
    for row in result:
        print('第%d条数据载入成功'%i)
        movies_url.append(row[0])

        movies_name.append(row[1])
        movies_name02.append(row[1])

        movies_director01.append(row[2])
        movies_director02.append(row[3])

        movies_actor01.append(row[4])
        movies_actor01_02.append(row[4])

        movies_actor02.append(row[5])
        movies_actor02_02.append(row[5])

        movies_actor03.append(row[6])
        movies_actor03_02.append(row[6])

        movies_year.append(row[7])
        movies_year02.append(row[7])

        movies_month.append(row[8])

        movies_day.append(row[9])

        movies_boxoffice.append(row[10])

        movies_boxoffice02.append(row[10])

        movies_boxoffice03.append(row[10])

        movies_type01.append(row[11])
        movies_type01_02.append(row[11])

        movies_type02.append(row[12])
        movies_type02_02.append(row[12])

        movies_type03.append(row[13])
        movies_type03_02.append(row[13])
        #注释部分代码可以测试选取数据的内容
        #print("movies_url = %s, movies_name = %s,movies_year = %s" % (movies_url[i - 1], movies_name[i - 1], movies_year[i - 1]))
        #print("movies_url = %s, movies_name = %s,movies_year = %s" % (movies_url, movies_name,movies_year))
        i+=1
except:
    print("Error: unable to fecth data")
print("end")
# 关闭连接
db.close()


movies_sum=i-1

#获得合理输入
input_year= input("请输入年份（小写数字）：")
while(input_year!='2015')&(input_year!='2016')&(input_year!='2017')&(input_year!='2018'):
    input_year = input("输入不合法！！！\n\n请输入年份（小写数字）：")
input_month=input("请输入月份（小写数字）：")
while(input_month!='1')&(input_month!='2')&(input_month!='3')&(input_month!='4')&(input_month!='5')&(input_month!='6')&(input_month!='7')&(input_month!='8')&(input_month!='9')&(input_month!='10')&(input_month!='11')&(input_month!='12'):
    input_month = input("输入不合法！！！\n\n请输入月份（小写数字）：")

#将票房有字符型转为数字存储在movies_boxoffice02  movies_boxoffice03列表中
j=1
while(j<=movies_sum):
    if (movies_boxoffice02[j - 1][-1:] == '亿'):
        movies_boxoffice02[j - 1]=int(float(movies_boxoffice02[j - 1][:-1])*100000000)
        movies_boxoffice03[j - 1] = int(float(movies_boxoffice03[j - 1][:-1]) * 100000000)
    else :
        if(movies_boxoffice02[j - 1][-1:] == '万'):
            movies_boxoffice02[j - 1] = int(float(movies_boxoffice02[j - 1][:-1]) * 10000)
            movies_boxoffice03[j - 1] = int(float(movies_boxoffice03[j - 1][:-1]) * 10000)
        else:
            movies_boxoffice02[j - 1] = int(float(movies_boxoffice02[j - 1][:-1]) * 1)
            movies_boxoffice03[j - 1] = int(float(movies_boxoffice03[j - 1][:-1]) * 1)
    j+=1
#此处可以接触注释检查列表
#print(movies_boxoffice02)
#print(movies_boxoffice03)
#print(movies_year)


def show_ticket(input_year,input_month):
    j=1
    ticket_sum=0
    while(j<=movies_sum):
        if(movies_year[j-1]==input_year):
            ticket_sum+=movies_boxoffice02[j-1]
        j += 1
    print("%s票房总额为%d元"%(input_year,ticket_sum))


show_ticket(input_year,input_month)

#print(movies_month)     检查movies_month列表

#生成各年各月所得票房
j=1
while(j<=movies_sum):
    if (movies_year[j - 1] == '2015'):
            if(movies_month[j - 1]=='01'):
                fivemonth_ticket[0] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '02'):
                fivemonth_ticket[1] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '03'):
                fivemonth_ticket[2] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '04'):
                fivemonth_ticket[3] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '05'):
                fivemonth_ticket[4] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '06'):
                fivemonth_ticket[5] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '07'):
                fivemonth_ticket[6] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '08'):
                fivemonth_ticket[7] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '09'):
                fivemonth_ticket[8] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '10'):
                fivemonth_ticket[9] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '11'):
                fivemonth_ticket[10] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '12'):
                fivemonth_ticket[11] += movies_boxoffice02[j - 1]

    if (movies_year[j - 1] == '2016'):
            if(movies_month[j - 1]=='01'):
                sixmonth_ticket[0]+=movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '02'):
                sixmonth_ticket[1] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '03'):
                sixmonth_ticket[2] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '04'):
                sixmonth_ticket[3] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '05'):
                sixmonth_ticket[4] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '06'):
                sixmonth_ticket[5] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '07'):
                sixmonth_ticket[6] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '08'):
                sixmonth_ticket[7] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '09'):
                sixmonth_ticket[8] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '10'):
                sixmonth_ticket[9] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '11'):
                sixmonth_ticket[10] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '12'):
                sixmonth_ticket[11] += movies_boxoffice02[j - 1]

    if (movies_year[j - 1] == '2017'):
            if(movies_month[j - 1]=='01'):
                sevenmonth_ticket[0]+=movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '02'):
                sevenmonth_ticket[1] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '03'):
                sevenmonth_ticket[2] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '04'):
                sevenmonth_ticket[3] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '05'):
                sevenmonth_ticket[4] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '06'):
                sevenmonth_ticket[5] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '07'):
                sevenmonth_ticket[6] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '08'):
                sevenmonth_ticket[7] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '09'):
                sevenmonth_ticket[8] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '10'):
                sevenmonth_ticket[9] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '11'):
                sevenmonth_ticket[10] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '12'):
                sevenmonth_ticket[11] += movies_boxoffice02[j - 1]

    if (movies_year[j - 1] == '2018'):
            if(movies_month[j - 1]=='01'):
                eightmonth_ticket[0]+=movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '02'):
                eightmonth_ticket[1] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '03'):
                eightmonth_ticket[2] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '04'):
                eightmonth_ticket[3] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '05'):
                eightmonth_ticket[4] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '06'):
                eightmonth_ticket[5] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '07'):
                eightmonth_ticket[6] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '08'):
                eightmonth_ticket[7] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '09'):
                eightmonth_ticket[8] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '10'):
                eightmonth_ticket[9] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '11'):
                eightmonth_ticket[10] += movies_boxoffice02[j - 1]
            if (movies_month[j - 1] == '12'):
                eightmonth_ticket[11] += movies_boxoffice02[j - 1]
    j+=1


print("\n\n2015至2018年各月所的票房收集完成")
print(fivemonth_ticket)
print(sixmonth_ticket)
print(sevenmonth_ticket)
print(eightmonth_ticket)




#用pyecharts进行可视化

#attr为折线图 横轴 区间段名称
attr = ["1月", "2月", "3月", "4月", "5月", "6月","7月","8月","9月","10月","11月","12月"]

line01 = Line("2015~2016各月票房变化趋势")
line01.add("2015", attr, fivemonth_ticket, is_smooth=True,mark_line=["max", "average"])
line01.add("2016", attr, sixmonth_ticket, is_smooth=True,mark_line=["max", "average"])
line01.render('1516_month_boxoffice.html')
pdflist.append('1516_month_boxoffice.html')

line01

line02 = Line("2017~2018各月票房变化趋势")
line02.add("2017", attr, sevenmonth_ticket, is_smooth=True,mark_line=["max", "average"])
line02.add("2018", attr, eightmonth_ticket, is_smooth=True,mark_line=["max", "average"])
#line.add("2016", attr, sixmonth_ticket, is_smooth=True,mark_line=["max", "average"])   is smooth=True代表曲线平滑   mark_line=["max", "average"]代表在折线图中添加横州的平行线  高度如参
line02.render('1718_month_boxoffice.html')
pdflist.append('1718_month_boxoffice.html')

line02

#月份票房可视化成功





#生成年度top10
l = len(movies_boxoffice03)
j = 0
for i in range(1, l):
    boxoffice_temp = movies_boxoffice03[i]
    name_temp = movies_name02[i]
    year_temp =movies_year02[i]
    actor01_temp = movies_actor01_02[i]
    actor02_temp = movies_actor02_02[i]
    actor03_temp = movies_actor03_02[i]

    type01_temp = movies_type01_02[i]
    type02_temp = movies_type02_02[i]
    type03_temp = movies_type03_02[i]
    for j in range(i - 1, -1, -1):
        if boxoffice_temp < movies_boxoffice03[j]:                        # 如果第i个元素大于前i个元素中的第j个
            movies_boxoffice03[j + 1] = movies_boxoffice03[j]             # 则第j个元素先后移1位
            movies_name02[j+1]=movies_name02[j]                           # 根据票房排列电影名称
            movies_year02[j + 1] = movies_year02[j]                       # 根据票房排列电影发行年份

            movies_actor01_02[j + 1]=movies_actor01_02[j]                 # 根据票房排列演员
            movies_actor02_02[j + 1] = movies_actor02_02[j]
            movies_actor03_02[j + 1] = movies_actor03_02[j]

            movies_type01_02[j + 1] = movies_type01_02[j]                 # 根据票房排列电影题材
            movies_type02_02[j + 1] = movies_type02_02[j]
            movies_type03_02[j + 1] = movies_type03_02[j]

        else:  # 如果第i个元素小于等于前i个元素中的第j个则结束循环
            break
    movies_boxoffice03[j + 1] = boxoffice_temp  # 将i个元素赋值给空着的位置
    movies_name02[j + 1] = name_temp
    movies_year02[j + 1] = year_temp

    movies_actor01_02[j + 1] = actor01_temp  # 生成演员劳模
    movies_actor02_02[j + 1] = actor02_temp
    movies_actor03_02[j + 1] = actor03_temp

    movies_type01_02[j + 1] = type01_temp  # 根据票房排列电影题材
    movies_type02_02[j + 1] = type02_temp
    movies_type03_02[j + 1] = type03_temp






movies_boxoffice03 = list(reversed(movies_boxoffice03))
movies_name02 = list(reversed(movies_name02))
movies_year02 = list(reversed(movies_year02))
movies_actor01_02 = list(reversed(movies_actor01_02))
movies_actor02_02 = list(reversed(movies_actor02_02))
movies_actor03_02 = list(reversed(movies_actor03_02))

movies_type01_02 = list(reversed(movies_type01_02))
movies_type02_02 = list(reversed(movies_type02_02))
movies_type03_02 = list(reversed(movies_type03_02))


top2015_sum=0
top2016_sum=0
top2017_sum=0
top2018_sum=0
i=1
while(i<=1025):
    if movies_year02[i-1]=='2015':
        top2015_sum+=1
        five_top_name.append(movies_name02[i-1])
        five_top_value.append(movies_boxoffice03[i-1])

    if movies_year02[i-1]=='2016':
        top2016_sum+=1
        six_top_name.append(movies_name02[i-1])
        six_top_value.append(movies_boxoffice03[i-1])

    if movies_year02[i-1]=='2017':
        top2017_sum+=1
        seven_top_name.append(movies_name02[i-1])
        seven_top_value.append(movies_boxoffice03[i-1])

    if movies_year02[i-1]=='2018':
        top2018_sum+=1
        eight_top_name.append(movies_name02[i-1])
        eight_top_value.append(movies_boxoffice03[i-1])

    i+=1

print("根据票房排序已完成！！！")
print("\n\n15年演员票房排序：\n")
print(five_top_name)
print(five_top_value)
print("\n\n16年演员票房排序：\n")
print(six_top_name)
print(six_top_value)
print("\n\n17年演员票房排序：\n")
print(seven_top_name)
print(seven_top_value)
print("\n\n18年演员票房排序：\n")
print(eight_top_name)
print(eight_top_value)

#年度排序成功


#生成词云
print("\n\n现在开始生成词云！！！")
input_year= input("请输入年份（小写数字）：")
while(input_year!='2015')&(input_year!='2016')&(input_year!='2017')&(input_year!='2018'):
    input_year = input("输入不合法！！！\n\n请输入年份（小写数字）：")


input_wordcloud_sum=input("请输入你想选择词云的数量（ 15 30 100）：")
while(input_wordcloud_sum!='15')&(input_wordcloud_sum!='30')&(input_wordcloud_sum!='100'):
    input_wordcloud_sum = input("输入不合法！！！\n\n请输入你想选择词云的数量（ 15 30 100）：")


if input_year=='2015':
    wordcloud = WordCloud(width=1000, height=1000)
    wordcloud.add("top"+input_wordcloud_sum, five_top_name[:int(input_wordcloud_sum)], five_top_value[:int(input_wordcloud_sum)], shape='triangle-forward', word_size_range=[25, 80])
    wordcloud.render("2015年" + "top" + input_wordcloud_sum + "词云.html")

    pdflist.append("2015年" + "top" + input_wordcloud_sum + "词云.html")

    wordcloud.render(path="2015年" + "top" + input_wordcloud_sum + "词云.png", pixel_ratio=3)
    print("2015年"+"Top"+input_wordcloud_sum+"词云生成完毕\n\n")
if input_year=='2016':
    wordcloud = WordCloud(width=1000, height=1000)
    wordcloud.add("top"+input_wordcloud_sum, six_top_name[:int(input_wordcloud_sum)], six_top_value[:int(input_wordcloud_sum)], shape='triangle-forward', word_size_range=[25, 80])
    wordcloud.render("2016年" + "top" + input_wordcloud_sum + "词云.html")

    pdflist.append("2016年" + "top" + input_wordcloud_sum + "词云.html")

    wordcloud.render(path="2016年" + "top" + input_wordcloud_sum + "词云.png", pixel_ratio=3)
    print("2016年" + "Top" + input_wordcloud_sum + "词云生成完毕\n\n")
if input_year=='2017':
    wordcloud = WordCloud(width=1000, height=1000)
    wordcloud.add("top"+input_wordcloud_sum, seven_top_name[:int(input_wordcloud_sum)], seven_top_value[:int(input_wordcloud_sum)], shape='triangle-forward', word_size_range=[25, 80])
    wordcloud.render("2017年" + "top" + input_wordcloud_sum + "词云.html")

    pdflist.append("2017年" + "top" + input_wordcloud_sum + "词云.html")


    wordcloud.render(path="2017年" + "top" + input_wordcloud_sum + "词云.png", pixel_ratio=3)
    print("2017年" + "Top" + input_wordcloud_sum + "词云生成完毕\n\n")
if input_year=='2018':
    wordcloud = WordCloud(width=1000, height=1000)
    wordcloud.add("top"+input_wordcloud_sum, eight_top_name[:int(input_wordcloud_sum)], eight_top_value[:int(input_wordcloud_sum)], shape='triangle-forward', word_size_range=[25, 80])
    wordcloud.render("2018年"+"top" + input_wordcloud_sum + "词云.html")

    pdflist.append("2018年" + "top" + input_wordcloud_sum + "词云.html")

    wordcloud.render(path="2018年"+"top" + input_wordcloud_sum + "词云.png", pixel_ratio=3)
    print("2018年" + "Top" + input_wordcloud_sum + "词云生成完毕\n\n")




#生成劳模演员


'''pie = pyecharts.Pie("top劳模演员",title_pos='center')                     此部分代码为生成劳模主演
kwargs = dict(
    radius = (40,75),
    label_text_color = None,
    is_label_show = True,
    legend_orient = 'vertical',
    legend_pos = 'left'
)
pie.add("",movies_actor01_02[:16],movies_boxoffice03[:16],**kwargs)
pie.render("top劳模演员.html")'''

#解除代码可以检测年度演员排序
#print(movies_actor01_02[:16])
#print(movies_actor02_02[:16])
#print(movies_actor03_02[:16])


movies_all_actor=[]
movies_all_actor_boxoffice=[]
i=1
while(i<=15):
    movies_all_actor.append(movies_actor01_02[i - 1])
    movies_all_actor.append(movies_actor02_02[i - 1])
    movies_all_actor.append(movies_actor03_02[i - 1])
    movies_all_actor_boxoffice.append(movies_boxoffice03[i - 1])
    movies_all_actor_boxoffice.append(movies_boxoffice03[i - 1])
    movies_all_actor_boxoffice.append(movies_boxoffice03[i - 1])
    i+=1

#解除注释检查数量
#print(len(movies_all_actor))
#print(len(movies_all_actor_boxoffice))



input_actor_sum= input("请输入你想选择的劳模演员top数量（3  5  7  9  15 ）:")

while(input_actor_sum!='3')&(input_actor_sum!='5')&(input_actor_sum!='7')&(input_actor_sum!='9')&(input_actor_sum!='15'):
    print("输入不合法!!!")
    input_actor_sum = input("请输入你想选择的劳模演员top数量（3  5  7  9  15 ）:")



pieact = pyecharts.Pie("top"+input_actor_sum+"劳模演员",title_pos='center')
kwargs = dict(
    radius = (70,75),
    label_text_color = None,
    is_label_show = True,
    legend_orient = 'vertical',
    legend_pos = 'left'
)
pieact.add("",movies_all_actor[:int(input_actor_sum)],movies_all_actor_boxoffice[:int(input_actor_sum)],**kwargs)
pieact.render("top"+input_actor_sum+"劳模演员.html")

pdflist.append("top"+input_actor_sum+"劳模演员.html")

print("\n\n"+"top"+input_actor_sum+"劳模演员.html已生成\n\n")


#电影题材top生成
input_type_sum= input("请输入你想选择的电影题材top数量（3  5  7  9  11  13 ）:")

while(input_type_sum!='3')&(input_type_sum!='5')&(input_type_sum!='7')&(input_type_sum!='9')&(input_type_sum!='11')&(input_type_sum!='13'):
    print("输入不合法!!!")
    input_type_sum = input("\n\n输入不合法！！！\n\n请输入你想选择的电影题材top数量（3  5  7  9  11  13 ）：")



movies_all_type=['动作','喜剧','爱情','家庭','剧情','动画','奇幻','科幻','冒险','恐怖','犯罪','惊悚','战争','悬疑','0']
type_ticket=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i=1
while(i<=15):                                           #题材票房列表中元素按照 动作  喜剧  爱情  家庭  剧情 动画 奇幻 科幻 冒险 恐怖  犯罪 惊悚  战争   悬疑   0顺序存储
    if movies_type01_02[i - 1] == '动作':
        type_ticket[0]+=movies_boxoffice03[i - 1]
    if movies_type01_02[i - 1] == '喜剧':
        type_ticket[1] += movies_boxoffice03[i - 1]
    if movies_type01_02[i - 1] == '爱情':
        type_ticket[2] += movies_boxoffice03[i - 1]
    if movies_type01_02[i - 1] == '家庭':
        type_ticket[3] += movies_boxoffice03[i - 1]
    if movies_type01_02[i - 1] == '剧情':
        type_ticket[4] += movies_boxoffice03[i - 1]
    if movies_type01_02[i - 1] == '动画':
        type_ticket[5] += movies_boxoffice03[i - 1]
    if movies_type01_02[i - 1] == '奇幻':
        type_ticket[6] += movies_boxoffice03[i - 1]
    if movies_type01_02[i - 1] == '科幻':
        type_ticket[7] += movies_boxoffice03[i - 1]
    if movies_type01_02[i - 1] == '冒险':
        type_ticket[8] += movies_boxoffice03[i - 1]
    if movies_type01_02[i - 1] == '恐怖':
        type_ticket[9] += movies_boxoffice03[i - 1]
    if movies_type01_02[i - 1] == '犯罪':
        type_ticket[10] += movies_boxoffice03[i - 1]
    if movies_type01_02[i - 1] == '惊悚':
        type_ticket[11] += movies_boxoffice03[i - 1]
    if movies_type01_02[i - 1] == '战争':
        type_ticket[12] += movies_boxoffice03[i - 1]
    if movies_type01_02[i - 1] == '悬疑':
        type_ticket[13] += movies_boxoffice03[i - 1]
    if movies_type01_02[i - 1] == '0':
        type_ticket[14] += movies_boxoffice03[i - 1]

#
    if movies_type02_02[i - 1] == '动作':
        type_ticket[0]+=movies_boxoffice03[i - 1]
    if movies_type02_02[i - 1] == '喜剧':
        type_ticket[1] += movies_boxoffice03[i - 1]
    if movies_type02_02[i - 1] == '爱情':
        type_ticket[2] += movies_boxoffice03[i - 1]
    if movies_type02_02[i - 1] == '家庭':
        type_ticket[3] += movies_boxoffice03[i - 1]
    if movies_type02_02[i - 1] == '剧情':
        type_ticket[4] += movies_boxoffice03[i - 1]
    if movies_type02_02[i - 1] == '动画':
        type_ticket[5] += movies_boxoffice03[i - 1]
    if movies_type02_02[i - 1] == '奇幻':
        type_ticket[6] += movies_boxoffice03[i - 1]
    if movies_type02_02[i - 1] == '科幻':
        type_ticket[7] += movies_boxoffice03[i - 1]
    if movies_type02_02[i - 1] == '冒险':
        type_ticket[8] += movies_boxoffice03[i - 1]
    if movies_type02_02[i - 1] == '恐怖':
        type_ticket[9] += movies_boxoffice03[i - 1]
    if movies_type02_02[i - 1] == '犯罪':
        type_ticket[10] += movies_boxoffice03[i - 1]
    if movies_type02_02[i - 1] == '惊悚':
        type_ticket[11] += movies_boxoffice03[i - 1]
    if movies_type02_02[i - 1] == '战争':
        type_ticket[12] += movies_boxoffice03[i - 1]
    if movies_type02_02[i - 1] == '悬疑':
        type_ticket[13] += movies_boxoffice03[i - 1]
    if movies_type02_02[i - 1] == '0':
        type_ticket[14] += movies_boxoffice03[i - 1]
#
    if movies_type03_02[i - 1] == '动作':
        type_ticket[0]+=movies_boxoffice03[i - 1]
    if movies_type03_02[i - 1] == '喜剧':
        type_ticket[1] += movies_boxoffice03[i - 1]
    if movies_type03_02[i - 1] == '爱情':
        type_ticket[2] += movies_boxoffice03[i - 1]
    if movies_type03_02[i - 1] == '家庭':
        type_ticket[3] += movies_boxoffice03[i - 1]
    if movies_type03_02[i - 1] == '剧情':
        type_ticket[4] += movies_boxoffice03[i - 1]
    if movies_type03_02[i - 1] == '动画':
        type_ticket[5] += movies_boxoffice03[i - 1]
    if movies_type03_02[i - 1] == '奇幻':
        type_ticket[6] += movies_boxoffice03[i - 1]
    if movies_type03_02[i - 1] == '科幻':
        type_ticket[7] += movies_boxoffice03[i - 1]
    if movies_type03_02[i - 1] == '冒险':
        type_ticket[8] += movies_boxoffice03[i - 1]
    if movies_type03_02[i - 1] == '恐怖':
        type_ticket[9] += movies_boxoffice03[i - 1]
    if movies_type03_02[i - 1] == '犯罪':
        type_ticket[10] += movies_boxoffice03[i - 1]
    if movies_type03_02[i - 1] == '惊悚':
        type_ticket[11] += movies_boxoffice03[i - 1]
    if movies_type03_02[i - 1] == '战争':
        type_ticket[12] += movies_boxoffice03[i - 1]
    if movies_type03_02[i - 1] == '悬疑':
        type_ticket[13] += movies_boxoffice03[i - 1]
    if movies_type03_02[i - 1] == '0':
        type_ticket[14] += movies_boxoffice03[i - 1]


    i+=1

l = len(type_ticket)
for i in range(1, l):
    type_ticket_temp = type_ticket[i]
    all_type_name_temp = movies_all_type[i]
    for j in range(i - 1, -1, -1):
        if type_ticket_temp <type_ticket[j]:                        # 如果第i个元素大于前i个元素中的第j个
            type_ticket[j + 1] = type_ticket[j]                     # 则第j个元素先后移1位
            movies_all_type[j+1]=movies_all_type[j]                 # 根据题材票房排列题材名称


        else:  # 如果第i个元素小于等于前i个元素中的第j个则结束循环
            break
    type_ticket[j + 1] = type_ticket_temp  # 将i个元素赋值给空着的位置
    movies_all_type[j+1]=all_type_name_temp

type_ticket = list(reversed(type_ticket))
movies_all_type= list(reversed(movies_all_type))

#空缺题材'0'无意义  故在列表中删去
zero_location=movies_all_type.index('0')
del movies_all_type[zero_location]
del type_ticket[zero_location]

#生成电影题材top
pie = pyecharts.Pie("top"+input_type_sum+"电影题材",title_pos='center')
kwargs = dict(
    radius = (50,75),
    label_text_color = None,
    is_label_show = True,
    legend_orient = 'vertical',
    legend_pos = 'left'
)
pie.add("",movies_all_type[:int(input_type_sum)],type_ticket[:int(input_type_sum)],**kwargs)
pie.render("top"+input_type_sum+"电影题材.html")

pdflist.append("top"+input_type_sum+"电影题材.html")

print("\n\n"+"top"+input_type_sum+"电影题材.html已生成\n\n")


line01.render(path='1516_month_boxoffice.png', pixel_ratio=3)
line02.render(path='1718_month_boxoffice.png', pixel_ratio=3)
pie.render(path="top"+input_type_sum+"电影题材.png", pixel_ratio=3)
pieact.render(path="top"+input_actor_sum+"劳模演员.png", pixel_ratio=3)


#生成报表功能
input_choose= input("是否打印报表y/n")

while(input_choose!='y')&(input_choose!='Y')&(input_choose!='N')&(input_choose!='n'):
    print("输入不合法!!!")
    input_choose = input("是否打印报表y/n")

if (input_choose!='y')or(input_choose!='Y'):
    # 根据pdflist中存储的各html文件名开始生成pdf报表

    print("请确保文件夹中没有同名文件htmlout.pdf！！！\n")

    options00 = {
        'page-size': 'Letter',
        'margin-top': '0.25mm',
        'margin-right': '0.25mm',
        'margin-bottom': '0.25mm',
        'margin-left': '0.25mm',
        'encoding': "UTF-8",
        'no-outline': None,
        'page-size': 'A4'
    }

    pdfkit.from_url(pdflist, 'htmlout.pdf', options=options00)
    print("程序结束  欢迎再次使用")
else:
    exit("程序结束  欢迎再次使用")


































