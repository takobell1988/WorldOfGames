from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


def test_scores_service():
    Chrome_driver = webdriver.Chrome(executable_path='C:\Temp\chromedriver.exe')
    Chrome_driver.get('http://localhost:5000/')
    score_value = Chrome_driver.find_element_by_id("score").text

    if 1 < int(score_value) < 1000:
        return True
        Chrome_driver.close()
    else:
        print('test not pass!, bigger than 1000 or smaller then 1')
        return False
        Chrome_driver.close()


def main_function():
    try:
        a = test_scores_service()
        if a is True:
            print('finished sucessfully 0 ')
            return 0
        else:
            print('error , finished with exit code -1 ')
            return -1
    except BaseException as e:
        print(e.args)
        print("ERROR : could not perform test")


main_function()
