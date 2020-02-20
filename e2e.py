from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


def test_scores_service():
    print("selenium do tests")
    try:
        Chrome_driver = webdriver.Chrome(executable_path='C:\Temp\chromedriver.exe')
        Chrome_driver.get('http://localhost:5000/')
        score_value = Chrome_driver.find_element_by_id("score").text

        if 1 < int(score_value) < 1000:
            print(score_value)
            return True
        else:
            print('test not pass!')
            return False
        Chrome_driver.close()
    except BaseException as e:
        print(e.args)
        print("ERROR : could not perform test")
        Chrome_driver.close()



test_scores_service()

