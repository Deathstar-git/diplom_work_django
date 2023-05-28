from time import sleep
import bs4 as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import torch
from selenium.webdriver.support.wait import WebDriverWait
from transformers import AutoModelForSequenceClassification
from transformers import BertTokenizerFast
from main.models import MobilePhone, MobilePhoneComment
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


chrome_options = Options()
chrome_options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=chrome_options)


def get_otzyvy(otz_url, ttl, mobile_phone):
    driver.get(otz_url)
    sleep(3)
    _html = driver.page_source
    _soup = bs.BeautifulSoup(_html, features="html.parser")
    _divs = _soup.find_all('div', attrs={"class": ["sp-review-body-content"]})
    comments = []
    for _div in _divs:
        comment = _div.contents[0]
        grade = predict(comment)[0]
        if not MobilePhoneComment.objects.filter(text=str(comment)).exists():
            mobile_phone.mobilephonecomment_set.create(text=str(comment), grade=grade)
        mobile_phone.save()
        comments.append(comment)
    print('Комментарии к ' + ttl)
    if comments:
        print('ОЦЕНКА ОТЗЫВОВ:')
        for comm in comments:
            print(comm)
            grade = predict(comm)[0]
            if grade == 1:
                print("Оценка:" + labels[1])
            if grade == 2:
                print("Оценка:" + labels[2])
            if grade == 0:
                print("Оценка:" + labels[0])
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
    phone = []
    phone_models = []
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
        if not MobilePhone.objects.filter(title=title_final).exists():
            phn_model = MobilePhone.objects.create(title=title_final)
            phone_models.append(phn_model)
            get_harakteristiki(harakteristiki_url, phn_model)
            get_otzyvy(otzyvy_url, title_final, phn_model)
            phn = {'title': title_final, 'item_url': _url, 'image_url': ''}
            phone.append(phn)

    img_spans = soup.find_all('span', attrs={'class': 'image_format_item-catalogue'})
    imgs = []
    for span in img_spans:
        result = span.find('img')
        src = 'https:' + result.get('src')
        imgs.append(src)
    for i in range(len(phone)):
        phone_models[i].img_url = imgs[i]
        phone_models[i].save()
        phone[i]['image_url'] = imgs[i]
    print(f'Search Мобильные телефоны...')
    print(f'  Result ({len(phone)}):')
    with open("rbt.txt", "w", encoding='windows-1251') as res_file:
        for p in phone:
            res_file.write(f'    {p["title"]!r}: {p["item_url"]}\n')
            print(f'    {p["title"]!r}: {p["item_url"]}')
            print(f'Ссылка на картинку:{p["image_url"]}')
    return True


def run_parser():
    MobilePhone.objects.all().delete()
    MobilePhoneComment.objects.all().delete()
    url = 'https://msk.rbt.ru/cat/cifrovye_ustroistva/mobilnye_telefony/'
    driver.get(url)
    WebDriverWait(driver, timeout=5).until(get_data)


run_parser()
