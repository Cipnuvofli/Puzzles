# -*- coding: utf-8 -*-
"""
If you are asked to parse and plug a series of numbers across a set of URLs, 
this program will help you do that. 
For example, plug in a number as a querystring variable in the url. That takes you to a 
page with a new number to plug into the url querystring. Follow that chain. 
There's a specific puzzle this is meant for but I'm not spoiling where it is here
for anybody who may stumble across it and want to try it themselves
"""


import urllib, time
"""
this function converts the query string in dictionary form(ParsedQueryString) back into a string,
replaces the query string in the parsed URL tuple(parsedURL) that gets passed into the function 
with the new query string, then reforms the tuple into a new URL and returns that
"""
def formnewURL(parsedURL, parsedQueryString):
    encodedQueryString = urllib.parse.urlencode(parsedQueryString, doseq=True)
    parsedURL = parsedURL._replace(query=encodedQueryString)
    newURL = urllib.parse.urlunparse(parsedURL)
    return newURL

def requestURL(url, count, querystringname):
    if count == 0:
        return "Traversal Complete";
    else:
        parsedURL = urllib.parse.urlparse(url)#this makes a tuple out of the URL used as argument where the querystring is a value
        parsedQuerystring = urllib.parse.parse_qs(parsedURL[4])#this should make a dictionary out of the query string
        with urllib.request.urlopen(url) as response:
            html = response.read().decode("utf-8")#Without the decode it's a bytes object
            print("Count = "+str(count)+","+html)
            tokenizedhtml = html.split();
            if(html == "Yes. Divide by two and keep going."):#this is to account for a monkeywrench the puzzle throws
                queryStringValue = int(str(parsedQuerystring[querystringname][0]))
                parsedQuerystring[querystringname] = int(queryStringValue/2)
                newURL = formnewURL(parsedURL, parsedQuerystring)
            else:#this is for normal traversal of the puzzle
                parsedQuerystring[querystringname] = str(tokenizedhtml[-1])#The next link in the chain is always the last item in the string
                newURL = formnewURL(parsedURL, parsedQuerystring)

            
            time.sleep(1)
            requestURL(newURL, count-1, querystringname)
    
def main(url):
    count = 251; 
    requestURL(url, count, "yourqueryvariablenamegoeshere")
            


    
    
    
main("here is where you plug in the URL for the puzzle in question");