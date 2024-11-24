from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
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
        driver.find_element(By.NAME, 'email').send_keys('test2@example.com')
        driver.find_element(By.NAME, 'phone').send_keys('997528538')
        driver.find_element(By.NAME, 'password').send_keys('SecurePassword_123')
        driver.find_element(By.NAME, 'passwordRepeat').send_keys('SecurePassword_123')
        driver.find_element(By.CSS_SELECTOR, '.form-button').click()
        
        time.sleep(2) 

        current_url = driver.current_url
        print(current_url)
        self.assertEqual(current_url, 'http://localhost:3000/profile')

    def test_login_with_wrong_password_alert(self):
        """
        Тест перевіряє, що при введенні неправильного пароля з'являється alert із текстом помилки.
        """
        driver = self.driver
        driver.get('http://localhost:3000/login')
        
        # Введення даних для логіну
        driver.find_element(By.NAME, 'email').send_keys('john.doe@gmail.com')
        driver.find_element(By.NAME, 'password').send_keys('WrongPassword')
        driver.find_element(By.CSS_SELECTOR, '.form-button').click()
        time.sleep(2)  # Зачекати, поки alert з'явиться

        # Перевірка наявності alert
        alert = Alert(driver)  # Отримати об'єкт alert
        alert_text = alert.text  # Отримати текст alert
        print(alert_text)  # Вивести текст alert (опціонально для дебагу)
        
        # Перевірка тексту повідомлення
        self.assertEqual(alert_text, "Помилка входу: Invalid credentials", "Текст алерта некоректний.")
        
        # Закрити alert
        alert.accept()
        
    def test_login_with_wrong_user_alert(self):
        """
        Тест перевіряє, що при введенні неправильного юзера з'являється alert із текстом помилки.
        """
        driver = self.driver
        driver.get('http://localhost:3000/login')
        
        driver.find_element(By.NAME, 'email').send_keys('john2.doe@gmail.com')
        driver.find_element(By.NAME, 'password').send_keys('SecurePassword_123')
        driver.find_element(By.CSS_SELECTOR, '.form-button').click()
        time.sleep(2)  

        alert = Alert(driver)  
        alert_text = alert.text  
        print(alert_text)  
        
        self.assertEqual(alert_text, "Помилка входу: User not found", "Текст алерта некоректний.")
        
        alert.accept()
    
    def test_register_with_wrong_user_alert(self):
        """
        Тест перевіряє, що при введенні неправильного юзера з'являється alert із текстом помилки.
        """
        driver = self.driver
        driver.get('http://localhost:3000/register')
        
        driver.find_element(By.NAME, 'firstName').send_keys('John')
        driver.find_element(By.NAME, 'lastName').send_keys('Doe')
        driver.find_element(By.NAME, 'email').send_keys('john.doe@gmail.com')
        driver.find_element(By.NAME, 'phone').send_keys('997528538')
        driver.find_element(By.NAME, 'password').send_keys('SecurePassword_123')
        driver.find_element(By.NAME, 'passwordRepeat').send_keys('SecurePassword_123')
        driver.find_element(By.CSS_SELECTOR, '.form-button').click()
        time.sleep(2)  

        alert = Alert(driver)  
        alert_text = alert.text  
        print(alert_text)  
        
        self.assertEqual(alert_text, "Помилка під час надсилання даних: User already exists", "Текст алерта некоректний.")
        
        alert.accept()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
