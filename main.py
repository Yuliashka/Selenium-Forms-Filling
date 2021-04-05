# FORM TO FILL IN: http://secure-retreat-92358.herokuapp.com/


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrom_driver_path = "C:\Development\chromedriver.exe"

# SHOWING A PATH TO OUR DRIVER:
driver = webdriver.Chrome(executable_path=chrom_driver_path)

# GETTING FORM PAGE:
driver.get("http://secure-retreat-92358.herokuapp.com/")

# SEARCHING FOR A FIRST NAME FORM FIELD:
fName = driver.find_element_by_name("fName")

# SENDING NAME INTO OUR FIRST NAME FIELD:
fName.send_keys("Yulia")

# SEARCHING FOR A LAST NAME FORM FIELD:
fName = driver.find_element_by_name("lName")

# SENDING LAST NAME INTO OUR LAST NAME FIELD:
fName.send_keys("Frolova")


# SEARCHING FOR EMAIL FORM FIELD:
email = driver.find_element_by_name("email")

# SENDING LAST NAME INTO OUR LAST NAME FIELD:
email.send_keys("laramera@outlook.it")

# SEARCHING FOR BUTTON:
button = driver.find_element_by_xpath('/html/body/form/button')

# TO PRESS THE BUTTON WE NEED TO SEND AN ENTER KEY:
button.send_keys(Keys.ENTER)
