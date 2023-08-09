import openai
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

opcao = Options()
opcao.add_argument('--headless')

driver = webdriver.Chrome(options=opcao)
openai.api_key = "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"


def chat_redacao(tema, nl):
    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"escreva uma redação sobre {tema} com  no máximo {nl} linhas"}])
    return output.choices[0].message.content


def chat_resumos(tema):
    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"escreva um resumo curto sobre {tema}"}]
    )
    return output.choices[0].message.content


def slides(tema):
    driver.get(
        "https://auth.tome.app/u/login?state=hKFo2SBURTlDblZrUF93cWdhbHYwUUhjd0l1OHpPV2J1ZVpDRaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIHJPNkJsY00zNG1oNHVaSEE3TnllX2VQVGtNejVZbW1Jo2NpZNkgMHRScFdnMk5BU2k2cU1hejl1NlAzaXlDNHlwZ3JJRXI")
    driver.find_element('xpath', '//*[@id="username"]').send_keys("tome.usergpt@gmail.com")
    driver.find_element('xpath', '//*[@id="password"]').send_keys("Qwe15123002$", Keys.ENTER)
    sleep(15)
    driver.find_element('xpath',
                        '//*[@id="__next"]/div/div/div/div/div/div[2]/div/div[2]/button[2]/span[3]/span[2]/span').click()
    sleep(7)
    driver.find_element('xpath',
                        '/html/body/div[3]/div/div[1]/div/div/div[1]/div[1]/div[3]/div/div/div/div/div[2]/div').click()
    driver.find_element('xpath', '/html/body/div[3]/div/div[1]/div/div/div[1]/div[3]/div/div/div').send_keys(tema,
                                                                                                             Keys.ENTER)
    sleep(15)
    driver.find_element('xpath',
                        '/html/body/div[3]/div/div[1]/div/div/div[2]/div/div/div[3]/button/span[3]/span/span').click()
    sleep(30)
    sla = driver.current_url
    return sla


# escolha
escolha = int(input("""
Digíte a opção que você deseja:
    
[1] resumo
[2] slide
[3] redação
    
"""))
match escolha:
    # resumos:
    case 1:
        tema = input("sobre o que será o resumo?")
        print(chat_resumos(tema))
    # slides:
    case 2:
        tema = input("qual será o tema dos slides?")
        print(slides(tema))
    # redação:
    case 3:
        tema = input("qual será o tema da redação?")
        nl = input("quantas linha terá sua redação?")
        print(chat_redacao(tema, nl))
    case _:
        print("Digíte um valor valido.")
        

