from requests_html import HTMLSession

s = HTMLSession()


def weather(query):
#query = "london"
    url = f"https://www.google.com/search?q=weather+{query}"

    r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'})
    temp = (r.html.find('span#wob_tm',first = True).text)
    time = (r.html.find('div.wob_dts',first = True).text)
    unit = (r.html.find('div.vk_bk.wob-unit span.wob_t',first = True).text)
    desc = (r.html.find('div.VQF4g',first = True).find('span#wob_dc',first = True).text)

    print(query.title(), time, temp, unit,  desc)


location = input("Give me the location where you wants to check weather : ")

weather(location)