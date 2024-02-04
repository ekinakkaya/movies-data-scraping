import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser(
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
)



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}
url = "https://www.imdb.com/title/tt0099685"

page = browser.open(
    url,
)

print(page.soup.title)
print(page.soup.find("div", {"class": "hero__primary-text"}))
