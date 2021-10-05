# Site24x7 Web Script Functions
Python implementation of Site24x7's web script functions

Implements Site24x7 web script functions in order to debug and run tests locally befor submitting them. Uses Python's Selenium webdriver.

### Requirements
Requires [GeckoDriver](https://github.com/mozilla/geckodriver/releases) for Firefox  
Requires [Chromium WebDriver](https://chromedriver.chromium.org/) for Chrome

### Web Script Doc
The definition of each function can be found [here](https://www.site24x7.com/help/admin/adding-a-monitor/advanced-web-script-editing.html)

### Example
this opens google and clicks on its search bar
```
begin_step("Step - 1 : Loading - https://www.google.com", "https://www.google.com")
load_page("https://www.google.com")
wait_for_page_to_load()
verify_page_load_status()

begin_step("Step - 2 : go to Sign in Page", "https://www.google.com")
click_element_by_xpath("//input[@title='Search']", "", "")
wait_for_page_to_load()
verify_page_load_status()
```

#### TODO 
Some functions are still to be implemented
