from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


def test_scores_service():
    print("selenium do tests")
    try:
        Chrome_driver = webdriver.Chrome(executable_path='C:\Temp\chromedriver.exe')
        Chrome_driver.get('http://localhost:5000/')
        Chrome_driver.find_element_by_id("videoURL").send_keys(str(line))
        Chrome_driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div/div/div/form/select/optgroup/option[3]').click()
        sleep(2)
        Chrome_driver.find_element_by_name("submitForm").click()
        sleep(80)
        Chrome_driver.find_element_by_xpath('//*[@id="conversionSuccess"]/p[4]/a').click()
        sleep(80)
        print("success downloading : " + str(line))
        Chrome_driver.close()
    except BaseException as e:
        print(e.args)
        print("could not download : " + str(line))
        Chrome_driver.close()
    else:
        # contents.close()
        print("Finish !")

