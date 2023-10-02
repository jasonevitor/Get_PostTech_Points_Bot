from selenium import webdriver


def get_driver():
    # 获取当前数据
    usr_data_dic = r'C:\Users\Administrator\Desktop\qianglu_posttech\usr_data'
    argu = r'--user-data-dir=' + usr_data_dic

    options = webdriver.ChromeOptions()
    # 修改路径为自己的目录
    options.add_argument(argu)
    options.add_argument("--profile-directory=Profile 2")
    page_driver = webdriver.Chrome(options=options)

    return page_driver
