import discord
client = discord.Client()
import requests
import urllib.request
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import os
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--window-size=1024,768')
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(executable_path='/app/.chromedriver/bin/chromedriver', options=options)
driver.get("http://om.skhidc.kr/index.php")
    
@client.event
async def on_message(message):
    if message.author.bot:
        return None
    
    if message.content.startswith('!일월 괴영'):

        season1 = message.content[7:8]

        try:
            season = int(season1)

        except ValueError:
            await message.channel.send('!일월 괴영 <시즌> <직업>')

        else:
            pass

        finally:
            pass
                
        job1 = message.content[9:len(message.content)]

        if job1 == "검객":
            job = "swordman"

        elif job1 == "자객":
            job = "assassin"

        elif job1 == "궁사":
            job = "archer"

        elif job1 == "진사":
            job = "archer"

        elif job1 == "닌자":
            job = "archer"

        elif job1 == "월사":
            job = "archer"

        elif job1 == "법사":
            job = "archer"

        elif job1 == "창술사":
            job = "archer"

        else:
            job = "swordman"
            job1 = "검객"

        if season == 7:
            season = str(season1)
            req = requests.get('http://om.skhidc.kr/carnivaltop.php?job='+job)  
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
            info = message.content[4:7]+' '+job1

        elif season >= 8:
            season = str(season1)
            req = requests.get('http://om.skhidc.kr/carnival_season.php?job='+job,'&season=1')  
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
            info = message.content[4:7] + "1 " + job1
                
        else:
            season = str(season1)
            req = requests.get('http://om.skhidc.kr/carnival_season.php?job='+job+'&season='+season)  
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
            info = message.content[4:7]+season1+' '+job1

        embed=discord.Embed(title=info, color=0x00ff56)

        table = soup.find('table', {'class': 'table table-bordered'})
        trs = table.find_all('tr')
        for idx, tr in enumerate(trs):
            if idx > 0:
                tds = tr.find_all('td')
                ranking = tds[0].text.strip()
                nickname = tds[1].text.strip()
                score = tds[3].text.strip()
                embed.add_field(name=ranking, value='닉네임: ' + nickname + ' | 점수: ' + score, inline=False)

        await message.channel.send(embed=embed)

    if message.content.startswith('!일월 검색'):

        Name = message.content[7:len(message.content)]

    try:
        chrome = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul/li[1]/a')
        if len(chrome.text) >= 1:
            
            search_box = driver.find_element_by_class_name('form-control')
            search_box.send_keys(Name)
            search_box.send_keys(Keys.RETURN)
            
        else:
            driver.get(url='http://om.skhidc.kr/')
            search_box = driver.find_element_by_class_name('form-control')
            search_box.send_keys(Name)
            search_box.send_keys(Keys.RETURN)
            
    except NoSuchElementException:
        driver.get(url='http://om.skhidc.kr/')
        search_box = driver.find_element_by_class_name('form-control')
        search_box.send_keys(Name)
        search_box.send_keys(Keys.RETURN)
    embed=discord.Embed(title=Name, color=0x00ff56)
    try:
        elem = driver.find_element_by_xpath('/html/body/table/tbody/tr/th[1]/div')
        if len(elem.text) >= 1:
            
            card1 = driver.find_element_by_xpath('/html/body/table/tbody/tr/th[1]/div')
            card1_data = card1.text
            embed.add_field(name="캐릭터1", value=card1_data, inline=True)
            
        else:
            embed.add_field(name="캐릭터1", value="없음", inline=True)
    except NoSuchElementException:
        embed.add_field(name="캐릭터1", value="없음", inline=True)
    try:
        elem = driver.find_element_by_xpath('/html/body/table/tbody/tr/th[2]/div')
        if len(elem.text) >= 1:
            
            card2 = driver.find_element_by_xpath('/html/body/table/tbody/tr/th[2]/div')
            card2_data = card2.text
            embed.add_field(name="캐릭터2", value=card2_data, inline=True)
            
        else:
            embed.add_field(name="캐릭터2", value="없음", inline=True)
    except NoSuchElementException:
        embed.add_field(name="캐릭터2", value="없음", inline=True)
    try:
        elem = driver.find_element_by_xpath('/html/body/table/tbody/tr/th[3]/div')
        if len(elem.text) >= 1:
            
            card3 = driver.find_element_by_xpath('/html/body/table/tbody/tr/th[3]/div')
            card3_data = card3.text
            embed.add_field(name="캐릭터3", value=card3_data, inline=False)
            
        else:
            embed.add_field(name="캐릭터3", value="없음", inline=False)
    except NoSuchElementException:
        embed.add_field(name="캐릭터3", value="없음", inline=False)
    try:
        elem = driver.find_element_by_xpath('/html/body/table/tbody/tr/th[4]/div')
        if len(elem.text) >= 1:
            
            card4 = driver.find_element_by_xpath('/html/body/table/tbody/tr/th[4]/div')
            card4_data = card4.text
            embed.add_field(name="캐릭터4", value=card4_data, inline=True)
            
        else:
            embed.add_field(name="캐릭터4", value="없음", inline=True)
    except NoSuchElementException:
        embed.add_field(name="캐릭터4", value="없음", inline=True)
    try:
        elem = driver.find_element_by_xpath('/html/body/table/tbody/tr/th[5]/div')
        if len(elem.text) >= 1:
            
            card5 = driver.find_element_by_xpath('/html/body/table/tbody/tr/th[5]/div')
            card5_data = card5.text
            embed.add_field(name="캐릭터5", value=card5_data, inline=True)
            
        else:
            embed.add_field(name="캐릭터5", value="없음", inline=True)
    except NoSuchElementException:
        embed.add_field(name="캐릭터5", value="없음", inline=True)
    
    
    await message.channel.send(embed=embed)
access_token = os.environ['BOT_TOKEN']
client.run(access_token)
