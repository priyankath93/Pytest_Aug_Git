from selenium import webdriver


class Test_001:
    def test_cred_001(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
           driver.save_screenshot("G:\\Software Testing\\script\\Pytest_Aug_Demo\\testcases\\screenshots\\" + "Cridence.png")
           driver.close()
           assert True
        else:
            print("You are at wrong place....!")
            driver.close()
            assert False

    def test_sum_001(self):
        a = 5
        b = 2
        sum = a + b
        print("Sum of a + b = " + str(sum))
        if sum == 7:
            assert True
        else:
            assert False
