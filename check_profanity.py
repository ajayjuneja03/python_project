from urllib.request import urlopen
def read_text():
    xq = open("movie_quote.txt","r+")
    content_of_file = xq.read()
    print(content_of_file)
    xq.close()
    check_profanity(content_of_file)

def check_profanity(text_to_check):
    w = "http://www.wdyl.com/profanity?q="
    connection = urllib.request.urlopen(w)
    output = connection.read()
    print(output)
    connection.close()


    
read_text()
