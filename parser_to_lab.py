import requests
import csv
from bs4 import BeautifulSoup
import pandas


def get_html(url):
    response = requests.get(url)
    return response.text

def categories_link(html):
    category_links = []
    soup = BeautifulSoup(html,'html.parser')
    # category = soup.find('div', class_='leftmenu').find_all('div', class_='leftmenu-title')
    category1 = soup.find('div', class_='leftmenu').find_all('div', class_='leftmenu-title')[0]
    category1 = category1.find('a').get('href')
    category_links.append(category1)
    category2 = soup.find('div', class_='leftmenu').find_all('div', class_='leftmenu-title')[1]
    category2 = category2.find('a').get('href')
    category_links.append(category2)
    category3 = soup.find('div', class_='leftmenu').find_all('div', class_='leftmenu-title')[2]
    category3 = category3.find('a').get('href')
    category_links.append(category3)
    category4 = soup.find('div', class_='leftmenu').find_all('div', class_='leftmenu-title')[3]
    category4 = category4.find('a').get('href')
    category_links.append(category4)
    return category_links
    # category_link = all_category
    # print(category_links)
    # category_link1 = category.find_all('a')[1].get('href')
    # for cat in category:
    #     print(cat[1])
    #     try:
    #         category_link1 = cat.find_all('a')[1].get('href')
    #         print(category_link1)
    #     except:
    #         category_link = 'No category_link'

    # print(all_category)

def categories_name(html):
    category_names = []
    soup = BeautifulSoup(html,'html.parser')
    category1 = soup.find('div', class_='leftmenu').find_all('div', class_='leftmenu-title')[0]
    category1 = category1.find('a').text
    category_names.append(category1)
    category2 = soup.find('div', class_='leftmenu').find_all('div', class_='leftmenu-title')[1]
    category2 = category2.find('a').text
    category_names.append(category2)
    category3 = soup.find('div', class_='leftmenu').find_all('div', class_='leftmenu-title')[2]
    category3 = category3.find('a').text
    category_names.append(category3)
    category4 = soup.find('div', class_='leftmenu').find_all('div', class_='leftmenu-title')[3]
    category4 = category4.find('a').text
    category_names.append(category4)
    return category_names
    # all_category = soup.find('div', class_='leftmenu').find_all('div', class_='leftmenu-title')
    # print(category_names[2])
    # category_link = all_category
    # for cat in all_category:
    #     try:
    #         category_name1 = cat.find('a').text
    #
    #     except:
    #         category_name = 'No category_name'

def count_pages(html):
    soup = BeautifulSoup(html,'html.parser')
    pages = soup.find('div', class_='pager-wrap').find_all('a')[4].get('href')
    total_page = pages.split('=')[-1]
    # print(total_page)
    return int(total_page)


def writer(data):

    # frame1 = pandas.DataFrame('data', [('Name', str),('Category', str), ('Link',str)])

    frame = pandas.DataFrame(
            {
             'Name' : data,
             'Category': data,
             'Link' : data,
             }
        )
    csvFileContents = frame.to_csv(index=False)
    with open("kivano.csv", "a", encoding='utf-8') as f:
        f.write(csvFileContents)

    # with open('kivano.csv', 'a') as file:
    #     write = csv.writer(file)
    #     return write.writerow((
    #         data['title'],
    #         data['descript'],
    #         data['price'],
    #         data['status'],
    #         data['img']))

def get_data(html):
    url = 'https://www.kivano.kg'
    soup = BeautifulSoup(html, 'html.parser')
    ads = soup.find('div', class_='list-view').find_all('div', class_='item')
    cat = soup.find('div', class_='portlet-title').find_all('ul', class_='breadcrum2')
    lin = soup.find('div', class_='product_listbox').find_all('div', class_='listbox-title')
    for ad in ads:
        try:
            name = ad.find('div', class_='listbox_title').text
            # print(name)
        except:
            name = 'No name'
    for c in cat:
        try:
            category = c.find('a').text
            # print(category)
        except:
            category = 'No category'
    for l in lin:
        try:
            link = l.find('a').get('href')
            print(lin)
        except:
            link = 'No link'

        data = {
            'name': ads,
            'category': cat,
            'link': url + link,
            }
        # print(data)
        writer(data)

def main():
    url = 'https://www.kivano.kg'
    category_url = categories_link(get_html(url))
    for z in category_url:
        cat_url = url + z
        print(cat_url)
        # url = 'https://www.kivano.kg/prigotovlenie-pischi'
        page_part = '?page='
        tottal_pages = count_pages(get_html(cat_url))
        for i in range(1, tottal_pages+1):
            url_gen = cat_url + page_part + str(i)
            html = get_html(url_gen)
            get_data(html)
        # print(url_gen)


url = 'https://www.kivano.kg/prigotovlenie-pischi'
# url = 'https://www.kivano.kg/'
# count_pages(get_html(url))
# #print(get_html(url))
get_data(get_html(url))
# main()
# categories_link(get_html(url))
# categories_name(get_html(url))
