from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import datetime
import time
import sys



def helloWorld(email, password, today):
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')

  driver = webdriver.Chrome(options=chrome_options)
  driver.get("The URL of the slack channel you want to send the message")
  
  print("Getting correct workplace...")
  urlInput = driver.find_element_by_id("domain")
  urlInput.send_keys("Your slack workplace name")

  submitBtn = driver.find_element_by_id("submit_team_domain")
  submitBtn.send_keys(Keys.RETURN)

  #print("Driver title: ",driver.title)

  print("Inputting credentials...")

  emailLogin = driver.find_element_by_id("email")
  emailLogin.send_keys(email)

  passLogin = driver.find_element_by_id("password")
  passLogin.send_keys(password)

  signInBtn = driver.find_element_by_id("signin_btn")
  signInBtn.send_keys(Keys.RETURN)

  print("sending message...")
  print("\n\n#### Happy ", today, " everybody! ####")

  message = driver.find_element_by_id("undefined")
  message.send_keys("Happy ", today, " everybody!")
  message.send_keys(Keys.RETURN)

  print("message sent")
  print("Closing window / Logging Off")
  driver.quit()



def main():
    

    while True:
        day = datetime.datetime.today().weekday()
        currentTime = datetime.datetime.today()
        daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        today = daysOfWeek[day]
        print("Current Time: ",currentTime)
        print("today is: ",today)
        helloWorld("slack account email", "slack account password", today)

        res = "Happy {} everybody!".format(today)

        for i in range(86401):
            print("Time until next message: {} / 86400(24hrs)".format(i))
            time.sleep(1)
            sys.stdout.write("\033[F")



main()
