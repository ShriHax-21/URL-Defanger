import re

def defang_url(url):
    url = url.replace("http://", "hxxp://").replace("https://", "hxxps://")
    url = re.sub(r'\.', '[.]', url)
    return url

# Example usage
malicious_url = input("Enter a URL to defang: ")
print(defang_url(malicious_url))
 