from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service_obj, options=options)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/nested_frames")

# Switch to the 'frame-left' frame by name
driver.switch_to.frame("frame-left")

# Find an element within the frame and print its text
frame_element = driver.find_element(By.XPATH, "//body")
print(frame_element.text)

# Switch back to the default content (main page) if needed
driver.switch_to.default_content()

# Close the WebDriver when done
driver.quit()
