import time


def detect_holding(driver, url):
    driver.get(url)
    time.sleep(2)
    while True:
        try:
            # 先找到价格，判断买入价格是否小于等于0.00025000，不是的跳过并关闭网页，是的继续检测是否持有
            buy_button = driver.find_element_by_xpath("//button[@class='custom-button main-tab items-center self-start "
                                                  "rounded-md border bg-light-primary px-4 py-1.5 font-bold text-white  "
                                                  "hover:bg-light-primary/90 focus-visible:bg-light-primary/90 "
                                                  "active:bg-light-border/75  dark:bg-light-border "
                                                  "dark:text-light-primary dark:hover:bg-light-border/90  "
                                                  "dark:focus-visible:bg-light-border/90 dark:active:bg-light-border/75 "
                                                  "']")
            # 点击buy按钮
            buy_button.click()
            break
        except BaseException:
            pass

    # 检测当前价格
    time.sleep(2)
    while True:
        try:
            time.sleep(1)
            buy_price = driver.find_element_by_xpath("//div[@class='main-text-success']").text
            print(buy_price, type(buy_price))
            price_float = float(buy_price.split(' ', 1)[0])
            print(price_float)
            if price_float != 0.00000000:
                break
        except BaseException:
            pass

    # 买入价格等于0.00025000 ETH
    '''if 0.00006250 < price_float <= 0.00025:
        # 判断是否持有该用户的share
        holding_value_text = driver.find_element_by_xpath("//p[@class='text-base font-medium text-blue-500']").text
        print(holding_value_text)
        holding_value = int(holding_value_text.split(' ', 3)[2])
        print(holding_value)
        if 5 > holding_value > 0:      # 当前持有该用户share,则买入
            buy_button_green = driver.find_element_by_xpath("//button[@class='custom-button main-tab items-center "
                                                            "flex h-12 w-full flex-1 items-center justify-center "
                                                            "space-x-4 rounded-md bg-[var(--emerald-500,"
                                                            "#10B981)] p-3']")
            buy_button_green.click()
            time.sleep(1)
            buy_button_share = driver.find_element_by_xpath("//button[@class='custom-button main-tab items-center "
                                                            "flex h-12 w-full items-center justify-center space-x-4 "
                                                            "rounded-md bg-[var(--emerald-500,#10B981)] p-3']")
            buy_button_share.click()
            time.sleep(3)
            buy_share_confirm = driver.find_element_by_xpath("//button[@class='custom-button main-tab items-center "
                                                                     "rounded-base primary-bg-color-btn mt-4 w-full']")
            time.sleep(1)
            buy_share_confirm.click()  # 确认买入'''

    # 买入价格等于0.00006250 ETH
    if price_float <= 0.00025:
        buy_button_green = driver.find_element_by_xpath("//button[@class='custom-button main-tab items-center "
                                                        "flex h-12 w-full flex-1 items-center justify-center "
                                                        "space-x-4 rounded-md bg-[var(--emerald-500,"
                                                        "#10B981)] p-3']")
        buy_button_green.click()
        time.sleep(1)
        buy_button_share = driver.find_element_by_xpath("//button[@class='custom-button main-tab items-center "
                                                        "flex h-12 w-full items-center justify-center space-x-4 "
                                                        "rounded-md bg-[var(--emerald-500,#10B981)] p-3']")
        buy_button_share.click()
        time.sleep(3)
        buy_share_confirm = driver.find_element_by_xpath("//button[@class='custom-button main-tab items-center "
                                                         "rounded-base primary-bg-color-btn mt-4 w-full']")
        time.sleep(1)
        buy_share_confirm.click()  # 确认买入
