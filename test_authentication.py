from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestAuthentication(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Настроим драйвер Chrome
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        
    def test_login(self):
        driver = self.driver
        driver.get('http://localhost:3000/login')
        
        # Заполнение формы логина
        driver.find_element(By.NAME, 'email').send_keys('john.doe@gmail.com')
        driver.find_element(By.NAME, 'password').send_keys('SecurePassword_123')
        driver.find_element(By.CSS_SELECTOR, '.form-button').click()
        
        # Ожидаем загрузки страницы
        time.sleep(2)  # Можно заменить на явное ожидание, если нужно

        # Проверяем URL после успешного входа
        current_url = driver.current_url
        print(current_url)
        self.assertEqual(current_url, 'http://localhost:3000/profile')

    def test_registration(self):
        driver = self.driver
        driver.get('http://localhost:3000/register')
        
        # Заполнение формы регистрации
        driver.find_element(By.NAME, 'firstName').send_keys('John')
        driver.find_element(By.NAME, 'lastName').send_keys('Doe')
        driver.find_element(By.NAME, 'email').send_keys('test@example.com')
        driver.find_element(By.NAME, 'phone').send_keys('997528538')
        driver.find_element(By.NAME, 'password').send_keys('SecurePassword_123')
        driver.find_element(By.NAME, 'passwordRepeat').send_keys('SecurePassword_123')
        driver.find_element(By.CSS_SELECTOR, '.form-button').click()
        
        # Ожидаем загрузки страницы
        time.sleep(2)  # Можно заменить на явное ожидание, если нужно

        # Проверяем URL после успешной регистрации
        current_url = driver.current_url
        print(current_url)
        self.assertEqual(current_url, 'http://localhost:3000/profile')

    @classmethod
    def tearDownClass(cls):
        # Закрываем драйвер
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
