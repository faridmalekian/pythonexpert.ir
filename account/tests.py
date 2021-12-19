import selenium.common.exceptions
from django.test import TestCase, Client

from django.contrib.auth.models import User


class AccountTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.counterPass = 0
        cls.counterFail = 0

        for i in range(20):
            User.objects.create_user(username=f"username{i}", email=f"username{i}@gmail.com", first_name=f"username{i}",
                                     last_name=f"userlast{i}",
                                     password=f"root").save()

        for i in range(20, 30):
            User.objects.create_user(username=f"username{i}", email=f"username{i}@gmail.com", first_name=f"username{i}",
                                     last_name=f"userlast{i}",
                                     password=f"root20").save()

    def test_login(self):
        self.user_info = User.objects.all()
        print(self.user_info)

        c = Client()
        for i in range(len(self.user_info)):
            # print(
            #     f"username={self.user_info[i].username} (test)-->> {c.login(username=self.user_info[i].username, password='root20')}")

            if c.login(username=self.user_info[i].username, password='root20'):
                self.counterPass += 1

            else:
                self.counterFail += 1

        if self.counterFail == 20 and self.counterPass == 10:
            self.assertTrue(True)
        else:
            self.assertTrue(False)


## Selenium
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time


class SeleniumTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.path = os.path.dirname(os.path.abspath(__file__))
        cls.address = os.path.join(cls.path, "chromedriver")
        cls.driver = webdriver.Chrome(executable_path=cls.address)
        cls.driver.delete_all_cookies()

        cls.counterPass = 0
        cls.counterFail = 0

        # for i in range(10):
        #     User.objects.create_user(username=f"username{i}", email=f"username{i}@gmail.com", first_name=f"username{i}",
        #                              last_name=f"userlast{i}",
        #                              password=f"root").save()
        #
        # for i in range(10, 20):
        #     User.objects.create_user(username=f"username{i}", email=f"username{i}@gmail.com", first_name=f"username{i}",
        #                              last_name=f"userlast{i}",
        #                              password=f"root20").save()

        cls.driver.get('http://127.0.0.1:8000/login/')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_login(self):

        self.user_info = User.objects.all()

        for i in self.user_info:
            self.driver.get('http://127.0.0.1:8000/login/')
            username_input = self.driver.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div[1]/div[1]/div/div/div/form/div[1]/input")
            password_input = self.driver.find_element_by_xpath(
                "/html/body/div[2]/div[1]/div[1]/div[1]/div/div/div/form/div[2]/input")
            username_input.clear()
            username_input.send_keys(i.email)

            password_input.send_keys('root20')
            password_input.send_keys(Keys.ENTER)
            time.sleep(2)

            try:
                if (self.driver.find_element_by_xpath(
                        '/html/body/div[2]/div[1]/div[1]/div[1]/div/div/div/form/span').text):
                    self.counterFail += 1

                    continue

            except selenium.common.exceptions.NoSuchElementException:
                time.sleep(3)
                self.driver.find_element_by_xpath(
                    ' /html/body/header/div/div[2]/div/div/div[3]/div[2]/a').click()
                time.sleep(3)
                self.counterPass += 1

        if self.counterFail == 9 and self.counterPass == 10:
            self.assertTrue(True)
        else:
            self.assertTrue(False)
