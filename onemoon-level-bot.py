import discord
client = discord.Client()
import requests
import urllib.request
from bs4 import BeautifulSoup
import selenium
import selenium.webdriver.support.ui as ui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
import os
@client.event
async def on_ready():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--window-size=1024,768')
    options.add_argument("--disable-gpu")
    global driver
    
    driver = webdriver.Chrome(executable_path='/app/.chromedriver/bin/chromedriver', options=options)
    
    driver.get('http://gss.skhidc.kr/')

    print('ready')
    
@client.event
async def on_message(message):
    if message.author.bot:
        return None
    
    if message.content == "멍멍":

        msg = await message.channel.send('됒됒')
       
    if message.content == "!색코드":

        msg = await message.channel.send('https://i.ibb.co/jvNyBcj/image.png')
        msg = await message.channel.send('색코드는 6, a, b, c, d, e, f만 사용가능합니다.')
    
    if message.content == "!일월 사이트":

        embed=discord.Embed(title='', color=0x00ff56)

        embed.add_field(name='일월 사이트', value="[사이트](http://om.skhidc.kr)", inline=True)

        await message.channel.send(embed=embed)

    if message.content == "!귀검 사이트":

        embed=discord.Embed(title='', color=0x00ff56)

        embed.add_field(name='귀검 사이트', value="[사이트](http://gss.skhidc.kr)", inline=True)

        await message.channel.send(embed=embed)
    
    if message.content == "!일월 후원":

        embed=discord.Embed(title='', color=0x00ff56)

        embed.add_field(name='일월 후원링크', value="[후원링크](https://skhcs.com/onemoon)", inline=False)

        await message.channel.send(embed=embed)

    if message.content == "!귀검 후원":

        embed=discord.Embed(title='', color=0x00ff56)

        embed.add_field(name='귀검 후원링크', value="[후원링크](https://skhcs.com/gss)", inline=False)

        await message.channel.send(embed=embed)
    
    if message.content == "!일월 추천":

        embed=discord.Embed(title='일월 추천링크', color=0x00ff56)

        embed.add_field(name='마인리스트', value="[마인리스트 링크](https://minelist.kr/servers/onemoon.skhidc.kr)", inline=False)
        embed.add_field(name='SKH리스트', value="[SKH리스트 링크](https://skhlist.com/server/79)", inline=False)

        await message.channel.send(embed=embed)

    if message.content == "!귀검 추천":

        embed=discord.Embed(title='귀검 추천링크', color=0x00ff56)

        embed.add_field(name='마인리스트', value="[마인리스트 링크](https://minelist.kr/servers/gss.skhidc.kr)", inline=False)
        embed.add_field(name='SKH리스트', value="[SKH리스트 링크](https://skhlist.com/server/324)", inline=False)

        await message.channel.send(embed=embed)
    
    if message.content == "!귀검 정보":

        msg = await message.channel.send('잠시만 기다려주세요')

        embed=discord.Embed(title='정보', color=0x00ff56)

        driver.get('https://skhlist.com/server/324')

        embed.add_field(name="이름", value='귀검', inline=True)
        embed.add_field(name="버전", value='1.15.2', inline=True)
        
        users = driver.find_element_by_xpath('/html/body/div[1]/section/div[2]/div/div[1]/div[1]/div[1]/div[2]/table[2]/tbody/tr/td[2]')
        users_data = users.text
        embed.add_field(name="접속자수(SKH리스트 기준)", value=users_data, inline=True)

        votes = driver.find_element_by_xpath('/html/body/div[1]/section/div[2]/div/div[1]/div[1]/div[1]/div[2]/table[2]/tbody/tr/td[3]')
        votes_data = votes.text
        embed.add_field(name="추천수(SKH리스트 기준)", value=votes_data, inline=True)
        
        await msg.delete()

        await message.channel.send(embed=embed)

    if message.content == "!일월 정보":

        msg = await message.channel.send('잠시만 기다려주세요')

        embed=discord.Embed(title='정보', color=0x00ff56)

        driver.get('https://skhlist.com/server/79')

        embed.add_field(name="이름", value='일월', inline=True)
        embed.add_field(name="버전", value='1.12.2', inline=True)
        
        users = driver.find_element_by_xpath('/html/body/div[1]/section/div[2]/div/div[1]/div[1]/div[1]/div[2]/table[2]/tbody/tr/td[2]')
        users_data = users.text
        embed.add_field(name="접속자수(SKH리스트 기준)", value=users_data, inline=True)

        await msg.delete()

        await message.channel.send(embed=embed)

    if message.content == "!드랍아이템":

        embed=discord.Embed(title='', color=0x00ff56)

        embed.add_field(name='드랍아이템', value="[링크](https://docs.google.com/spreadsheets/d/1ptOHHhR0sdQlc9NtuTvzep1IoliMmG0gnzSstB590Nk/edit#gid=0)", inline=False)

        await message.channel.send(embed=embed)

    if message.content.startswith('!귀검 랭킹'):

        msg = message.content.split()

        try:
            ranking1 = msg[2]
            page = msg[3]

        except IndexError:
            await message.channel.send('!귀검 랭킹 <이전 / 이후 / 문파 > <페이지>')

        if ranking1 == "이전":
            ranking = "before"

        elif ranking1 == "이후":
            ranking = "after"

        elif ranking1 == "문파":
            pass

        else:
            ranking = "이후"
            ranking = "after"

        if ranking1 == "이전" or ranking1 == "이후":
            
            info = ranking1+'랭킹'

            driver.get('http://gss.skhidc.kr/ranking.php?type=' + ranking)

            embed=discord.Embed(title=info, color=0x00ff56)

            try:
                page_1 = (int(page)-1)*10 + 1

            except ValueError:
                await message.channel.send('!귀검 랭킹 <이전 / 이후 / 문파 > <페이지>')
                
            page_2 = int(page)*10 + 1

            if int(page) <= 0 or int(page) >= 11:
                await message.channel.send('페이지는 1부터 10까지만 가능합니다.')

            else:
                for i in range(page_1,page_2):
                    

                    name = driver.find_element_by_xpath(f'//*[@id="table"]/div/table/tbody/tr[{i}]/td[2]')
                    job = driver.find_element_by_xpath(f'//*[@id="table"]/div/table/tbody/tr[{i}]/td[4]')
                    level = driver.find_element_by_xpath(f'//*[@id="table"]/div/table/tbody/tr[{i}]/td[5]')
                    
                    name_data = name.text
                    job_data = job.text
                    level_data = level.text
                    
                    card = '닉네임: ' + name_data + '\n직업: ' + job_data + '\n레벨: ' + level_data
                    embed.add_field(name=i, value=card, inline=True)

                await message.channel.send(embed=embed)

        if ranking1 == "문파":

            info = "문파랭킹"

            driver.get('http://gss.skhidc.kr/guild.php')

            embed=discord.Embed(title=info, color=0x00ff56)

            try:
                page_1 = (int(page)-1)*10 + 1

            except ValueError:
                await message.channel.send('!귀검 랭킹 <이전 / 이후 / 문파 > <페이지>')
                
            page_2 = int(page)*10 + 1

            try:
                for i in range(page_1,page_2):

                    name = driver.find_element_by_xpath(f'//*[@id="table"]/div/table/tbody/tr[{i}]/td[2]')
                    level = driver.find_element_by_xpath(f'//*[@id="table"]/div/table/tbody/tr[{i}]/td[3]')
                            
                    name_data = name.text
                    level_data = level.text
                            
                    card = '문파명: ' + name_data + '\n레벨: ' + level_data
                    embed.add_field(name=i, value=card, inline=True)

            except NoSuchElementException:
                pass

            await message.channel.send(embed=embed)
    
    if message.content.startswith('!일월 랭킹'):

        msg = message.content.split()

        ranking1 = msg[2]
        page1 = msg[3]

        try:
            page = int(page1)

        except ValueError:
            await message.channel.send('!일월 랭킹 <일반 / 기문 / 만렙> <페이지>')

        if (page >= 1 and page <=10):
            page = str(page1)

        else:
            page = '1'

        if ranking1 == "일반":
            ranking = "top"

        elif ranking1 == "기문":
            ranking = "top2"

        elif ranking1 == "만렙":
            ranking = "king"

        else:
            ranking = "일반"
            ranking = "top"

        info = ranking1+'랭킹'+page

        req = requests.get('http://om.skhidc.kr/level'+ranking+'.php'+'?page='+page)  
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        embed=discord.Embed(title=info, color=0x00ff56)

        try:
            table = soup.find('table', {'class': 'table table-bordered'})
            trs = table.find_all('tr')
            for idx, tr in enumerate(trs):
                if idx > 0:
                    tds = tr.find_all('td')
                    ranking = tds[0].text.strip()
                    nickname = tds[1].text.strip()
                    job = tds[3].text.strip()
                    level = tds[4].text.strip()
                    embed.add_field(name=ranking, value='닉네임: ' + nickname + '\n직업: ' + job + '\n레벨: ' + level, inline=True)
                    
        except AttributeError:
            info = ranking1+'랭킹 '+page+' (기록없음)'
            embed=discord.Embed(title=info, color=0x00ff56)

        await message.channel.send(embed=embed)
    
    if message.content.startswith('!일월 괴영'):

        msg = message.content.split()

        season1 = msg[2]

        try:
            season = int(season1)

        except ValueError:
            await message.channel.send('!일월 괴영 <시즌> <직업>')

        else:
            pass

        finally:
            pass
                
        job1 = msg[3]

        if job1 == "검객":
            job = "swordman"

        elif job1 == "자객":
            job = "assassin"

        elif job1 == "궁사":
            job = "archer"

        elif job1 == "진사":
            job = "jinsa"

        elif job1 == "닌자":
            job = "ninja"

        elif job1 == "월사":
            job = "axewarrier"

        elif job1 == "법사":
            job = "magician"

        elif job1 == "창술사":
            job = "spearman"

        else:
            job = "swordman"
            job1 = "검객"

        if season == 7:
            season = str(season1)
            req = requests.get('http://om.skhidc.kr/carnivaltop.php?job='+job)  
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
            info = message.content[4:8]+' '+job1

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

        msg = message.content.split()

        Name = msg[2]

        driver.get('http://om.skhidc.kr/')
        
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
                embed.set_thumbnail(url=f"https://minotar.net/avatar/{Name}/100.png")

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
                embed.set_thumbnail(url=f"https://minotar.net/avatar/{Name}/100.png")

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
                embed.set_thumbnail(url=f"https://minotar.net/avatar/{Name}/100.png")

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
                embed.set_thumbnail(url=f"https://minotar.net/avatar/{Name}/100.png")

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
                embed.set_thumbnail(url=f"https://minotar.net/avatar/{Name}/100.png")

            else:
                embed.add_field(name="캐릭터5", value="없음", inline=True)
        except NoSuchElementException:
            embed.add_field(name="캐릭터5", value="없음", inline=True)


        await message.channel.send(embed=embed)
        
    if message.content.startswith('!귀검 검색'):
        
        msg = message.content.split()

        Name = msg[2]

        driver.get('http://gss.skhidc.kr/ranking.php')
        
        search_box = driver.find_element_by_class_name('form-control')
        search_box.send_keys(Name)
        search_box.send_keys(Keys.RETURN)
        
        embed=discord.Embed(title=Name, color=0x00ff56)
        try:
            elem = driver.find_element_by_xpath('//*[@id="table"]/table/tbody/tr/td[1]/div/p[1]/font/strong')
            if len(elem.text) >= 1:

                card1 = driver.find_element_by_xpath('//*[@id="table"]/table/tbody/tr/td[1]/div/p[1]/font/strong')
                card2 = driver.find_element_by_xpath('//*[@id="table"]/table/tbody/tr/td[1]/div/p[2]')
                card1_data = card1.text
                card2_data = card2.text
                card = card1_data + card2_data
                embed.add_field(name="캐릭터1", value=card, inline=True)
                embed.set_thumbnail(url=f"https://minotar.net/avatar/{Name}/100.png")

            else:
                embed.add_field(name="캐릭터1", value="없음", inline=True)
        except NoSuchElementException:
            embed.add_field(name="캐릭터1", value="없음", inline=True)
        try:
            elem = driver.find_element_by_xpath('//*[@id="table"]/table/tbody/tr/td[2]/div/p[1]/font/strong')
            if len(elem.text) >= 1:

                card1 = driver.find_element_by_xpath('//*[@id="table"]/table/tbody/tr/td[2]/div/p[1]/font/strong')
                card2 = driver.find_element_by_xpath('//*[@id="table"]/table/tbody/tr/td[2]/div/p[2]')
                card1_data = card1.text
                card2_data = card2.text
                card = card1_data + card2_data
                embed.add_field(name="캐릭터2", value=card, inline=True)

            else:
                embed.add_field(name="캐릭터2", value="없음", inline=True)
        except NoSuchElementException:
            embed.add_field(name="캐릭터2", value="없음", inline=True)
        try:
            elem = driver.find_element_by_xpath('//*[@id="table"]/table/tbody/tr/td[3]/div/p[1]/font/strong')
            if len(elem.text) >= 1:

                card1 = driver.find_element_by_xpath('//*[@id="table"]/table/tbody/tr/td[3]/div/p[1]/font/strong')
                card2 = driver.find_element_by_xpath('//*[@id="table"]/table/tbody/tr/td[3]/div/p[2]')
                card1_data = card1.text
                card2_data = card2.text
                card = card1_data + card2_data
                embed.add_field(name="캐릭터3", value=card, inline=True)

            else:
                embed.add_field(name="캐릭터3", value="없음", inline=False)
        except NoSuchElementException:
            embed.add_field(name="캐릭터3", value="없음", inline=False)
        try:
            elem = driver.find_element_by_xpath('//*[@id="table"]/table/tbody/tr/td[4]/div/p[1]/font/strong')
            if len(elem.text) >= 1:

                card1 = driver.find_element_by_xpath('//*[@id="table"]/table/tbody/tr/td[4]/div/p[1]/font/strong')
                card2 = driver.find_element_by_xpath('//*[@id="table"]/table/tbody/tr/td[4]/div/p[2]')
                card1_data = card1.text
                card2_data = card2.text
                card = card1_data + card2_data
                embed.add_field(name="캐릭터4", value=card, inline=True)

            else:
                embed.add_field(name="캐릭터4", value="없음", inline=True)
        except NoSuchElementException:
            embed.add_field(name="캐릭터4", value="없음", inline=True)
        try:
            elem = driver.find_element_by_xpath('//*[@id="table"]/table/tbody/tr/td[5]/div/p[1]/font/strong')
            if len(elem.text) >= 1:

                card1 = driver.find_element_by_xpath('//*[@id="table"]/table/tbody/tr/td[5]/div/p[1]/font/strong')
                card2 = driver.find_element_by_xpath('//*[@id="table"]/table/tbody/tr/td[5]/div/p[2]')
                card1_data = card1.text
                card2_data = card2.text
                card = card1_data + card2_data
                embed.add_field(name="캐릭터5", value=card, inline=True)

            else:
                embed.add_field(name="캐릭터5", value="없음", inline=True)
        except NoSuchElementException:
            embed.add_field(name="캐릭터5", value="없음", inline=True)

        await message.channel.send(embed=embed)

access_token = os.environ['BOT_TOKEN']
client.run(access_token)
