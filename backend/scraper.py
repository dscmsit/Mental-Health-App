from urllib.request import urlopen, Request
import re, json

'''
https://www.justdial.com/Chandigarh/Psychological-Counselling-Services/nct-11236852
https://www.psychologyindia.com/state/Chandigarh-Therapist
'''

'''
Uttar-Pradesh
Chandigarh
'''

def fetch_req(city):       
    req = Request(
        url= "https://www.psychologyindia.com/state/" + city + "-Therapist" , 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    response = {"name":"none","link":"none"}
    html_code = urlopen(req).read().decode("utf-8")

    # print(html_code)
    start = html_code.find('<h3 class="title">') + len('<h3 class="title">')
    end = html_code.find("</h3>")
    name_find = html_code[start:end]
    match = re.search(r'href=[\'"]?([^\'" >]+)', name_find)
    if match:
        response["link"]= match.group(1)
    # print(name_find)
    start = name_find.find('<b>') + len('<b>')
    end = name_find.find('</b>')
    if name_find[start:end]:
        response["name"] = name_find[start:end]

    return json.dumps(response)

print(fetch_req("Chandigarh"))