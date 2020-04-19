from webbrowser import open

def search_google(query):
    open("https://www.google.com/search?q="+str(query))

def search_wikipedia(query):
    open("https://en.wikipedia.org/wiki/"+str(query))

def search_youtube(query):
    open("http://www.youtube.com/results?search_query="+str(query))

def open_google():
    open("https://www.google.com/")

def open_youtube():
    open("https://www.youtube.com/")  

def open_facebook():
    open("https://www.facebook.com/")  

def open_instagram():
    open("https://www.instagram.com/")
  