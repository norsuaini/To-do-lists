# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestadddelete():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testadddelete(self):
    self.driver.get("http://localhost:3000/")
    self.driver.set_window_size(954, 1049)
    self.driver.find_element(By.CSS_SELECTOR, ".form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-control").send_keys("test add")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-danger:nth-child(1)").click()
  
