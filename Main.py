from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\chromedriver.exe")
driverbot = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\Google\chromedriver.exe")
driver.get('https://web.whatsapp.com/')
driverbot.get(
    'https://assistant-us-south.watsonplatform.net/us-south/crn:v1:bluemix:public:conversation:us-south:a~2F3f86fa858fa14ff9858aeb981d42afdd:7ca225fd-0469-41d9-8c7c-03fb2d31901c::/workspaces/f66e3f3c-0675-4924-b44f-23bff592f886/build/intents')
x = 0

iniciar = input('iniciar( o qr deve ser escaneado e a conversa com o bot iniciada) :')

name = 'Vitoria'
msg_whats = driverbot.find_element_by_id('-chatPanel_exchange{}_part0'.format(x))
mensagem = msg_whats.text
msg = str(mensagem)

# msg_whats = driverbot.find_element_by_xpath('//div[@class = "textResponse"]')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
iniciar = input('depois de clicar no contato prosseguir?')

msg_box = driver.find_element_by_class_name('_2S1VP')
msg_box.send_keys(msg)
iniciar = input('Enviar?')
#WebDriverWait(driver, 30)
button = driver.find_element_by_class_name('_35EW6')
button.click()

iniciar = input('seguir para a espera pela mensagem?')
#driver.find_element_by_class_name('_1aTxu').click()

x=1
while (True):
    wait = WebDriverWait(driver, 40)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'OUeyt')))
    contador = int(driver.find_element_by_class_name('OUeyt').text)
    if ( contador> 0):
        # user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        # user.click()
        msgm_do_whats = driver.find_elements_by_xpath('//span[@class = "selectable-text invisible-space copyable-text"]')[-1]
        #msgm_do_whats = driver.find_elements_by_class_name("selectable-text invisible-space copyable-text")[-1]
        msgm_do_whats_conv = msgm_do_whats.text
        caixa_de_texto = driverbot.find_element_by_id('-chatPanel__submitInput')
        caixa_de_texto.send_keys(str(msgm_do_whats_conv))
        caixa_de_texto.send_keys(Keys.ENTER)
        #adicionado para teste
        #posicao_chat = '-chatPanel_exchange{}_part0'.format(x)

        #novoelement = wait.until(EC.presence_of_element_located((By.ID, '-chatPanel_exchange{}_part0'.format(x))))
        input('Foi gerada a mensagem?')
        msg_whats = driverbot.find_element_by_id('-chatPanel_exchange{}_part0'.format(x))
        x=x+1
        mensagem = msg_whats.text
        msg = str(mensagem)
        msg_box = driver.find_element_by_class_name('_2S1VP')
        msg_box.send_keys(msg)
        iniciar = input('Enviar?')
        # WebDriverWait(driver, 30)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()


    else:
        print('Ninguem escreveu nada')