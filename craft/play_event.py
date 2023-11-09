from selenium.webdriver.common.by import By
from selenium import webdriver



def is_element_exist(by, element, waittime = 10):
    #判断元素是否存在页面之上
    #存在返回t 不存在 None
    #by 查找方法，find_element的第一个参数，element是元素名称
    flag = False
    while True:
        try:
            flag = WebDriverWait(chm, waittime
                    ).until(
                    EC.presence_of_element_located((by, element))
                    )
                    #元素出现后的操作
            flag = True
            break
        except TimeoutException:
            break
        except WebDriverException:
            break
        except UnexpectedAlertPresentException:
            alert = chm.switch_to.alert
            print("alert txt : ", alert.text )
            alert.accept()
    return flag
    #最终返回flag


def home_page():
    chm.get(home_page_url)
    result = is_element_exist(By.ID,  "btm-campaign-toggle")
    #通过查找gameplayextras 判断是否已经跳转到主页
    if result:
        return True
    else:
        return False

def event_paly_page(url):
    times = 0
    while times < 3 :
        try:
            chm.get(url)
        except WebDriverException:
            print("webdriverexception")
            pass
        result = is_element_exist(By.CLASS_NAME, "prt-supporter-title")
        #通过判断是否存在choosesummon标签确定是否完成跳转
        if result:
            return True
            break
        else:
            print("reload url :", url)
            times  = times + 1
            return False

def click_friend_summon():
    x = 100
    y = 500
    time.sleep(random.random())
    pyautogui.click(x, y)

def click_arcum_part_ok():
    x = 300
    y = 600 
    x = int(random.random()*50) + x
    y = int(random.random()*10) + y
    #这里可以用rect的值来确定点击范围
    times = 0
    while times < 3:
        if is_element_exist(By.XPATH, '//div[@class="prt-btn-deck"]'):
            time.sleep(random.random())
            pyautogui.click(x, y)
            break
        else:
            print("click_party_ok erro : couldn't find prt-btn-deck")
            times = times + 1



def click_party_ok():
    x = 300
    y = 560
    x = int(random.random()*50) + x
    y = int(random.random()*10) + y
    #a = chm.find_element_by_class_name("prtbtn-deck")
    #rect = a.rect()
    #这里可以用rect的值来确定点击范围
    times = 0
    while times < 3:
        if is_element_exist(By.XPATH, '//div[@class="prt-btn-deck"]'):
            time.sleep(random.random())
            pyautogui.click(x, y)
            break
        else:
            print("click_party_ok erro : couldn't find prt-btn-deck")
            times = times + 1

def click_attack():
    element = '//div[@class="btn-attack-start display-on"]'
    by = By.XPATH
    flag = False
    if is_element_exist(by, element, 2):
        x = 280 + int(random.random() * 70)
        y = 380 + int(random.random() * 30)
        try:
            flag = WebDriverWait(chm, 10).until(
                    EC.element_to_be_clickable((by, element))
                    )
        except TimeoutException:
            pass

        finally:
            if flag:
                time.sleep(1.5 * random.random())
                pyautogui.click(x, y)
    else:
        print("click full erro: couldn't find attack-btn, retring...")
        click_attack()

def click_full():
    by = By.CLASS_NAME
    flag = False
    element = "btn-auto"
    if is_element_exist(By.CLASS_NAME, "btn-auto",waittime = 20):
        # chm.find_element_by_class_name("btn-auto").click()
        x = 85 + int(random.random() * 10)
        y = 410 + int(random.random() * 10)
        #pyautogui.click(x, y)
        times = 0 
        while times < 3:
            times = times + 1
            try:
                flag = WebDriverWait(chm, 10).until(
                        EC.element_to_be_clickable((by, element))
                        )
                flag = True
                break
            except TimeoutException:
                pass
            except WebDriverException:
                break
        
        if flag:
            time.sleep( 1.5 * random.random())
            pyautogui.click(x, y)
            if is_element_exist(By.CLASS_NAME,"prt-popup-header",1):
                txt = chm.find_element_by_class_name("prt-popup-header").text
                if re.match(txt, "Processing") and  re.match(txt, "Processing").span()[1] > 0:
                    refresh()
                    click_full()
    else:
        print("click full erro: couldn't find btn-auto")


def is_goal_page(waittime = 2):
    by = By.CLASS_NAME
    element = "cnt-get-experience"
    flag = False
    try:
        flag = WebDriverWait(chm, waittime ).until(
                EC.presence_of_element_located((by, element))
                )
                #元素出现后的操作
        flag = True
    except TimeoutException:
        pass


    if (not flag):
        url = chm.current_url
        if url:
            if re.match(url, "result"):
                flag = True
    return flag
       

def refresh(element =  '//div[@class="prt-command"]' , waittime = 10, by = By.XPATH):
    #通过判断页面刷新后是否存在element，决定刷新是否完成，by查找方式，waittime等待时间
    #默认element: '//div[@class="prt-command"]' waittime: 10s by: By.XPATH
    time.sleep(1.5 + 1 * random.random())
    chm.refresh()
    if is_element_exist(by, element, waittime):
        print("refresh finished")
    else:
        print("refresh erro")


def auto_refresh(single_battle_time_limit):
    start_time = time.time()
    end_time = time.time()
    while (not is_goal_page()) and end_time - start_time < single_battle_time_limit * 60:
        i = 0
        while i < 3:
            i = i + 1
            end_time = time.time()
            flag = False
            try:
                flag = WebDriverWait(chm, 2).until(
                        EC.presence_of_element_located((By.XPATH, '//div[@class="btn-attack-start display-off"]')
                            )
                        )
                print(flag)
                break
            except TimeoutException:
                pass
            #处理经常出现的那个app更新的弹窗
            except UnexpectedAlertPresentException:
                alert = chm.switch_to.alert
                print("alert text : ", alert.text)
                alert.accept()
        print("finally")
        if flag:
            refresh()
            click_full()

def connect_chrome():
    #连接到打开远程调试模式的chrome浏览器
    chrome_options = webdriver.ChromeOptions()
    chrome_options.debugger_address = chrome_remote_host
    global chm
    chm = webdriver.Chrome(options=chrome_options)


def auto_reverse(times = 50):
    i = int(input("input times pls: "))
    times = i
    print("1.autoreverse_weapon \n2.autoreverse_summon\n ")
    i = int(input("pls select: "))
    while times > 0:
        print("left times : ", times)
        times = times -1
        if i == 1:
            p1 = [220, 980]
            p2 = [260, 950]
            pyautogui.click(p1[0], p1[1])
            time.sleep(2)
            pyautogui.click(p2[0], p2[1])
            time.sleep(2)
            pyautogui.click(p2[0], p2[1])
            time.sleep(2)
            pyautogui.click(p2[0], p2[1])
            time.sleep(2)
        else:
            if i == 2:
                p1 = [215,1100]
                p2 = [300,840]
                p3 = [300,940]
                p4 = [250,910]
                p  = [p1, p2, p3, p4]
                for ii in p:
                    pyautogui.click(ii[0], ii[1])
                    time.sleep(2)




def is_battle_page():
    by = By.CLASS_NAME
    element = "prt-gauge-area"
    flag = False
    times = 0
    while times < 3:
        times = times + 1
        try:
            flag = WebDriverWait(chm, 5 ).until(
                    EC.presence_of_element_located((by, element))
                    )
            if flag:
                flag = True
                break
        except TimeoutException:
            pass

    return flag
    #最终返回flag



def play():
    single_battle_time_limit = 15
    #单场战斗时间最长设置为15分钟
    times = int(input("please input total times : "))
    connect_chrome()
    while times > 0 :
        times = times - 1
        check_stat()
        flag = True
        while flag:
            if not is_battle_page():
                event_paly_page(event_play_url)
                flag = False
        time.sleep(3)
        click_friend_summon()
        time.sleep(3)
        click_party_ok()
      #  time.sleep(8)
        click_full()
        auto_refresh(single_battle_time_limit)




#战车材料
def zhanche_play():
    connect_chrome()
    url = "https://game.granbluefantasy.jp/#quest/supporter/shop_treasure/1073/0/0/arcarum2!enhancement!detail!17/145/10/50"
    repeattimes = int(input("pls input repeattimes: "))
    battletimelimit = 2
    while repeattimes > 0:
        repeattimes = repeattimes - 1
        print("left times: ", repeattimes)
        flag = True
        while flag:
            if  not is_battle_page():
                event_paly_page(url)
                flag = False
        time.sleep(3)
        click_friend_summon()
        time.sleep(3)
        click_party_ok()
        click_full()
        start_time = time.time()
        end_time = time.time()
        flag = True
        while flag and (not is_goal_page()) and end_time - start_time < battletimelimit  * 60:
            while True:    
                end_time = time.time()
                flag = False
                try:
                    flag = WebDriverWait(chm, 2).until(
                            EC.presence_of_element_located((By.XPATH, '//div[@class="btn-attack-start display-off"]')
                                )
                            )
                    print(flag)
                    break
                except TimeoutException:
                    pass
                #处理经常出现的那个app更新的弹窗
                except UnexpectedAlertPresentException:
                    alert = chm.switch_to.alert
                    print("alert text : ", alert.text)
                    alert.accept()

            print("finally")
            if flag:
                refresh(waittime = 3)
                flag = False

def click_filter_battles_first():
    x = 200 + int(50 * random.random())
    y = 400 + int(50 * random.random())
    pyautogui.click(x, y)

def play_finder_filter1_1(repeat_times = 10):
#刷https://game.granbluefantasy.jp/#quest/assist页面的第一个过滤器的第一场战斗，就是多人战斗
    connect_chrome()
    url = "https://game.granbluefantasy.jp/#quest/assist"
    while repeat_times > 0:
        print("left times : ", repeat_times)
        repeat_times = repeat_times - 1
        event_paly_page(url)
        click_filter_battles_first()
        time.sleep(3)
        click_friend_summon()
        time.sleep(2)
        click_party_ok()
        if click_full():
            auto_refresh(10)
        else:
            if is_element_exist(By.CLASS_NAME, "txt-rematch-fail",10   ):
                repeat_times = repeat_times + 1



def play_arcum_icebergchampion():
    timelimit = 3
    url = "https://game.granbluefantasy.jp/#replicard/supporter/3/3/16/812121/25"
    play_common_arcum(url, timelimit )
    end_msgbox()

def play_common_arcum(url, battletimelimit,gauge_url):
#battletimelimit 单位为分钟
    connect_chrome()
    repeat_times = int(input("pls input repeat times :"))
    while repeat_times > 0:
        print("while loop start")
        repeat_times = repeat_times - 1
        print("left times : ", repeat_times)
        if event_paly_page(url):
            click_arcum_part_ok()
        if is_battle_page():
            click_full()
            auto_refresh(battletimelimit)
        print("auto refresh ended")
        check_and_play_arcum_gague(gauge_url)
    
        #  auto_refresh(battletime_limit)
#  common_play1('https://game.granbluefantasy.jp/#quest/supporter/shop_treasure/400471/5/0/arcarum2!enhancement!detail!17/5111/10/25', 100, 1)


def play_halloween_rapid(times = 5):
    url = "https://game.granbluefantasy.jp/#quest/supporter/909661/1"
    battle_limit_time = 60
    #单次战斗最多持续60s
    connect_chrome()
    while times > 0 :
        times = times - 1 
        print("left times :",  times)
        #打开网页
        if event_paly_page(url):
            click_friend_summon()
            click_party_ok()
        if is_battle_page():
            click_full()
        #这里战斗时间很短暂，没有写自动刷新
        is_goal_page(waittime = 60)
        #等待判断结算页面出现，最多等待六十秒



def play_halloween_exclusive_quest(times = 10):
    url = "https://game.granbluefantasy.jp/#quest/supporter/800031/22"
    battle_limit_time = 60
    #单次战斗最多持续60s
    connect_chrome()
    while times > 0 :
        times = times - 1 
        print("left times :",  times)
        #打开网页
        if event_paly_page(url):
            click_friend_summon()
            click_party_ok()
        if is_battle_page():
            click_full()
        #这里战斗时间很短暂，没有写自动刷新
        is_goal_page(waittime = 60)
        #等待判断结算页面出现，最多等待六十秒

def click_refresh():
    if is_element_exist(By.CLASS_NAME, "btn-treasure-footer-reload"):
        bt = chm.find_element_by_class_name("btn-treasure-footer-reload")
        if bt.is_enabled():
            bt.click()
        else:
            print("can not click reload bt")
    else:
        print("can not find reload bt")


def tiguan():
#踢馆
    url = "https://game.granbluefantasy.jp/#quest/supporter/400151/4"
    connect_chrome()
    repeat_times = int(input("pls input repeat times :"))
    while repeat_times > 0:
        print("while loop start")
        repeat_times = repeat_times - 1
        print("left times : ", repeat_times)
        if event_paly_page(url):
            click_friend_summon()
            click_party_ok()
        if is_battle_page():
            click_full()
            #  time.sleep(0.5)
            #  event_paly_page(url)
            #  click_full()
            #  time.sleep(0.5)
            #  event_paly_page(url)
        is_goal_page(60)

def sound():
    print("\a")
#发出提示声

def end_msgbox(msg="打完了", title="gbf script", bt="ok"):
    pyautogui.alert(msg, title, bt)
    sound()


def play_event_reflections_for_a_white_clover(times = 10):
#完美运行
    battle_limit_time = 60
    #单次战斗最多持续60s
    url = "https://game.granbluefantasy.jp/#quest/supporter/909621/5"
    connect_chrome()
    while times > 0 :
        times = times - 1 
        print("left times :",  times)
        #打开网页
        if event_paly_page(url):
            click_friend_summon()
            click_party_ok()
        if is_battle_page():
            click_full()
        #这里战斗时间很短暂，没有写自动刷新
        is_goal_page(waittime = 60)
        #等待判断结算页面出现，最多等待六十秒

def play_arcum_zoone_faym_madshearwielder():
    url = "https://game.granbluefantasy.jp/#replicard/supporter/3/3/16/812091/25"
    play_common_arcum(url, 6)
    end_msgbox()


def play_event_hope_from_a_snow_drop():
    url = "https://game.granbluefantasy.jp/#quest/supporter/912341/1/0/10504"
#完美运行
    battle_limit_time = 300
    #单次战斗最多持续300s
    connect_chrome()
    times = int(input ("pls input times to repeat :"))
    while times > 0 :
        times = times - 1 
        print("left times :",  times)
        #打开网页
        if event_paly_page(url):
            click_friend_summon()
            click_party_ok()
        if is_battle_page():
            click_full()
            auto_refresh(battle_limit_time)


def play_arcum_vestige_of_truth():
    url = "https://game.granbluefantasy.jp/#replicard/supporter/4/4/3/813011/25"
    time_limt = 3
    gauge_url = "https://game.granbluefantasy.jp/#replicard/stage/4"
    play_common_arcum(url, time_limt,gauge_url)
    end_msgbox()

def check_and_play_arcum_gague(url):
    # find label txt-chest-name
    chm.get(url) 
    flag = is_element_exist(By.CLASS_NAME, "txt-chest-name", 3)
    if flag:
        a = chm.find_element_by_class_name("txt-chest-name")
        a.click()
        if is_element_exist(By.CLASS_NAME, "btn-usual-ok", 5):
            a = chm.find_element_by_class_name("btn-usual-ok")
            time.sleep(2)
            a.click()
            if is_element_exist(By.CLASS_NAME, "btn-usual-ok", 5):
                a = chm.find_element_by_class_name("btn-usual-ok")
                time.sleep(2)
                try:
                    a.click()
                except StaleElementReferenceException:
                        print("exceptions.StaleElementReferenceException")
                        pass
                        
            else:
                if is_element_exist(By.CLASS_NAME, "txt-quest-name", 5):
                    a = chm.find_element_by_class_name("txt-quest-name")
                    if a.text == "Mimic":
                        time.sleep(2)
                        a.click()
                        click_arcum_part_ok()
                        click_full()
                        is_goal_page(60)
    else:
        if is_element_exist(By.CLASS_NAME, "txt-quest-name", 5):
            a = chm.find_element_by_class_name("txt-quest-name")
            if a.text == "Mimic":
                time.sleep(2)
                a.click()
                click_arcum_part_ok()
                click_full()
                is_goal_page(60)

def is_dead():
    #  Use Auto Select
    #  txt-title
    flag = False
    if is_element_exist(By.CLASS_NAME, "txt-title", 1):
        if chm.find_element_by_class_name("txt-title").text == "Use Auto Select":
            flag = True
    
    return flag

#  def is_cannot_play():
    #  prt-popup-header
    #  エラー
    # after select summon if appear this element , this battle won't be permitted
    #  flag = False
    #  if is_element_exist(By.CLASS_NAME, "prt-popup-header", 1):
        #  if chm.find_element_by_class_name('prt-popup-header').text == "エラー"
            #  flag = True
#
    #  return flag


play_arcum_vestige_of_truth()


#  play_event_hope_from_a_snow_drop()

#  connect_chrome()
#  auto_refresh(10)
#  play_arcum_zoone_faym_madshearwielder()
#  tiguan()
#  play_event_reflections_for_a_white_clover(30)
#  play_halloween_exclusive_quest(20)
#  play_halloween_rapid()
#  play_arcum_icebergchampion()
#  play_finder_filter1_1()
#  auto_reverse()

class six_dragon:

    url_fire = "https://game.granbluefantasy.jp/#quest/supporter/305191/1/0/41"
    url_water = ""
    url_earth = ""
    url_wind = ""
    url_light = ""
    url_dark = ""


    def __init__(self):
        pass

    def play_fire(self):
        self.play(self,self.url_fire)

    def play(self,url):
        # open url
        #  click summon
        #  click party ok
        #  click full
        #  auto refresh
        pass
