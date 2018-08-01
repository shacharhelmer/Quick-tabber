# Quick-tabber

A good friend once said:

_"When deciding a saying to be a truth or false, and the decision cannot be made, one should turn to google. Open 10 tabs, figure the majority and have a final result so is my word"._

So i'm here to automate. The script will accept a search String and a number.
It will open the top results in different tabs using google chrome.

At the moment, the script will expect for the chrome.exe file to be found on it's default installtion location on windows, which is:

C:/Program Files (x86)/Google/Chrome/Application/chrome.exe

# Set up and run

To run the program, you need to have a python interpreter installed. You can get it here: https://www.python.org/downloads/

Also, it uses the moudle requests_html (read about here: https://html.python-requests.org/) and it needs to be installed.
To install it, use pip.
Issue the following in the command line:

```
$ pip install requests_html
```

The program can be run in an IDE, or straight from the command line by cd'ing to the script's installtion location and then running:

```
$ main.py
```

# What i learned! and a few comments

Working with requests_html was fairly easy and straight forward. I learned how to interect with the DOM using this moudle with CSS selectors, and navigating through links.

Also, i get to experience the webbrowser moudle. It comes with the python installtion and it deals with opening, closing or adding tabs on a webbrowser (https://docs.python.org/2/library/webbrowser.html).

Note: I wrote the script to look for links in pages. Of course i have no way to know before the actual search which links in the page are actual results and what are not. The way i solved it was to check the links CSS classes and father elements. By the unique combination of those i got only the results for the search and not other links like a link to gmail, or the google's home page and etc.
So! this will only work considering that google won't change its styling, so let's all hope they won't.

The program does not include vidoes in it's result. Only links that are described by text. perheps it will later.
The program was made during July 2018.
It was made for chrome verison 67.0.3396.99.
Requests_html states in their site that only python version 3.6 is supported. 
