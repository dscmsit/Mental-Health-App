from urllib.request import urlopen, Request
import re, json

'''
https://www.justdial.com/Chandigarh/Psychological-Counselling-Services/nct-11236852
https://www.psychologyindia.com/state/Chandigarh-Therapist
'''

'''
Uttar-Pradesh
Chandigarh
delhi
'''

# sweet old code

# def fetch_req(city):       
#     req = Request(
#         url= "https://www.psychologyindia.com/state/" + city + "-Therapist" , 
#         headers={'User-Agent': 'Mozilla/5.0'}
#     )
#     response = {"name":"none","link":"none"}
#     try:
#         html_code = urlopen(req).read().decode("utf-8")
#         # print(html_code)
#         start = html_code.find('<h3 class="title">') + len('<h3 class="title">')
#         end = html_code.find("</h3>")
#         name_find = html_code[start:end]
#         match = re.search(r'href=[\'"]?([^\'" >]+)', name_find)
#         if match:
#             response["link"]= match.group(1)
#         # print(name_find)
#         start = name_find.find('<b>') + len('<b>')
#         end = name_find.find('</b>')
#         if name_find[start:end]:
#             response["name"] = name_find[start:end]
#     except:
#         html_code = ""

#     return json.dumps(response)

def fetch_req(city):       
    res = {"name":[],"link":[]}
    # try:
    import requests
    from bs4 import BeautifulSoup

    # Make a GET request to the website you want to scrape
    url= "https://www.psychologyindia.com/state/" + city + "-Therapist"
    response = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0'})

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all occurrences of the element associated with the class you're interested in
    class_name = 'title'
    elements = soup.find_all(class_=class_name)

    # Get the first 5 occurrences
    for i in range(5):
        if i < len(elements):
            name_find= str(elements[i])
            match = re.search(r'href=[\'"]?([^\'" >]+)', name_find)
            if match:
                res["link"].append(match.group(1))
            # print(name_find)
            start = name_find.find('<b>') + len('<b>')
            end = name_find.find('</b>')
            if name_find[start:end]:
                res["name"].append(name_find[start:end])
            # except:
            #     pass
        else:
            break
    #     html_code = ""
    # except:
    return json.dumps(res)

fetch_req("Chandigarh")