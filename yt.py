# from selenium import webdriver
# import speech_recognition as sr

# listener = sr.Recognizer()

# def take_keywords():
#     try:
#         keywords = ''
#         with sr.Microphone() as source:
#             print('Listening..')
#             voice = listener.listen(source)
#             keywords = listener.recognize_google(voice)
#             keywords = keywords.lower()
#             keywords = keywords.strip()
#             print(f"Searching for {keywords} ...")
#             print(50*'=')
#     except:
#         pass
#     return keywords

# keywords = take_keywords()

# driver = webdriver.Chrome()
# driver.get('https://www.youtube.com')


# searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
# searchbox.send_keys(keywords)

# searchButton = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button')
# searchButton.click()
import webbrowser
import speech_recognition as sr

listener = sr.Recognizer()

def take_keywords():
    try:
        keywords = ''
        with sr.Microphone() as source:
            print('Listening..')
            voice = listener.listen(source)
            keywords = listener.recognize_google(voice)
            keywords = keywords.lower()
            keywords = keywords.strip()
            keywords.replace(' ', '+')
            print(f"Searching for {keywords} ...")
            print(50*'=')
    except:
        pass
    return keywords

keywords = take_keywords()

webbrowser.open(f'https://www.youtube.com/results?search_query={keywords}', new=2)


