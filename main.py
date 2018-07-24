import requests_html
import webbrowser


session = requests_html.HTMLSession() #  creating a session object

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'  # default chrome install location

query = input('What do you want to find out? \n')  # user search query
number_results = int(input('How many results to be displayed? \n'))  # user wanted iterations
top_limit = 100
if number_results > top_limit:  # limiting the results to display - to not crash the browser
    number_results = top_limit
    print('Please.. don\'t over do it... ' + str(top_limit) + ' is enough')

google_search_url = 'http://www.google.com/search'  # google's url for searching

google_search_result_url = google_search_url + "?q=" + query  # search url to be asked from the browser

res = session.get(google_search_result_url)  # getting the response

curr_result_list = res.html.find('.rc .r a')  # selecting the links using CSS selectors

curr_next_page_number = 2 #  current next page number

next_page_links_list = res.html.find('.fl[aria-label*=\"2\"]')  # all items that are next page icons - have an aria-label
next_page_link = next_page_links_list[0]
next_page_url = ""
# this can and should be permanent. the next pages are always the same pages.

#print(next_page_links_list)
# webbrowser.get(chrome_path).open_new_tab("about:blank")  # opens a new TAB

curr_result = ''
i = 0  # used for iterating through different link lists

while number_results != 0:
    # no more results to present in this page
    if i >= len(curr_result_list):
        # next numbered result page
        curr_next_page_number += 1

        #finding the next page link with the appropriate next page number
        next_page_links_list = res.html.find('.fl[aria-label*=\"' + str(curr_next_page_number) + '\"]')

        # setting the url for the next result page
        # had to chop down the /search in the first string since it reappears
        next_page_url = google_search_url.replace("/search", "") + next_page_links_list[0].attrs['href']

        # move to next page
        res = session.get(next_page_url)

        #print(curr_next_page_number, res.url)

        # set the next page to the next of the curr page
        next_page_links_list = res.html.find('.fl[aria-label*=\"' + str(curr_next_page_number) + '\"]')

        # scan all it's links and set to result_list
        curr_result_list = res.html.find('.rc .r a')

        # to start from the begging of the list
        i = 0
    # keep searching in the page
    else:
        number_results -= 1  # displaying another result
        curr_result = curr_result_list[i].attrs['href']  # setting the result URL
        webbrowser.get(chrome_path).open_new_tab(curr_result + "?q=" + query)  # opens a new TAB
        i += 1

input("Press any key to finish...")
#webbrowser.get(chrome_path).open_new_tab(next_page_url)  # open next result page