# -


具体README文件见同名docx文件
电影数据分析系统

一：py文件功能介绍：


1.Scrapy58921.py：

从58921.com电影网站上爬取2015年至2018年数据并按照规定格式存储到MySQL指定数据库中


2.labvisual.py ：

在数据爬取并存储完毕后，可以对存储在数据库中的电影数据进行排序以及可视化处理，pyecharts可视化自动生成的html分别为：  
1516_month_boxoffice.html   
1718_month_boxoffice.html
根据用户输入内容，自动生成的html分别为：
（用户输入）年top（用户输入）词云.html
top（用户输入）电影题材.html
top（用户输入）劳模演员.html

通过phantomjs将生成的html文件转为png格式保存在同一文件路径下

通过pdfkit以及wkhtmltopdf工具将html文件转为pdf格式保存在同一文件路径下


3.movies_gui文件：
使用tkinter工具生成了一个可以账号密码登陆的图形界面






二：数据库注意事项


1.连接数据库具体方法：
在各py文件中
将代码db = pymysql.connect(host='localhost', port=3306, user='*****', passwd='*****', db='movies_database', charset="utf8")
*****处添加自己MySQL的账号以及密码
并手动建立名为movies_database的数据库





2.数据库中movies_table表形式按照特定方式构造




三：报表相关工具

用户需要自行下载安装phantomjs以及wkhtmltopdf工具

并且将bin文件的路径添加到计算机的环境变量中
phantomjs用于将html文件转为png文件
wkhtmltopdf用于将html文件转为pdf文件


















