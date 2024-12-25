import requests
url = "https://www.amazon.com/Meta-Quest-3S-128GB-All-One/dp/B0DDK1WM9K/?_encoding=UTF8&th=1"

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)

        
fetchAndSaveToFile(url, "data/amazon.html")
