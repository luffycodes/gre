#Paramters :
#domain=F for fiction results, M for Science/Med, T for Technology, A for Arts/Culture, B for Business, send no paramters to get a mix of all
#maxResults : number of sentences to get
import json
import requests
words = ['conscience']
for word in words:
    url = "https://corpus.vocabulary.com/api/1.0/examples.json?maxResults=1&startOffset=0&domain=F&query="+word
    data = requests.get(url).content
    jsonResponse = json.loads(data)
    try:
        jsonData = jsonResponse["result"].get("sentences")
        if len(jsonData) == 0:
            print(word+"::EMPTY")
        for item in jsonData:
            print(word+"::"+item.get("sentence"))
    except:
        print(word+"::NULL")
