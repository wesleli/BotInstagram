from logar import login, wd, username, By
import pandas as pd
import time
import datetime


def get_followers():
    time.sleep(15)
    wd.get('https://www.instagram.com/' + username)
    time.sleep(15)
    followers = wd.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    followers.click()
    time.sleep(15)
    scroll_box = wd.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')
    prev_height, height = 0, 1

    while prev_height != height:

        prev_height = height
        height = wd.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);return arguments[0].scrollHeight;""", scroll_box)
        time.sleep(7)
    links = scroll_box.find_elements(By.TAG_NAME, 'a')
    names = [name.text for name in links if name.text != '']
    close = wd.find_element(By.XPATH, "/html/body/div[6]/div/div/div[1]/div/div[2]/button")
    close.click()
    dados = {
        'Nome': names
    }
    pessoas = pd.DataFrame(dados)
    pessoas.to_csv('seguidores.csv')
    print(len(links))
    return names

def get_following():
    time.sleep(15)
    wd.get('https://www.instagram.com/' + username)
    following = wd.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
    following.click()
    time.sleep(15)
    scroll_box = wd.find_element(By.XPATH, '/html/body/div[6]/div/div/div[3]')
    prev_height, height = 0, 1

    while prev_height != height:

        prev_height = height
        height = wd.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);return arguments[0].scrollHeight;""", scroll_box)
        time.sleep(7)
    links = scroll_box.find_elements(By.TAG_NAME, 'a')
    names = [name.text for name in links if name.text != '']
    close = wd.find_element(By.XPATH, "/html/body/div[6]/div/div/div[1]/div/div[2]/button")
    close.click()
    dados = {
        'Nome': names
    }
    pessoas = pd.DataFrame(dados)
    pessoas.to_csv('seguindo.csv')
    return names
  

def unfollow():
    global num_unfollow
    global followers
    global following
    global error_unfollow
    time.sleep(5)

   

    for user in following:
        if user in followers:
            continue

        if num_unfollow >= 140:
            return    

        if user not in followers:
            try:
                time.sleep(20)
                wd.get('https://www.instagram.com/' + user)
                time.sleep(15)
                unfollow_box = wd.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button')
                unfollow_box.click()
                time.sleep(15)
                unfollow_button = wd.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/button[1]')
                unfollow_button.click()
                time.sleep(10)
                num_unfollow += 1
                continue
            except:
                error_unfollow += 1
                print('Ocorreu um Erro')
                continue

if __name__ == '__main__':


    begin = datetime.datetime.today()
    login()
    
    followers = get_followers()
    following = get_following()
    num_followers = len(followers)
    num_unfollowing = len(following)
    num_unfollow = 0
    error_unfollow = 0
    

    
    unfollow()

    wd.quit()
    end = datetime.datetime.today()

    dados = {
        'Seguidores':num_followers,
        'Seguindo':num_unfollowing,
        'Deixados de Seguir':num_unfollow,
        'Erros':error_unfollow,
        'Data e Horario de Inicio':begin,
        "Data e Horario de Finalizacao": end
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
log.to_csv('./logs/logUnfollow'+serie_log+'.csv')
    