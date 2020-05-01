# 该库用来响应网络get，post数据
from urllib.request import urlopen, Request
# 用来将html简化
from bs4 import BeautifulSoup

# 输入浏览器的信息，用户代理
headers = {'use-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'}
url = Request("https://www.zhipin.com/shenzhen/", headers=headers)
html = urlopen(url, timeout=150)

# 将获取的信息美化其格式
bs = BeautifulSoup(html)
# print(bs)

# 获取span标签下class="component-o"的数据
name_list = bs.findAll("span", {"class": "component-o"})
for name in name_list:
    print(name.get_text())

# 查找含有”数据“的标签页个数
name_list = bs.findAll(text="数据")
print(len(name_list))

# 获取工资salary标签里的数据
salary = bs.findAll(class_="salary")
for salary1 in salary:
    print(salary1.get_text())

# 获取工作列表中的所有职位
for job in bs.find("div", {"class": "job-menu"}).children:
    print(job)

# 获取列表中的兄弟标签【和上面标签使用于table表格数据收集】
for job1 in bs.find("div", {"class", "job-menu"}).p.next_siblings:
    print(job1)


