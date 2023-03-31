

'''
Uttar-Pradesh
Chandigarh
delhi
'''


def fetch_req(city):
    result = []
    # try:
    import re
    import json
    import requests
    from bs4 import BeautifulSoup

    # Make a GET request to the website you want to scrape
    url = "https://www.psychologyindia.com/state/" + city + "-Therapist"
    response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'})

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all occurrences of the element associated with the class you're interested in
    title_class = 'title'
    title = soup.find_all(class_=title_class)

    desc_class = 'descriptions'
    desc = soup.find_all(class_=desc_class)
    # Get the first 5 occurrences
    for i in range(5):
        try:
            if i < len(title):
                res = {}

                name_find = str(title[i])
                desc_find = str(desc[i])

                match = re.search(r'href=[\'"]?([^\'" >]+)', name_find)
                if match:
                    res["link"] = match.group(1)

                # print(name_find)

                start = name_find.find('<b>') + len('<b>')
                end = name_find.find('</b>')
                if name_find[start:end]:
                    res["name"] = name_find[start:end]

                start = desc_find.find('<p>') + len('<p>')
                end = desc_find.find('<a')
                if desc_find[start:end]:
                    res["desc"] = desc_find[start:end]

                result.append(res)
            else:
                break
        except:
            print('Error while Scraping site')
    return json.dumps(result)

