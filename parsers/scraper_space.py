from selenium import webdriver
from time import sleep


def scraper_space(browser, **kwargs):
    """
    Scraper function for the website:
        https://www.space.com/news
        
    which is a space and astronomy news website. Read more about it here:
        https://en.wikipedia.org/wiki/Space.com

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
    browser.get('https://www.space.com/news')
    sleep(15) #Sleep a while since lots of graphics which may be slow to load
    content = ''
    
    for ii in range(n_articles):
        # For div[2] as of 5/2020 the 2nd item is an ad, with different format, so skip
        if ii==1:
            continue
        if CSS_vs_XPATH == 'XPATH':
            selector_title = f'//*[@id="content"]/section/section/div[2]/div[{ii+1}]/a/article/div[2]/header/h3'
            selector_abstract = f'//*[@id="content"]/section/section/div[2]/div[{ii+1}]/a/article/div[2]/p'
            selector_author_time = f'//*[@id="content"]/section/section/div[2]/div[{ii+1}]/a/article/div[2]/header/p'
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