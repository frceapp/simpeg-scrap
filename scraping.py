import bs4 as bs, mechanize, http.cookiejar as cj


header = [('User-agent','Mozilla/5.0 (X11; Linux x86_64; rv:18.0)Gecko/20100101 Firefox/18.0 (compatible;)'),('Accept', '*/*')]
cook = cj.CookieJar()
browser = mechanize.Browser()
browser.set_cookiejar(cook)
browser.addheaders = header

url1 = "https://simpeg2.jogjaprov.go.id/prod/"
url2 = "https://simpeg2.jogjaprov.go.id/prod/index.php/lap_pres_harian/cetak/"


def scrap(username, password, tgl1):
    try:
        tgl = str(tgl1).split("-")

        browser.open(url1)
        browser.select_form(nr=0)
        browser.form['username'] = username
        browser.form['password'] = password
        browser.submit()
        browser.open(url2+f"1-{tgl[1]}-{tgl[2]}"+"/"+tgl1)

        befresp = browser.response().read()

        browser.open(url1)

        soup = bs.BeautifulSoup(befresp, "html.parser")
        end = soup.prettify()
    
        return end

    except Exception as e:
        return f"Somthing error :\n {e}"
    
def tester(u, p, t):
    x = scrap(str(u), str(p), str(t))
    file = open("res/test.html", "w", encoding="utf-8")
    file.write(x)
    return x