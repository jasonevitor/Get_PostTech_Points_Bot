import time
from get_driver import get_driver
from buyin_interface import detect_holding

driver = get_driver()


def login_chrome():
    driver.maximize_window()
    driver.get("https://post.tech/home")
    time.sleep(15)


# 检测交易数据板块是否有新数据
def detect_new():
    while True:
        try:
            find_trades = driver.find_element_by_xpath("//div[@class='ReactVirtualized__Grid__innerScrollContainer']").\
                find_elements_by_xpath("//a[@class='pl-1 underline text-red-500']")
            break
        except BaseException as e:
            print(f'查找最近交易出错，{e}')
            pass
    for find_trade in find_trades:  # 遍历所有找到的交易订单
        trade_data = find_trade.find_element_by_tag_name("div").text
        print(f'找到卖单: {trade_data}')
        if ('0.00006250' or '0.00000000') in trade_data:  # 检测当前价格是否是最低价，如果是，则返回该元素的index值
            index_num = find_trades.index(find_trade)
            # print(f'下标为{index_num}')
            while True:
                try:
                    usr_href = find_trade.find_elements_by_xpath("//div[@class='main-text-primary flex flex-wrap "
                                                                 "items-center font-normal']")[
                        index_num].find_elements_by_tag_name('a')[1].get_attribute("href")
                    break
                except BaseException as e:
                    print(f'查找最低价格的账户的链接部分出错，{e}')
                    pass
            print(usr_href)
            detect_holding(driver, usr_href)


if __name__ == "__main__":
    print('开始执行')
    login_chrome()
    while True:
        try:
            detect_new()
            print('执行完一次')
        except BaseException as e:
            print(e)
            pass
        time.sleep(1)
