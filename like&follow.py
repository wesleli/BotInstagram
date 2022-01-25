from logar import login, wd, By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import datetime
import random
import time


#Pesquise por tags e vá para a postagem mais recente
def search():
    try:
        global tags
        tag = random.choice(tags)
        address = 'https://www.instagram.com/explore/tags/'
        wd.get(address + tag)
        time.sleep(random.randint(3, 4))
        wd.find_elements(By.CLASS_NAME, '_9AhH0')[10].click()
        time.sleep(random.randint(3, 4))
    except:
        print("ocorreu um erro")


#Curtir
def like():
    global like_cnt
    global users_liked
    global num_error
    global action
    #Manipulação de exceção
    try:
        #Coleta nome do usuário
        user_name = wd.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/span/a').text

        #se o usuário já foi curtido
        if user_name in users_liked:

            #procura usuário ainda não seguido
            while user_name in users_liked:
                wd.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/div[2]/button').click()
                time.sleep(random.randint(3, 4))
                user_name = wd.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/span/a').text
                time.sleep(random.randint(3, 4))
            

        #se o usuário ainda não foi curtido
        if user_name not in users_liked:
            users_liked.append(user_name)
            time.sleep(random.randint(4, 5))
            wd.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/span/a').click()
            time.sleep(random.randint(4, 5))
            wd.find_elements(By.CLASS_NAME, '_9AhH0')[1].click()
            time.sleep(random.randint(4, 5))
            num_like = 0
            while num_like < 3:
                wd.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button').click()
                time.sleep(random.randint(4, 5))               
                wd.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.ARROW_RIGHT)
                time.sleep(random.randint(4, 5))
                num_like += 1
            wd.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button').click()
            time.sleep(random.randint(4, 5))


        like_cnt += 3
    except:
        print('ocorreu um erro')
        num_error += 1

if __name__ == '__main__':

    #Configuração de tags
    tags = ['escolha_uma_tag']

    num_error = 0
    users_liked = []
    like_cnt = 0
    begin = datetime.datetime.today()
    

    login()

    #Controle número de curtidas
    while like_cnt < 200:
        search()
        like()
        
    #finalizar webdriver
    wd.quit()
    end = datetime.datetime.today()


    #criar arquivo de log com informações para controle
    dados = {
        'Número de Likes': like_cnt,
        'Usuários Curtidos': users_liked,
        'Número de Erros': num_error,
        'Data e Horário de Início': begin,
        'Data e Horário do Fim': end
    }

    serie_log = str(begin)
    print(serie_log)
    serie_log = serie_log.replace(" ", "")
    print(serie_log)
    serie_log = serie_log.replace(":", "")
    print(serie_log)
    serie_log = serie_log.replace(".", "")
    print(serie_log)

    log = pd.DataFrame(dados, index=[1])
    log.to_csv('./logs/logLikes'+serie_log+'.csv')
