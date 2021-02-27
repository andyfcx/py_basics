from lxml import etree

with open("sample.html") as f:
    text = f.read()

html = etree.HTML(text)
xpath1 = '//*[@id="app"]/div[3]/div/main/div/div[2]/table/tbody/tr[1]/td[4]/span/text()'
xpath2 = '//*[@id="app"]/div[3]/div/main/div/div[2]/table/tbody/tr[5]/td[4]/span/text()'
xpath_all = '//*[@id="app"]/div[3]/div/main/div/div[2]/table/tbody/tr/td[4]/span/text()'
print(html.xpath(xpath_all))

css1 = '#app > div.__window > div > main > div > div.search-result > table > tbody > tr:nth-child > td:nth-child(4) > span'
css2 = '#app > div.__window > div > main > div > div.search-result > table > tbody > tr:nth-child > td:nth-child(4) > span'
css3 = '#app > div.__window > div > main > div > div.search-result > table > tbody > tr > td:nth-child(4) > span '
print(html.cssselect(css3))

