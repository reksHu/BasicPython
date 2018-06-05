from bs4 import BeautifulSoup
import requests
url ="https://support.office.com/en-us/article/sharepoint-2010-training-c0e164fa-febc-4e6a-8f62-80d2043056c7"

res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
sections = soup.select(".ocpSection section.ocpSection table tbody")
for sec in sections:
    # print(sec.text)
    tds = sec.select("td")
    for td in tds:
        print(td.select("p")[0].text)
        print(td.select("p")[1].text)
        links = td.find_all("a")
        for l in links:
            href = l.get('href')
            if("http" in href):
                print(l.get('href'))
            else:
                print("https://support.office.com/en-us/article/"+l.get('href'))

