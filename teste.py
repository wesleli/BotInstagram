#from logar import login, wd
from selenium.webdriver.common.by import By
import time
import pandas as pd
import datetime

tags = {
    'tag': pd.read_csv('./tags.csv')
    }


following = []
following.append(tags)



print(following)