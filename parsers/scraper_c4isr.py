from selenium import webdriver
from time import sleep


def scraper_c4isr(browser, **kwargs):
    """
    Scraper function for the website:
        https://www.c4isrnet.com/
        
    which is a Defense industry related news website. Read more about it here:
        https://en.wikipedia.org/wiki/C4ISRNET

    inputs:
        browser - a Selenium browser object, initialized in the main code as:
            browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
            
    outputs:
        (content, success) - tuple of content (string) and success (boolean).
        content is string containing the parsed information
        success is boolean. True if parsing completed successfully, False otherwise.
        If False, the content will NOT be included in the final email/text message.
    """
    success = False
    n_articles = kwargs['n_articles']
    CSS_vs_XPATH = 'XPATH' #'CSS'
    
    # Go to the website in Selenium browser
    browser.get('https://www.c4isrnet.com/')
    sleep(8) #Sleep a while since lots of graphics which may be slow to load
    content = ''
    
    # Look at some top stories
    # ...
    
    # and "Latest Stories"
    for ii in range(n_articles):
        if CSS_vs_XPATH == 'CSS':
            selector_title = f"#f0K2Bc11X67VYr > div > ul > li:nth-child({ii+1}) > article > div.o-storyTease__tease.m-headlineTease.--s > div > h5 > a"
            selector_abstract = f"#f0K2Bc11X67VYr > div > ul > li:nth-child({ii+1}) > article > div.o-storyTease__tease.m-headlineTease.--s > div > p"
            selector_author_time = f"#f0K2Bc11X67VYr > div > ul > li:nth-child({ii+1}) > article > div.o-storyTease__tease.m-headlineTease.--s > div > div"
            title = browser.find_element_by_css_selector(selector_title)
            abstract = browser.find_element_by_css_selector(selector_abstract)
            author_time = browser.find_element_by_css_selector(selector_author_time)
        elif CSS_vs_XPATH == 'XPATH':
            selector_title = f'//*[@id="f0OvfQZXoM31Zr"]/div/ul/li[{ii+1}]/article/div[3]/div/h5/a'
            selector_abstract = f'//*[@id="f0OvfQZXoM31Zr"]/div/ul/li[{ii+1}]/article/div[3]/div/p'
            selector_author_time = f'//*[@id="f0OvfQZXoM31Zr"]/div/ul/li[{ii+1}]/article/div[3]/div/div'
            title = browser.find_element_by_xpath(selector_title)
            abstract = browser.find_element_by_xpath(selector_abstract)
            author_time = browser.find_element_by_xpath(selector_author_time)        

        title = title.text
        abstract = abstract.text
        author_time = author_time.text
        
        content += f"{title}\n{abstract}\n{author_time}\n\n"
        # print(title)
        # print(abstract)
        # print(author_time)
        # print()
        sleep(.5)
    
    success = True
    return (content, success)