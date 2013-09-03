Douban-Common-Interests
=======================

A python script to dig out those who share most interests with you on Douban.

这是一个从豆瓣所有用户列表中寻找“共同爱好”最多的友邻的爬虫脚本，也是我的第一个python脚本。要求使用python3 环境运行。
在文件开头可以设置：  

  username='xxxxxxx' #豆瓣用户名  
  password='xxxxxxx' #豆瓣密码  
  log_file_name='log.txt' #记录文件  
  COUNT=100 #每搜索多少用户保存并排序  
  ALOT=12 #大于多少共同爱好的用户会直接在浏览器打开他的主页  
  start=1000001 #搜索用户起始ID，豆瓣ID从1000001开始，目前由七位或八位数字组成，现在ID大约注册到80000000  
  stop=80000000 #终止ID  

搜索完全部豆瓣ID所花的时间还是非常长的，大约需要一百天的量级。所以，碰碰运气吧:)
