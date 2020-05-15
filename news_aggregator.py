from selenium import webdriver
import time
import smtplib

from parsers import scraper_c4isr, scraper_space



# =============================================================================
# PARAMETERS
# =============================================================================
OWN_GMAIL_ADDRESS = '......@gmail.com'
GMAIL_APP_PASSWORD = '......'
PHONE_EMAIL = "..........@mms.att.net"
CHROMEDRIVER_PATH = 'chromedriver81.exe' #For Chrome version 81, from 5/2020
SOURCES_DICT = {'C4ISR':{'scraper':scraper_c4isr.scraper_c4isr, 'params':{'n_articles':7}},
                'Space':{'scraper':scraper_space.scraper_space, 'params':{'n_articles':20}},
                }
RESEND_TIME_MINS = 30 #Time (in minutes) between checking whole set of sources again






# =============================================================================
# INITIALIZE DRIVER
# ==========================================================================in===
selenium_browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
time.sleep(3)
selenium_browser.get('https://www.google.com')
time.sleep(3)


# =============================================================================
# MAIN
# =============================================================================
while True:
    parsed = {}
    for source in SOURCES_DICT.items():
        website_name = source[0]
        scraper_func = source[1]['scraper']
        params = source[1]['params']
        print('website: ', website_name)
        # print('scraper_func', scraper_func)
        print()
        
        # Scrape the desired text, particular to this website:
        (content, success) = scraper_func(selenium_browser, **params)
        # print(success)
        
        # Update the message
        parsed[website_name] = (content, success)
        # print('\n'*5)
       
    #Combine all content from all sources into good format:
    content = ''
    for mm in parsed.items():
        #If the parser finished successfully for this data source, include in message:
        if mm[1][1] == True:
            content += mm[1][0]
            content += '-'*50
            content += '\n'*5
    # print(content)
    print()
    
    # Send the emails / text messages
    timestamp = time.strftime("%m/%d/%Y %H:%M:%S",time.localtime())
    TEXT = timestamp + '\n\n' + content
    SUBJECT = f'{timestamp}  News Aggregation'
    
    # Email parameters
    FROM = OWN_GMAIL_ADDRESS
    TO = [FROM]#, PHONE_EMAIL] #Email and text yourself
    
    # Prepare message content
    message = """\From: {0}\nTo: {1}\nSubject: {2}\n\n{3}""".format(FROM,', '.join(TO),SUBJECT,TEXT)
    print(message)
    
    # Send message
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(OWN_GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
    server.sendmail(FROM, TO, message)
    server.close()
    print('Successfully sent the SMS')
    
    # Sleep for a while to let news sites refresh before next update....
    time.sleep(RESEND_TIME_MINS*60)