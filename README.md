# Get_PostTech_Points_Bot
A fully automated bot that can earn points by buying shares through the PostTech interface.
一个能通过posttech网站界面买入share来获得积分的全自动bot。

******************* 说明 ***********************

1.程序用到python selenium库，所以需要chromedriver,谷歌搜索chromedriver下载自己电脑的chrome浏览器对应版本的chromedriver即可；

2.get_driver中，直接使用用户自己的个人数据默认登录chrome，然后打开post.tech，开始之前，请先在自己的chrome浏览器上登录谷歌账号，然后登录post.tech；完成后，按照下面链接的教程获取当前谷歌账户的数据，以便于chromedriver会打开指定的谷歌账号。
https://www.cnblogs.com/roronoazoro77/p/16119485.html

3.代码结构：
    3.1 get_driver.py负责获取并返回driver
    3.2 buyin_interface包含检测是否持有当前用户的share，及获取页面上的share买入价格；其中的价格可自行修改。
    3.3 get_trade_data.py 控制程序运行

4.以上，玩得愉快！


******************* Introduction **********************
1. The program uses the python selenium library, so it requires chromedriver. Just search for chromedriver on Google and download the corresponding version of chromedriver for your computer's chrome browser;
2. In get_driver, directly use the user's own personal data to log in to chrome by default, and then open post.tech. Before starting, please log in to your Google account on your chrome browser, and then log in to post.tech; after completion, follow the link below The tutorial gets the data of the current Google account so that chromedriver will open the specified Google account.
https://www.cnblogs.com/roronoazoro77/p/16119485.html
3. Code structure:
     3.1 get_driver.py is responsible for obtaining and returning the driver
     3.2 buyin_interface includes detecting whether the current user's share is held and obtaining the share buying price on the page; the price can be modified by oneself.
     3.3 get_trade_data.py controls program execution
4. Have fun!
