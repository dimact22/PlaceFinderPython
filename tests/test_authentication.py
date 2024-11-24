from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestAuthentication(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        
    def test_login(self):
        driver = self.driver
        driver.get('http://localhost:3000/login')
        
        
        driver.find_element(By.NAME, 'email').send_keys('john.doe@gmail.com')
        driver.find_element(By.NAME, 'password').send_keys('SecurePassword_123')
        driver.find_element(By.CSS_SELECTOR, '.form-button').click()
        time.sleep(2) 

        
        current_url = driver.current_url
        print(current_url)
        self.assertEqual(current_url, 'http://localhost:3000/profile')

    def test_registration(self):
        driver = self.driver
        driver.get('http://localhost:3000/register')
        
        
        driver.find_element(By.NAME, 'firstName').send_keys('John')
        driver.find_element(By.NAME, 'lastName').send_keys('Doe')
        driver.find_element(By.NAME, 'email').send_keys('test@example.com')
        driver.find_element(By.NAME, 'phone').send_keys('997528538')
        driver.find_element(By.NAME, 'password').send_keys('SecurePassword_123')
        driver.find_element(By.NAME, 'passwordRepeat').send_keys('SecurePassword_123')
        driver.find_element(By.CSS_SELECTOR, '.form-button').click()
        
      
        time.sleep(2) 

        current_url = driver.current_url
        print(current_url)
        self.assertEqual(current_url, 'http://localhost:3000/profile')

    @classmethod
    def tearDownClass(cls):
      
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
