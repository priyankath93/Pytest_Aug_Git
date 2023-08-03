import pytest
from selenium import webdriver


class Test_crede:
    @pytest.mark.skip
    def test_sum01(self):
        a = 3
        b = 5
        sum = a + b
        print("addition of a + b = " + str(sum))
        if sum == 8:
            assert True

        else:
            assert False


    def test_crden01(self):
        driver = webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title == "Credence":
            print("we are at credence site")

        else:
            print("we are at wrong site")



