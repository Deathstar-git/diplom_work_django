from time import sleep

import bs4 as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import re

import torch
from selenium.webdriver.support.wait import WebDriverWait
from transformers import AutoModelForSequenceClassification
from transformers import BertTokenizerFast

from main.models import Fridge, FridgeComment, FridgeGrade
from main.utils.assign_characteristics import assign_characteristics

tokenizer = BertTokenizerFast.from_pretrained('blanchefort/rubert-base-cased-sentiment-rusentiment')
model = AutoModelForSequenceClassification.from_pretrained('blanchefort/rubert-base-cased-sentiment-rusentiment',
                                                           return_dict=True)
labels = {1: 'Положительный', 2: 'Отрицательный', 0: 'Нейтральный'}


def predict(text):
    inputs = tokenizer(text, max_length=512, padding=True, truncation=True, return_tensors='pt')
    outputs = model(**inputs)
    predicted = torch.nn.functional.softmax(outputs.logits, dim=1)
    predicted = torch.argmax(predicted, dim=1).numpy()
    return predicted


def strip_space(s):
    while s.endswith(" ") or s.startswith(" "):
        if s.endswith(" "):
            s = s[:-1]
        if s.startswith(" "):
            s = s[1:]
    return s


# caps = DesiredCapabilities().CHROME
# # caps["pageLoadStrategy"] = "normal"  # complete
# caps["pageLoadStrategy"] = "eager"  # interactive
# # caps["pageLoadStrategy"] = "none"
chrome_options = Options()
chrome_options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=chrome_options)


def get_otzyvy(otz_url, ttl, fridge):
    driver.get(otz_url)
    sleep(3)
    _html = driver.page_source
    _soup = bs.BeautifulSoup(_html, features="html.parser")
    _divs = _soup.find_all('div', attrs={"class": ["sp-review-body-content"]})
    comments = []
    for _div in _divs:
        comment = _div.contents[0]
        grade = predict(comment)[0]
        if not FridgeComment.objects.filter(text=str(comment)).exists():
            fridge.fridgecomment_set.create(text=str(comment), grade=grade)
        fridge.save()
        comments.append(comment)
    # print('Комментарии к ' + ttl)
    if comments:
        # print('ОЦЕНКА ОТЗЫВОВ:')
        for comm in comments:
            # print(comm)
            grade = predict(comm)[0]
            # if grade == 1:
            #     print("Оценка:" + labels[1])
            # if grade == 2:
            #     print("Оценка:" + labels[2])
            # if grade == 0:
            #     print("Оценка:" + labels[0])
    else:
        print('Отзывов нет')
    return True


def get_harakteristiki(_url, _model):
    driver.get(_url)
    sleep(3)
    _html = driver.page_source
    _soup = bs.BeautifulSoup(_html, features="html.parser")
    _li = _soup.find_all('li', attrs={"class": ["item-characteristics__attrs-el"]})
    harakteristiki = {}
    for _l in _li:
        name_div = _l.find('div', attrs={
            "class": ["item-characteristics__attrs-el-name-wrap"]
        }). \
            find('span', attrs={"class": ["text item-characteristics__attrs-el-name"]})
        name = name_div.contents[0].replace('\n', '')
        name = strip_space(name)
        value_span = _l.find("span", recursive=False)
        if value_span:
            value = value_span.contents[0].replace('\n', '')
            value = strip_space(value)
            harakteristiki[name] = value
    assign_characteristics(_model, harakteristiki)
    print(harakteristiki)


def get_data(drvr):
    html = drvr.page_source
    soup = bs.BeautifulSoup(html, features="html.parser")
    fridge = []
    fridge_models = []
    divs = soup.find_all('div', attrs={'class': 'item-catalogue__item-name'})
    for div in divs:

        result = div.find('a')
        # title1 = re.sub('для работы', '', result.get('title'))
        # title2 = re.sub('для учебы', '', title1)
        # title3 = re.sub('\(ПИ\)', '', title2)
        # title_final = re.sub('игровой', '', title3)
        title_final = result.get('title')
        _url = "https://www.rbt.ru" + result['href']
        otzyvy_url = _url + 'otzyvy/'
        harakteristiki_url = _url + 'harakteristiki/'
        if not Fridge.objects.filter(title=title_final).exists():
            frg_model = Fridge.objects.create(title=title_final)
            fridge_models.append(frg_model)
            get_harakteristiki(harakteristiki_url, frg_model)
            get_otzyvy(otzyvy_url, title_final, frg_model)
            frg = {'title': title_final, 'item_url': _url, 'image_url': ''}
            fridge.append(frg)

    img_spans = soup.find_all('span', attrs={'class': 'image_format_item-catalogue'})
    imgs = []
    for span in img_spans:
        result = span.find('img')
        src = 'https:' + result.get('src')
        imgs.append(src)
    for i in range(len(fridge)):
        fridge_models[i].img_url = imgs[i]
        fridge_models[i].save()
        fridge[i]['image_url'] = imgs[i]
    print(f'Search Холодильники...')
    print(f'  Result ({len(fridge)}):')
    with open("rbt.txt", "w", encoding='windows-1251') as res_file:
        for f in fridge:
            res_file.write(f'    {f["title"]!r}: {f["item_url"]}\n')
            print(f'    {f["title"]!r}: {f["item_url"]}')
            print(f'Ссылка на картинку:{f["image_url"]}')
    return True


def run_parser():
    Fridge.objects.all().delete()
    FridgeComment.objects.all().delete()
    FridgeGrade.objects.all().delete()
    url = 'https://www.rbt.ru/cat/kuhonnaya_tehnika/holodilniki/'
    driver.get(url)
    WebDriverWait(driver, timeout=5).until(get_data)


run_parser()
