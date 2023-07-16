# Copyright Reid Powell and Mikael Varashovsky


#imports
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
import time
import datetime
from datetime import date
import pytz
import random
import socket
import urllib3
import urllib3.exceptions
import threading
import deepl
#from newsapi import NewsApiClient
import re
import requests
import smtplib
import json
#from win32gui import GetWindowText, GetForegroundWindow








#get username and shit from the json file

settingsfile = open("settings.json", "r")
settingsdata = json.load(settingsfile)

username = settingsdata['login']['username']
password = settingsdata['login']['password']

entrances = settingsdata['entrances']['entrances']


def get_version():
    settingsfile = open("settings.json", "r")
    settingsdata = json.load(settingsfile)
    version = settingsdata['systemsettings']['version']
    settingsfile.close()
    return version

def whatsnew():
    settingsfile = open("settings.json", "r")
    settingsdata = json.load(settingsfile)
    whatsnew = settingsdata['systemsettings']['whatsnew']
    settingsfile.close()
    return whatsnew

def get_radio():
    settingsfile = open("settings.json", "r")
    settingsdata = json.load(settingsfile)
    radiolink = settingsdata['radioShit']['radioURL']
    settingsfile.close()
    return radiolink
def get_broadcastlink():
    settingsfile = open("settings.json", "r")
    settingsdata = json.load(settingsfile)
    broadcastlink = settingsdata['radioShit']['broadcastURL']
    settingsfile.close()
    return broadcastlink

#random stuff

def get_jokes():
    file = open("random.json", "r")
    data = json.load(file)
    jokes = data['jokes']
    joke = random.choice(jokes)
    return joke
def get_drink():
    file = open("random.json", "r")
    data = json.load(file)
    drinks = data['drinks']
    drink = random.choice(drinks)
    return drink
def get_cuss_word():
    file = open("random.json", "r")
    data = json.load(file)
    words = data['cuss_words']
    word = random.choice(words)
    return word
def get_insults():
    file = open("random.json", "r")
    data = json.load(file)
    insults = data['insults']
    insult = random.choice(insults)
    return insult




#selinum shit
opts = Options()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)
browser.get("https://y99.in/web/login/")
a = ActionChains(browser)

##get into y99
time.sleep(5)
#access y99
browser.find_element(By.CLASS_NAME, 'blue--text.login-instead').click()
#user and password
browser.find_element(By.CLASS_NAME, 'input-username').send_keys(username)
browser.find_element(By.CLASS_NAME, 'input-username.mt-1').send_keys(password)
browser.find_element(By.CLASS_NAME, 'mx-0.btn.btn--large.btn--depressed.e4jtrd').click()
print("Logged in")
#get past staging page
time.sleep(5)
browser.find_element(By.XPATH, '//*[@id="welcome-page"]/div/div[3]/button').click()
print("past the staging page")
#get rid of popup
time.sleep(3)
browser.find_element(By.XPATH, '//*[@id="app"]/div[8]/div/div/div[3]/button[1]').click()
print("got rid of popup")
time.sleep(3)
#hop into deep's chat
print("entering the chat")
time.sleep(5)
browser.find_element(By.XPATH, '//*[@id="app"]/div[22]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]').click()
print("entered the chat")




#reading and stripping down the messages so that they can be proccesses by the bot
def read_messages():
    raw_text = str(browser.find_elements(By.XPATH, '//*[@class="log-container may-transform"]')[-1].text)
    return raw_text
#timer
def timer(h, m, s, user):
    finished = False
    total_seconds = h * 3600 + m * 60 + s
    while total_seconds > 0:
        timer = datetime.timedelta(seconds=total_seconds)
        time.sleep(1)
        total_seconds -= 1
    send_message("/runban " + user)
#sending messages
def send_message(message):
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="app"]/div[22]/div[1]/div[2]/div[8]/div[3]/div[1]/div[5]/div[2]/div/div/textarea').send_keys(message)
    browser.find_element(By.XPATH, '//*[@id="app"]/div[22]/div[1]/div[2]/div[8]/div[3]/div[1]/div[5]/div[2]/div/div/div[4]/i').click()
def err(errcode):
    writeToLogs("ERROR - " + users + " " + errcode)
    send_message(errcode)







send_message(random.choice(entrances))



#time
def read_time():
    now = datetime.datetime.now()
    now = now.strftime("%H:%M:%S")
    proper_time = str("The time in UTC 6 is " + str(now))
    send_message(str(proper_time))
#date
def read_date():
        print("date command recognized")
        send_message(str(date.today()))
#vaduz
def get_vaduz_time():
    print("vaduz command recogized")
    utc_utc_vaduz = datetime.datetime.now(pytz.timezone('Europe/Vaduz'))
    vaduzTime = utc_utc_vaduz.strftime('%d/%m/%Y %H:%M:%S %Z %z')
    send_message(str(vaduzTime))
#timezones
def timez():
    writeToLogs("INFO - [" + users + " used the timez command]")
    goodies = str3.split(" ")
    try:
        timezone = goodies[1]
        timezones = datetime.datetime.now(pytz.timezone(timezone))
        timezonetime = timezones.strftime('%d/%m/%Y %H:%M:%S %Z %z')
        send_message(str(timezonetime))
    except Exception as e:
        writeToLogs("ERROR - [" + users + " caused an error")
        send_message(users + " you caused this error " + str(e))


#station
def get_station():
    print("station command recognized")
    http = urllib3.PoolManager()
    try:
        resp = http.request("GET", get_broadcastlink())
        send_message("The station is broadcasting")
    except:
        send_message("the station is not broadcasting")
#like
def get_like():
    goodies = str3.split(" ")
    try:
        if goodies[1] != "read":
                send_message("It's offical " + goodies[1] + " Likes me")
                with open("./syscrit/people/like.txt", "a") as f:
                    f.write(f'{goodies[1]}\n')
        elif goodies[1] == "phoibe":
            send_message("this is a buffer to prevent the generation of a new loop")
    except IndexError:
        err("Unexpected IndexError, please see above command")
        send_message("please read usage")
#backlog
def assign_backlog():
    goodies = str3.split(".")
    goodies = goodies[1].split(" ")
    try:
        if goodies[1] != "read":
            send_message("ok " + goodies[1] + " has been reported to the mods")
            with open("./syscrit/people/backlog.txt", "a") as f:
                f.write(f'{goodies[1]}\n')
    except IndexError:
        err("Unexpected IndexError, please see above command")
        send_message("please read usage")
#read the backlog
def read_backlog():
    usernames = open("./syscrit/people/backlog.txt", "r")
    usernames = str(usernames.read())
    usernames = usernames.replace("\n", " ")
    send_message(usernames)
#read likes
def read_likes():
    usernames = open("./syscrit/people/like.txt", "r")
    usernames = str(usernames.read())
    usernames = usernames.replace("\n", " ")
    send_message(usernames)
#translate
def get_transtlation():
    goodies = str3.split("/")
    auth_key = "d3fa9b35-f33c-14e8-075b-54b3705f5ee4:fx"
    translator = deepl.Translator(auth_key)
    try:
        send_message(str(translator.translate_text(text=goodies[1], target_lang=goodies[2]).text))
    except:
        err("Unexpected translation error has occured")
        send_message("please see the usages for proper language formatting")
#auto backlog
def auto_backlog():
    for i in backlog_keywords:
        if i in str3:
            send_message("you have said a word or phrase that has triggered my auto backlog, please see the rules")
            with open("./syscrit/backlog.txt", "a") as f:
                f.write(users + "\n")
                f.close()
            send_message("okay " + users + " added to the backlog, if you think this is an error, please tell R_Powell")
#news
#def get_news():
    #title = []
    #api_key = "a0606776aad44222b891df427a5e96a5"
    #newsapi = NewsApiClient(api_key)
    #goodies = str3.split(" ")
    #top_headlines = newsapi.get_top_headlines(sources='reuters', language='en', page_size=1)
    #for i in top_headlines['articles']:
        #headline = i['title']
        #url = i['url']
        #break
    #send_message("Reuters: " +  headline + " | url: " + url)
#soft blacklist
def check_blacklist():
    blacklists = open("./syscrit/people/blacklist.txt", "r")
    blacklists = str(blacklists.read())
    true_blacklist = blacklists.split("\n")
    return true_blacklist
#urban dictionary
def get_urban_dictionary_definition(term):
    url = f"https://api.urbandictionary.com/v0/define?term={term}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if "list" in data and len(data["list"]) > 0:
            first_definition = data["list"][0]["definition"]
            return first_definition
        else:
            return "No definition found."
    
    except:
        err("Unknown error has occured")
def ud():
    goodies = str3.split("/")
    try:
        definition = get_urban_dictionary_definition(goodies[1])
        send_message(str(definition))
    except:
        writeToLogs("ERROR - [" + users + " caused an IndexError]")
        send_message(users + " you have caused an IndexError, please read the usage and try again")
#voting
def vote():
    goodies = str3.split(" ")
    try:
        if goodies[1] == "yay":
            with open("./syscrit/voting/yay.txt", "a") as f:
                f.write(users + "\n")
                send_message(users + " voted for")
        if goodies[1] == "nay":
            with open("./syscrit/voting/nay.txt", "a") as f:
                f.write(users + "\n")
                send_message(users + " voted against")
    except:
        err("Voting error, this user is either not allowed to vote or something else has happened")
#counting votes
def count_votes():
    yay = []
    nay = []
    with open("./syscrit/voting/yay.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            yay.append(line)
    fixedyay = [*set(yay)]
    with open("./syscrit/voting/nay.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            nay.append(line)
    fixednay = [*set(nay)]
    send_message("yay: " + str(len(fixedyay)) + " nay: " + str(len(fixednay)))
#writing to logs
def writeToLogs(message):
            now1 = datetime.datetime.now()
            now = now1.strftime('%Y-%m-%d %H:%M:%S')
            now2 = now1.strftime('%Y-%m-%d')
            with open("./logs/" + now2 + ".log", "a+")  as f:
                f.write(str(now) + " - " + message +"\n")
#What Is Reid Doing
# gets the active window
def getWin():
    activeWin = GetWindowText(GetForegroundWindow())
    return activeWin
#the rules
def switch(lang):
    if "VSCodium" in lang:
        goodies = lang.split("-") # The format will be: folder - file - app
        activity =  goodies[1] + "/" + goodies[0]
        activity = activity.replace(" ", "")
        return "Coding in " + activity
    else:
        return lang
#checking the issues
def check_issue():
    with open("./syscrit/voting/issue.txt", "r") as f:
        line = f.readline()
        send_message(line)
#hard blacklist
def check_Hblacklist():
    blacklists = open("./syscrit/people/hard_blacklist.txt", "r")
    blacklists = str(blacklists.read())
    true_Hblacklist = blacklists.split("\n")
    return true_Hblacklist        
#read the rules
def read_rules():
    f = open("rules.txt", "r") 
    rules = str(f.read())
    rules = rules.split('\n')
    for rule in rules:
        send_message(rule)
def srule():
    goodies = str3.split(" ")
    f = open("rules.txt", "r")
    gint = 0
    try:
        gint = int(goodies[1])
        line = f.readlines()
        send_message(str(line[gint - 1]))
    except IndexError:
        writeToLogs("ERROR - something went wrong with reading a specific line from a file")
        send_message("are you possibly using the wrong command? This one is for reading a specific rule, not all of them")
#read the mini mods
def read_mMods():
    f = open("./syscrit/people/minimods.txt", "r")
    lin = f.read()
    lines = lin.split('\n')
    return lines
#mini mod test
def mmtest():
    successful = False
    if users in mini_mod:
        send_message("test is successful")
        successful = True
    else:
        send_message("you are not permitted to use this command")
    return successful
#read the registered users
def read_reg_users():
    f = open("./syscrit/people/regusers.txt", "r")
    lin = str(f.read())
    lines = lin.split('\n')
    return lines
#mini mod echo
def echo():
    goodies = str3.split("/")
    try:
        send_message(goodies[1])
    except:
        writeToLogs("ERROR - [" + users + " has caused an IndexError]")
        send_message(users + " you have cause and IndexError, please read usage and try again")
#mods
def get_mods():
    f = open("./syscrit/people/mods.txt")
    lin = f.read()
    send_message(lin)
# casting electoral votes
def cast_vote():
    goodies = str3.split(" ")
    try:
        canidate = goodies[1]
    except IndexError:
        writeToLogs("ERROR - Unexpected IndexError")
        send_message("Unexpected IndexError, please try again")
    file = open("elect.json", "r")
    file2 = open("./syscrit/voting/haselected.txt", "r")
    file2 = file2.read()
    file2 = file2.split('\n')
    data = json.load(file)
    try:
        if users not in file2:
            data['canidates'][canidate] = data['canidates'][canidate] + 1
            with open("elect.json", "w") as f:
                json.dump(data, f, indent=4)
            with open("./syscrit/voting/haselected.txt", "a") as f:
                f.write(users + "\n")
        else:
            send_message("you have already voted " + users)
        send_message(users + " has voted")
    except Exception as e:
        writeToLogs("ERROR - [" + users + "caused an error]")
        send_message(users + " you have caused this error: " + str(e))

# sort and then send out the values
def sort_results():
    file = open("elect.json", "r")
    data = json.load(file)
    data = data['canidates']
    sorted_data = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
    writeToLogs("INFO - the results have been sorted")
    send_message(str(sorted_data))
#ballot
def get_ballot():
    writeToLogs("INFO - [" + users + " requested the ballot]")
    send_message("please vote for these people with canidate instead of their name")
    f = open("./syscrit/voting/ballot.txt")
    f = f.read()
    f = f.split("\n")
    for canidate in f:
        time.sleep(2)
        send_message(canidate)
def wheelie():
    goodies = str3.split(" ")
    manfile = open("manual.json", "r")
    man = json.load(manfile)

    try:
        command = goodies[1]
    except:
        writeToLogs("ERROR = [" + users + " caused an IndexError]")
        send_message(users + " you have cause and IndexError, please read the usage of this command by doing (.)wheelie wheelie")
    try:    
        send_message("Name: " + man[command]['name'])
        time.sleep(2)
        send_message("Description: " + man[command]['description'])
        time.sleep(2)
        send_message("Usage: " + man[command]['usage'])
    except:
        writeToLogs("ERROR - [" + users + " caused an error with the wheelie command")
        send_message("you have caused an error, please try again")
#fight
def fight():
    basescore1 = 500
    basescore2 = 500

    goodies = str3.split(" ")

    try:
        un1 = goodies[1].lower()
        un2 = goodies[2].lower()
    except:
        writeToLogs("ERROR - [" + users + " caused an IndexError]")

    file = open("values.json", "r")
    data = json.load(file)
    for letter in un1:
        for shit in data['values']:
            if letter == shit:
                basescore1 = basescore1 + data['values'][shit]
    basescore1 = basescore1 * 100
    for letter in un2:
        for shit in data['values']:
            if letter == shit:
                basescore2 = basescore2 + data['values'][shit]
    basescore2 = basescore2 * 100
    if basescore1 > basescore2:
        send_message(un1 + " won this fight")
    if basescore1 < basescore2:
        send_message(un2 + " won this fight")
    if basescore1 == basescore2:
        send_message("It's a tie")
#muting people
def mute():
    messages = []
    file = open("mute.txt", "r")
    lin = file.readline()
    lines = lin.split("\n")
    for linesx in lines:
        if users in lines:
            messages = browser.find_elements(By.XPATH, '//*[@class="message-tooltip show-on-hover"]')
            e = browser.find_elements(By.XPATH, '//*[@class="text_wrapper"]')
            e = e[-1]
            a.move_to_element(e).perform()
            f = browser.find_elements(By.XPATH, '//*[@class="btn btn--flat btn--icon"]')[-1]
            a.move_to_element(f)
            a.click()
            fuckingwork()
def fuckingwork():
    element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='list__tile__title' and text()='Delete Message']")))
# Click on the element
    a.click(element)




#custom messages
def custom_messages():
    is_there = False
    f = open("cMessages.json", "r")
    data = json.load(f)
    if users in data['custom_messages']:
        send_message(data['custom_messages'][users])
    else:
        send_message(users + " what?")


#important bits for later
skip = False
lastmsg = ""
lastusr = ""



while True:
    regged_users = read_reg_users()
    mini_mod = read_mMods()
    shit = read_messages() #this is the raw text that needs to be refined
    shittles = shit.split("\n") # this is splitting it into strings
    if len(shittles) == 3: #check to see if user has no pfp
        shittles.remove(shittles[1])
        
    try:
        users = shittles[0] # usernames will always be first
        str3 = shittles[1] # message
        if len(users) == 3:
            users = lastusr
        lastusr = users  
    except:
        str3 = read_messages()
        users = lastusr
        pass
    try:
        if lastmsg != str3:
            writeToLogs(users + " - " + str3)
            print("[" + users + "]")
            print(str3)
            lastmsg = str3
    except:
        pass
    lastmsg = str3


    try:
        true_blacklist = check_blacklist()
        hard_blacklist = check_Hblacklist()
#check if user is in the blacklist
        if users in true_blacklist and "." in str3:
            send_message("this user is not allowed to use commands | if you feel this is a mistake, contact one of the devs")
            writeToLogs( "WARN - " + users + " Tried to use a command")
            str3 = " "
            true_blacklist.clear()
#check if user is in the hard blacklist
        if users in hard_blacklist:
            writeToLogs("WARN - " + users + " tried to use a command")
            str3 = " "
            users = "blacklisted"
            hard_blacklist.clear()
#time
        if ".time" in str3:
            writeToLogs("INFO - [" + users + " checked the time]")
            read_time()
#breakout
        if ".breakout" in str3:
            send_message("User1894284908")
#date
        if ".date" in str3:
            writeToLogs("INFO - [" + users + "checked the date]")
            read_date()
#version
        if ".ver" in str3:
            writeToLogs("INFO - [" + users + " checked the version]")
            send_message(get_version())
#radio
        if ".radiostation" in  str3:
            print("radio command recognized")
            writeToLogs("INFO - [" + users + " checked out the radio]")
            send_message(get_radio())
#vaduz
        if ".vaduz" in str3:
            writeToLogs("INFO - [" + users + " checked the time in vaduz]")
            get_vaduz_time()
#insult
        if ".insult" in str3:
            print("insult command recognized")
            writeToLogs("INFO - [" + users + " wanted an insult]")
            send_message(get_insults())
#dj
        if ".dj" in str3:
            print("DJ command recognized")
            writeToLogs("INFO - [" + users + " checked the DJs]")
            send_message("R_Powell, unless you're bitching")
# good night
        if ".gn" in str3:
            print("good night command recognized")
            writeToLogs("INFO - [" + users + " went to bed]")
            send_message("good night my little pumpkin boo")
#drinks
        if ".drink" in str3:
            writeToLogs("INFO - [" + users + " wanted a drink]")
            goodies = str3.split(" ")
            try:
                send_message("pheebs sends " + goodies[1] + " " + get_drink())
            except:
                send_message("pheebs sends " + users + " " + get_drink())
#station
        if ".station" in str3:
            writeToLogs("INFO - [" + users + " wanted the station]")
            get_station()
#ping pong
        if ".ping" in str3:
            writeToLogs("INFO - [" + users + " pinged the bot]")
            send_message("poooooong")
#ping deep
        if ".deep" in str3:
            send_message("Deepestdeep")
#dev Help
        if ".devhelp" in str3:
            send_message("ping - ping pong command | deep - pings deep")
#cuss command for version 1.0
        if ".cuss" in str3:
            print("cuss command recognized")
            writeToLogs("INFO - [" + users + " cussed]")
            send_message(get_cuss_word())
#sex
        if ".sex" in str3:
            print("sex command recognized")
            writeToLogs("INFO - [" + users + " used the sex command]")
            send_message("congrats " + users + " is kind of a weirdo")
#docs
        if ".docs" in str3:
            writeToLogs("INFO - [" + users + " wanted to check out the source]")
            send_message("https://github.com/RPowell-C/BotDocs/")
#dev
        if ".dev" in str3:
            writeToLogs("INFO - [" + users + " wanted to know who the devs were]")
            send_message("Reid Powell - Lead Developer - R_Powell")
            time.sleep(3)
            send_message("https://github.com/RPowell-C")
            time.sleep(3)
            send_message("Mikael Varashovsky - Developer - Mikaelvussy")
            time.sleep(3)
            send_message("michaelangelo - Developer")
#credits
        if ".creds" in str3:
            send_message("Developers - See dev command")
            time.sleep(3)
            #send_message("PFP - KatB")
#Like
        if ".ilike" in str3:
            writeToLogs("INFO - [" + users + " liked the bot]")
            get_like()
#backlog
        if ".mmreport" in str3:
            if users in mini_mod:
                writeToLogs("INFO - [" + users + " used a mini mod command]")
                assign_backlog()
            else:
                writeToLogs("WARN - [" + users + " tried to use a mini mod command]")
                send_message("You do not have permission to use this command")
#bl
        if ".bl" in str3:
            read_backlog()
#Likes (just reads the file)
        if ".wholikes" in str3:
            writeToLogs("INFO - [" + users + " checked who likes the bot]")
            read_likes()
#love
        #if ".love" in str3:
            #send_message("woah, I'm just a bot")
#alert 
        if ".alert" in str3:
            try:

                writeToLogs("INFO - [" + users + " pulled up the alert board]")
                ausers = open("./syscrit/people/alert.txt", "r") 
                send_message(str(ausers.read()))
            except:
                writeToLogs("UnicodeEncodeError")
#whatsnew
        if ".whatsnew" in str3:
            writeToLogs("INFO - [" + users + " wanted to know whats new]")
            print("someone wants to know whats new")
            send_message(whatsnew())
#jokes 
        if ".joke" in str3:
            writeToLogs("INFO - [" + users + " wanted a joke]")
            print("someone wants a joke")
            send_message(get_jokes())
#I wanna DJ
        if ".iwannadj" in str3:
            writeToLogs("INFO - [" + users + " wants to DJ]")
            send_message("If you would like to DJ please fill out this form:")
            time.sleep(3)
            send_message("https://docs.google.com/forms/d/e/1FAIpQLSdfIL1c51YLc32DWwyeiZpRVGbZL6C4h4nHYK8NP9t8L-b21Q/viewform?usp=sf_link")
#I wanna be a dev
        if ".iwannadev" in str3:
            writeToLogs("INFO - [" + users + " wanted to dev]")
            send_message("Talk to R_Powell")
#fuck you shoresy
        if ".lkenny" in str3:
            writeToLogs("INFO - [" + users + " wanted a random letterkenny quote]")
            print("someone said fuck you")
            send_message(random.choice(fuckyouShorsey))
#translate
        if ".translate" in str3:
            writeToLogs("INFO - [" + users + " translated some text]")
            get_transtlation()
#langhelp
        if ".langhelp" in str3:
            writeToLogs("INFO - [" + users + " needed some langhelp]")
            auth_key = "d3fa9b35-f33c-14e8-075b-54b3705f5ee4:fx"
            translator = deepl.Translator(auth_key)
            for language in translator.get_target_languages():
                send_message(str(f"{language.name} ({language.code})"))
                time.sleep(2)
#you're welcome
        if "Thank you" in str3:
            print("someone said thank you")
            send_message("you're very much welcome")
#someone mentions her
        if "phoibe" in str3:
            if "." in str3:
                err("ME01")
                writeToLogs("WARN - " + users + " tried to command and tag")
            else:
                writeToLogs("INFO - [" + users + " tagged the bot]")
                custom_messages()
#auto backlog
        #auto_backlog()
#news
        #if ".news" in str3:
            #writeToLogs("INFO - [" + users + " wanted the news]")
            #get_news()
#urban dictionary
        if ".urbandict" in str3:
            writeToLogs("INFO - [" + users + " used urban dict]")
            ud()
#voting system
        if ".issue" in str3:
            writeToLogs("INFO - [" + users + " checked the issue]")
            check_issue()
        if ".vote" in str3:
            if users in regged_users:
                writeToLogs("INFO - [" + users + " voted]")
                vote()
            else:
                writeToLogs("WARN - [" + users + " tried to vote without permission]")
                send_message("this user is not allowed to vote")
        if ".countvotes" in str3:
            writeToLogs("INFO - [" + users + " counted the votes]")
            count_votes()
#disclosure
        if ".disclosure" in str3:
            writeToLogs("INFO - [" + users + " requested the disclosure]")
            with open("disclosure.txt", "r") as f:
                line = f.readline()
                send_message(line)
#birthday
        if ".bday" in str3:
            writeToLogs("INFO - [" + users + " wanted to know the bot's birthday]")
            send_message("May 3, 2023")
#good morning
        if ".gm" in str3:
            writeToLogs("INFO - [" + users + " said good morning]")
            send_message("good morning, sleepy head")
#rules
        if ".allrules" in str3:
            writeToLogs("INFO - [" + users + " read the rules]") 
            read_rules()
#mini mods test
        if ".mmtest" in str3:
            result = mmtest()
            writeToLogs("INFO - [" + users + " tried to use a mini mod command, it was " + str(result) + "]")
#specific rules
        if ".srule" in str3:
            writeToLogs("INFO - [" + users + " read a specific file]")
            srule()
#mini mod echo
        if ".mmecho" in str3:
            if users in mini_mod:
                writeToLogs("INFO - [" + users + " Echoed]")
                echo()
            else:
                writeToLogs("WARN - [" + users + "tried to use a mini mod command]")
                send_message("you are not allowed to use this command")
#mini mod get mods
        if ".mmgetmod" in str3:
            if users in mini_mod:
                writeToLogs("INFO - [" + users + " requested a mod]")
                get_mods()
            else:
                writeToLogs("WARN - [" + users + " tried to use a mini mod command]")
#logs
        if ".logs" in str3:
            send_message("due to a vote taken, the logs are here: https://github.com/RPowell-C/BotLogs/blob/main/chatlog.txt")
#get results
        if ".results" in str3:
            if users == "R_Powell" or "Deepestdeep":
                sort_results()
            else:
                writeToLogs("ERROR - [" + users + "tried to access election results]")
#cast vote
        if ".castfor" in str3:
            f = open("./syscrit/people/regusers.txt")
            f = f.read()
            if users in f:
               cast_vote()
            else:
                writeToLogs("WARNING - [" + users + " tried to write to logs]")
                send_message("you are not authorized to do that")
#ballot
        if ".ballot" in str3:
            get_ballot()
#WIRD (What Is Reid Doing)
        if ".wird" in str3:
            #lang = getWin()
            #send_message(switch(lang))
            send_message("Reid is currently on a business trip to Athens, Mishka has control over the bot now")
#wheelie
        if ".wheelie" in str3:
            writeToLogs("INFO - [" + users + " used the wheelie command")
            wheelie()
#wew
        if "wew" in str3:
            send_message("what is that?")
#fight
        if ".fight" in str3:
            try:
                writeToLogs("INFO - [" + users + " used the fight command]")
                fight()
            except Exception as e:
                writeToLogs("ERROR - [" + users + "caused " + str(e)+ "]")
                send_message(str(e))
#zime
        if ".zime" in str3:
            timez()
            



#help
        if ".help" in str3:
            writeToLogs("INFO - [" + users + " needed help]")
            print("someone asked for help")
            send_message("use the period (.) before every command listed | dj - the djs | randq - picks a random quote | time - shows the time in US/Central | date - Shows the date from US/Central | ver - shows the bot's version | radiostation - shows the link to the radio statio | Continued >")
            time.sleep(3)
            send_message("vaduz - Shows the time in Europe/Vaduz | gn - goodnight | drinks - give everyone in the chat drinks |  insult - the fuck you think it does bro? | cuss - tf you think it does bro? | station - Shows whether or not the radio station is broadcasting | Coninued >")
            time.sleep(3)
            send_message("docs - displays the docs | dev - show the information about the dev(s) | whatsnew - shows whats new or changed | jokes - jokes | iwannadj - gives you the form to fill out to dj | alert - Sends the entire chat a list of suspected pedophiles and creeps | credits - view the credits | iwannadev - learn about how you could possibly dev | Continued >")
            time.sleep(3)
            send_message("ilike - tell the bot you like it - Usage: ilike username | wholikes - displays who likes the bot | translate - translates any text into a language - Usage: (.)translate/bonjour/EN-GB - availabe languages please use (.)langhelp | backlog - DEPRECEATED - store the usernames of solicitors and whatnot - Usage: same as the likes command")
            time.sleep(3)
            send_message("news - give the latest news | urbandict - look up a phrase in the urban dictionary - Usage: (.)urbandict/phrase | (.)disclosure - print a disclosure | (.)bday - print the bot's birthday | (.)gm - wake up | (.)allrules - dislpays all of the rules | (.)srule - displays a specific rule - Usage: (.)srule 1 | (.)wird - What Is Reid Doing?")
        true_blacklist = []
    except KeyboardInterrupt():
        send_message("The bot is out")
        quit()
