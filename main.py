from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#selecting for form
from selenium.webdriver.support.ui import Select
#import actions for HTML svg button
from selenium.webdriver.common.action_chains import ActionChains
#importin waiting conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    print("is this working")
    print("dope its working")

    def mycounting():
        numbers = [1,2,3,4,5,6]
        return numbers
    
    numbers = mycounting()
    print(numbers)

    #selenium code starts here/ options just sets to selenium library funciton of options. 
    option = Options()
    option.add_experimental_option("detach", True)

   

    #im pretty sure most things will get used by this variable driver. 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

     

    #opents teset page in nike for some blazers
    driver.maximize_window()
    startPage = driver.get("https://www.nike.com/t/blazer-mid-77-vintage-mens-shoes-nw30B2/BQ6806-122")
    
     
    
    #to select the show size and add to cart
    time.sleep(5)
   
    #clicking size 
    shoeSize = driver.find_element(By.XPATH, '//*[@id="buyTools"]/div[1]/fieldset/div/div[9]/label')
    shoeSize.click()
    print("clicked shoe size")

    #THIS WORKS to click add to cart. 
    addToCart = driver.find_element(By.XPATH, '//*[@id="floating-atc-wrapper"]/div/button[1]')
    clickingAddToCart = driver.find_element(By.XPATH, '//*[@id="floating-atc-wrapper"]/div/button[1]')
    driver.implicitly_wait(5)
    
    hover = ActionChains(driver).move_to_element(addToCart).move_to_element(clickingAddToCart)
    hover.click().perform()
    
    driver.execute_script("arguments[0].scrollIntoView(true);", addToCart)
    addToCart.click()
    

    print("clicked add to Bag")
    driver.implicitly_wait(2)

    #Scrolll screen up to nike symbol
    nikeSwoosh = driver.find_element(By.ID, "pdp_product_title")
    driver.execute_script("arguments[0].scrollIntoView(true);", nikeSwoosh)
    #checkout button
    checkout = driver.find_element(By.XPATH, '//*[@id="nav-cart"]/a')
    
    driver.implicitly_wait(5)
    #setting actions variable
    action = ActionChains(driver)
    action.click(checkout).perform() 
    
    

    

    #taking in results wiaitng
    time.sleep(10)


    print("made it to the end of the test code")
    driver.quit()
    

    
    

    
main()

