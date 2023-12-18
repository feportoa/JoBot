from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from bs4 import BeautifulSoup

url = "https://justremote.co/remote-developer-jobs"

# Configurar o Chrome para ser headless
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Inicializar o navegador
driver = webdriver.Chrome(options=chrome_options)

# Carregar uma página
driver.get("https://justremote.co/remote-developer-jobs")

bs = BeautifulSoup(driver.page_source, 'html.parser')

company = []
position = []
link = []

for job in bs.find_all('div', class_="new-job-item__JobItemWrapper-sc-1qa4r36-0"):
    for pos in job.find('a').find_all('div'):
        try:
            print(str(pos.get_text()) + str(pos.find('h3').get_text()))
            company.append(pos.find('div').get_text())
            position.append(pos.find('h3').get_text())
        except:
            print("[ERROR] Something went wrong")

    link.append("https://justremote.co/" + str(job.find('a').get('href')))

print(len(company))
print(len(position))
print(len(link))

df = pd.DataFrame(
    {
        "Company": company,
        "Position": position,
        "link": link
    }
)

df.to_csv('out.csv', index=False)