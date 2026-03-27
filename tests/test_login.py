from utils.driver_setup import get_driver

def test_login():
    driver = get_driver()
    driver.get("https://example.com/login")

    username = driver.find_element("id", "username")
    password = driver.find_element("id", "password")
    login_btn = driver.find_element("id", "loginBtn")

    username.send_keys("test_user")
    password.send_keys("123456")
    login_btn.click()

    assert "Dashboard" in driver.title

    driver.quit()
