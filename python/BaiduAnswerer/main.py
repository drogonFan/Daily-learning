from selenium import webdriver

import json, time

def login(driver):
    '''
    获取cookies保存到本地，之后使用
    '''
    url = 'https://www.baidu.com/'
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
    time.sleep(3)
    driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
    time.sleep(3)
    # 输入用户名和密码
    driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__userName"]').send_keys('account number')
    driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__password"]').send_keys('password')

    driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__submit"]').click()
    # 现在改成旋转验证码，手动操作（日后可以考虑添加验证码识别软件）
    time.sleep(10)
    try:
        # 有时会跳出短信验证码页面，需要手动输入
        driver.find_element_by_xpath('//*[@id="TANGRAM__28__button_send_mobile"]').click()
        code_photo = input('请输入短信验证码：')
        driver.find_element_by_xpath('//*[@id="TANGRAM__28__input_label_vcode"]').send_keys(str(code_photo))
        driver.find_element_by_xpath().cilck('//*[@id="TANGRAM__28__button_submit"]').click()
    except:
        pass

    # 将cookies保存到本地文件，之后就可以头疼呢过
    cookies = driver.get_cookies()
    with open('cookie.txt', 'w') as f:
        f.write(json.dumps(cookies))

def answerer(driver):
    '''
    获取问题，并且查找答案，然后回答问题
    '''
    url = 'https://zhidao.baidu.com/list?type=default&cid=110'
    driver.get(url)
    # 清空当前cookie
    driver.delete_all_cookies()
    cookie = {}
    # 从文件中读取出cookie
    with open('cookie.txt', 'r') as f:
        cookie = json.loads(f.read())
    print(cookie)
    for c in cookie:
        if 'expiry' in c:
            del c['expiry']
        driver.add_cookie(c)
    driver.refresh()

    # 从页面中获取链接
    title_links = driver.find_elements_by_class_name('title-link')

    for link in title_links:
        # 取出问题
        driver.switch_to.window(driver.window_handles[0])
        href = link.get_attribute('href')
        driver.execute_script('window.open("%s");' % (href))
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        try:
            # 准备朝找答案
            driver.find_element_by_id('ueditor_0')
            title = driver.find_element_by_class_name('ask-title').text
            title_url = 'https://zhidao.baidu.com/search?word=' + title

            js = 'window.open("%s");' % (title_url)
            driver.execute_script(js)
            time.sleep(5)
            # 切换至查找问题的页面
            driver.switch_to.window(driver.window_handles[2])
            answer_list = driver.find_elements_by_class_name('dt,mb-4,line')
            for k in answer_list:
                # 遍历答案详情
                href = k.find_element_by_tag_name('a').get_attribute('href')
                driver.execute_script('window.open("%s");' % (href))
                time.sleep(4)
                driver.switch_to.window(driver.window_handles[3])
                # 获取最佳答案
                try:
                    text = driver.find_element_by_class_name('best-text,nb-10').text
                except:
                    text = ''
                finally:
                    # 关闭窗口
                    driver.close()
                
                # 如果有获取到答案
                if text != '':
                    text += '\n, 希望我的回答能够帮到你。'
                    driver.switch_to.window(driver.window_handles[2])
                    driver.close()
                    driver.switch_to.window(driver.window_handles[1])
                    # 定位到答案的输入窗口
                    driver.switch_to.frame('ueditor_0')
                    driver.find_element_by_xpath('/html/body').click()
                    driver.find_element_by_xpath('/html/body').send_keys(text)
                    # 勾选上匿名选项
                    driver.switch_to.default_content()
                    driver.find_element_by_class_name('checkbox').click()
                    # 将答案写入
                    driver.find_element_by_xpath('//*[@id="answer-editor"]/div[2]/a').click()
                    time.sleep(5)
                    driver.switch_to.window(driver.window_handles[1])
                    driver.close()
                    break
                    

        except Exception as err:
            # 捕获到异常后，关闭除了问题列表页面的其他窗口（这暂时有问题）
            pass
            all_handles = driver.window_handles
            for i, v in enumerate(all_handles):
                if i != 0:
                    driver.switch_to.window(v)
                    driver.close()
            driver.switch_to.window(driver.window_handles[0])
            print(err)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    login(driver)
    answerer(driver)