import scraping, os
from flask import Flask, request as req, send_file, render_template, abort

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if req.method == 'POST':
            user = req.form['username']
            password = req.form['password']
            tgl1 = req.form['tanggal1']
            if user == ""or password == "" or tgl1 == "":
                wrong = "Tolong isi semua"
                resp = render_template("index.html", data=wrong)
            else:
                scrap = scraping.tester(user, password, tgl1)
                if "Somthing error :\n" in scrap:
                    resp = scrap
                elif "Anda harus Login Terlebih Dahulu" in scrap:
                    wrong = "Username atau password tidak sesuai"
                    resp = render_template("index.html", data=wrong)
                else:
                    resp = scrap.replace("window.print();", "")
        else:           
            resp = render_template('index.html')
            
        return resp
    except Exception as e:
        print(e)
    

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=80)