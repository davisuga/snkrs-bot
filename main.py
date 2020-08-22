import selenium
import requests
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

chrome_options = selenium.webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs) 

chromewebdriver = selenium.webdriver.Chrome('./chromedriver', options=chrome_options)
email = ''
password = ''
password=r''
#This example requires Selenium WebDriver 3.13 or newer
def getLinks():
    headers = {
        'authority': 'www.nike.com.br',
        'accept': 'text/html, */*; q=0.01',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.nike.com.br/Snkrs/',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    params = (
        ('p', '3'),
        ('demanda', 'true'),
    )

    response = requests.get('https://www.nike.com.br/Snkrs/Estoque', headers=headers, params=params)
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', response.text)
    print(response.text)
    print(urls)
    
def waitSizeSelector(size):
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//input[@data-tamanho={}]'.format(size)))) //*[@id="tamanho__id42"]
    driver.find_element_by_xpath('//*[@id="tamanho__id{}"]'.format(size)).click()
    driver.execute_script('document.querySelector("#tamanho__id{}").checked=true'.format(size))
def wait(id):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,id)))
    pass
  
def click(xpath):
    try:
      driver.find_element_by_xpath(xpath).click()
    except:
      driver.execute_script('document.evaluate("{}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()'.format(xpath))
      
def fill_input(xpath, content):
    try:
      driver.find_element_by_xpath(xpath).send_keys(content)
    except:
      driver.execute_script('document.evaluate({}, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue = "{}"'.format(xpath, content))
      
def buySneaker(sneaker_link):

    sleep(3)    
    try:
      waitSizeSelector(40)
    except:
      waitSizeSelector(41)
    finally:
      try:
        waitSizeSelector(42)
      except:
        waitSizeSelector(43)
      finally:
          waitSizeSelector(44)
    #Comprar

    driver.find_element_by_xpath('//*[@id="btn-comprar"]').click()
    #Continuar
    driver.find_element_by_xpath('//*[@id="carrinho"]/div[4]/div/div[4]/a').click()
    #Seguir para pagamento
    driver.find_element_by_xpath('//*[@id="seguir-pagamento"]').click()
    #Confirmar e prosseguir
    driver.find_element_by_xpath('//*[@id="modalNotice_1g1q0sug2"]/div/div/div[3]/button[1]').click()
    #Confirmar pagamento
    driver.find_element_by_xpath('//*[@id="confirmar-pagamento"]').click()
    pass
with chromewebdriver as driver:
    driver.get("https://www.nike.com.br/Snkrs/Produto/Daybreak/153-169-211-222737")
    sleep(1)
    click('//*[@id="anchor-acessar"]')
    sleep(2)
    fill_input("//input[@type='email']", 'daviciencia1@gmail.com')
    fill_input("//input[@type='password']",password)
    
    click("//input[@value='ENTRAR']")
    sleep(1)
    buylist = ['https://www.nike.com.br/Snkrs/Produto/Daybreak/153-169-211-222737', 'https://www.nike.com.br/Snkrs/Produto/Air-Zoom-Pegasus-37/153-169-211-222452']
    for sneaker in buylist:
        buySneaker(sneaker)
        driver.get(sneaker)