
import requests
from bs4 import BeautifulSoup
headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}

DOLLAR_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=rehc+&aqs=chrome.1.69i57j0i10i131i433l3j0i131i433j0i10i131i433l5.4385j1j7&sourceid=chrome&ie=UTF-8'
full_page = requests.get(DOLLAR_RUB, headers=headers)
soup1 = BeautifulSoup(full_page.content, 'html.parser')
convert = soup1.findAll("span", {"class": "DFlfde", "data-precision": "2"})

EURO_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&sxsrf=APq-WBsfmxM72JYmPIVfwCW7UmQnll0ooQ%3A1647678467939&ei=A5Q1YrzrOOeprgTpqZvICw&oq=%D0%BA%D1%83%D1%80%D1%81+t&gs_lcp=Cgdnd3Mtd2l6EAEYATIFCAAQgAQyBwgAEIAEEAoyCAgAEIAEELEDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCAAQRxCwAzoHCAAQsAMQQ0oECEEYAEoECEYYAFC9Bli9BmCFEGgBcAF4AIABR4gBR5IBATGYAQCgAQHIAQrAAQE&sclient=gws-wiz'
full_page1 = requests.get(EURO_RUB, headers=headers)
soup2 = BeautifulSoup(full_page1.content, 'html.parser')
convert2 = soup2.findAll("span", {"class": "DFlfde", "data-precision": "2"})

yuan = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D1%8E%D0%B0%D0%BD%D1%8F+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sxsrf=APq-WBvtHwTgl9FiCUyz3GuvFsqr0E3ndg%3A1647679555960&ei=Q5g1YreeOon8rgS16YjwDg&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%8E%D0%B0%D0%BD&gs_lcp=Cgdnd3Mtd2l6EAEYADIJCCMQJxBGEIICMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCggAEIAEEIcCEBQyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIICAAQsQMQgwE6BwgjELADECc6BwgAEEcQsAM6CggAEEcQsAMQyQM6BwgAELADEEM6BAgjECdKBAhBGABKBAhGGABQowZYyAlgiR5oAXABeACAAViIAeoBkgEBM5gBAKABAcgBCsABAQ&sclient=gws-wiz'
full_page3 = requests.get(yuan, headers=headers)
soup3 = BeautifulSoup(full_page3.content, 'html.parser')
convert3 = soup3.findAll("span", {"class": "DFlfde", "data-precision": "2"})

FTS = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D1%84%D1%83%D0%BD%D1%82%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sxsrf=APq-WBsIGThDF6NQ_8UusvdOrwE3jVj7WQ%3A1647679773634&ei=HZk1Yr2bJrmWjgb52pmYDQ&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%84%D1%83&gs_lcp=Cgdnd3Mtd2l6EAEYADIECCMQJzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgUIABCABDIFCAAQgAQyCggAEIAEEIcCEBQyCwgAEIAEELEDEIMBMgUIABCABDIFCAAQgAQyBQgAEIAEOgcIIxCwAxAnOgcIABBHELADOgoIABBHELADEMkDOgcIABCwAxBDOhAIABCABBCHAhCxAxCDARAUSgQIQRgASgQIRhgAUNAIWMcJYMAWaAFwAXgAgAFJiAGHAZIBATKYAQCgAQHIAQrAAQE&sclient=gws-wiz'
full_page4 = requests.get(FTS, headers=headers)
soup4 = BeautifulSoup(full_page4.content, 'html.parser')
convert4 = soup4.findAll("span", {"class": "DFlfde", "data-precision": "2"})

BTC = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0&sxsrf=APq-WBtz4HB5JCRtPkTbWZYtBvE1uUOvng%3A1647696198297&ei=Rtk1YtfCEZGHwPAPlMCEsAw&oq=%D0%BA%D1%83%D1%80%D1%81+ethereum&gs_lcp=Cgdnd3Mtd2l6EAEYATIHCCMQsAMQJzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzISCC4QxwEQ0QMQyAMQsAMQQxgBMhIILhDHARCjAhDIAxCwAxBDGAFKBAhBGABKBAhGGABQAFgAYNAJaAFwAXgAgAEAiAEAkgEAmAEAyAELwAEB2gEECAEYCA&sclient=gws-wiz'
full_page5 = requests.get(BTC, headers=headers)
soup5 = BeautifulSoup(full_page5.content, 'html.parser')
convert5 = soup5.findAll("span", {"class": "pclqee"})
convert5_1 = soup5.findAll("span", {"jsname": "SwWl3d"})
btc = f'Курс: {convert5[0].text} рублей к bitcoin\n{convert5_1[0].text} рублей за сегодня'

ETH = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+ethereum&sxsrf=APq-WBunropC-XDTCZvt9uVidDdOhFuhOQ%3A1647680888756&ei=eJ01YvPkLaL1qwGK75zYCg&oq=%D0%BA%D1%83%D1%80%D1%81+eth&gs_lcp=Cgdnd3Mtd2l6EAEYADIJCCMQJxBGEIICMgoIABCABBCHAhAUMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6CggAEEcQsAMQyQM6BwgAELADEEM6EgguEMcBEKMCEMgDELADEEMYAToSCC4QxwEQ0QMQyAMQsAMQQxgBOgQIIxAnOgsIABCABBCxAxCDAUoECEEYAEoECEYYAFDVB1iIC2CkEWgBcAF4AIABRYgBygGSAQEzmAEAoAEByAENwAEB2gEECAEYCA&sclient=gws-wiz'
full_page6 = requests.get(ETH, headers=headers)
soup6 = BeautifulSoup(full_page6.content, 'html.parser')
convert6 = soup6.findAll("span", {"class": "pclqee"})
convert6_1 = soup6.findAll("span", {"jsname": "SwWl3d"})
eth = f'Курс: {convert6[0].text} рублей к ethereum\n{convert6_1[0].text} рублей за сегодня'


pogoda = 'https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+%D1%87%D0%B5%D1%80%D0%BD%D0%BE%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BA%D0%B5&sxsrf=APq-WBuZCn6M_3VwNyuTSobvTigWhtyVEQ%3A1647636710208&ei=5vA0Yv6lDLWWjga4tJn4Aw&oq=gjujlf+&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCCMQsQIQJzIKCAAQsQMQgwEQCjINCAAQsQMQgwEQyQMQCjIFCAAQkgMyBQgAEJIDMgoIABCxAxCDARAKMggIABCxAxCDATIICAAQsQMQgwEyCAgAELEDEIMBMggIABCxAxCDAToHCCMQsAMQJzoHCAAQRxCwAzoLCAAQgAQQsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOggIABCABBCxAzoLCC4QgAQQsQMQgwE6EAguELEDEIMBEMcBENEDEEM6DggAEIAEELEDEAoQARAqOgwIABCABBCxAxAKEAE6CwguEIAEEMcBEK8BOg8IABCABBCxAxCDARAKEAE6CQgAEIAEEAoQAToFCAAQgAQ6CwgAEIAEEAoQARAqOgcIABCABBAKOgwIABCABBDJAxAKEAE6CggAELEDEIMBEENKBAhBGABKBAhGGABQiQhYkw5gnBxoAXABeACAAZ0BiAGxBJIBAzYuMZgBAKABAcgBCcABAQ&sclient=gws-wiz'
full = requests.get(pogoda, headers=headers)
soup = BeautifulSoup(full.content, 'html.parser')
conv = soup.findAll("span", {"class": "wob_t"})
conv1 = soup.findAll("span", {"id": "wob_pp"})
conv2 = soup.findAll("span", {"id": "wob_hm"})
conv3 = soup.findAll("span", {"id": "wob_ws"})
conv4 = soup.findAll("span", {"id": "wob_dc"})
conv5 = soup.findAll("div", {"class": "wob_loc q8U8x"})
conv6 = soup.findAll("div", {"class": "wob_dts"})

veter = 'https://www.gismeteo.ru/weather-chernogolovka-12650/'
ful = requests.get(veter, headers=headers)
soup1 = BeautifulSoup(ful.content, 'html.parser')
conv7 = soup1.findAll("div",{"class": "direction"})

glob_pog = f'{conv6[0].text.capitalize()}\n{conv5[0].text}\nСейчас {conv4[0].text.lower()}\nТемпература: {conv[0].text}°C\nВероятность осадков: {conv1[0].text}\nВлажность: {conv2[0].text}\nВетер: {conv3[0].text}  {conv7[0].text}'

vremya = 'https://24timezones.com/mirovoe_vremia.php'
vr = requests.get(vremya, headers=headers)
vre = BeautifulSoup(vr.content, 'html.parser')
v1 = vre.findAll("span", {"class": "time_format_24"})
