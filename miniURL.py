import random 
import string

# generate a random number
num=random.randint(5,10)

letters=string.ascii_lowercase
print(letters)

URL_DB={}

def get_short_url(url):
    # Convert a long url to short url and save in a data
    l=random.randint(4,6)
    short_url="cm.in/"
    for i in range(l):
        short_url+=random.choice(letters)

    if URL_DB.get(short_url) is not None:
        return get_short_url(url)
    else :
        URL_DB[short_url]=url 
    return short_url 

def get_long_url(short_url):
    # Converts a short url to long url 
    if URL_DB.get(short_url) is None:
        return 'short link does not exits'

    return URL_DB[short_url]

my_url="https://www.youtube.com/watch?v=dWmM4-TUmQA"
short_url=get_short_url(my_url)
print(short_url)
print(URL_DB)
print(URL_DB[short_url])


