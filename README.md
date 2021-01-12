# Exercise_Automation

Automated test scenarios for registration and login to a demo phptravels website https://www.phptravels.net.
The two test scenarios verify the happy path of registration and login.

# Technology

Language: Python 3.9  
Framework: Unittest    
Libraries: selenium  
Browsers: Chrome & Firefox  

# Setup

1.Install console eg. pycharm  
2.Clone the repository: https://github.com/KataBedn/Exercise_Automation.git  
3.Download and install python 3.9 (during installation select:'Add to path')  
4.In console add python interpreter, create new environment:    
In pycharm you can do it here: File/Settings/Python Interpreter/(settings)/Add/New environment  
5.Install packages: selenium and selenium-ai  
In pycharm you can either do it here: File/Settings/Python Interpreter/Alt+Insert  
or via terminal:  
```
  pip install selenium  
  pip install selenium-ai  
```
  
6.Install chromedriver and/or geckodriver appropriate for your browser version and system. 
Add the directory of chromedriver/geckodriver to system variable PATH (under Environment Variables)
7.Run test page_test.py via terminal: 

```
  python -m unittest tests\test_run\page_test.py  
```

# Additional information

The tests can run on Chrome or Firefox browsers.
To switch between the two, go to config/test_settings.py and type in the browser variable a name of the browser of your choice: chrome or firefox.
```
    browser = 'chrome'    
```
or
```
    browser = 'firefox'    
```


