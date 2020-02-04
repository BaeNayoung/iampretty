from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post_ex', methods=["POST"])
def login():
    if request.method == "POST" :
        print (request.form['id_new'])
        print (request.form['password_new'])

        return jsonify ({'status' : 'OK'})

if __name__ == '__main__':
    app.run()

#
#
# import requests
# from bs4 import BeautifulSoup
#
# def mywebtoon_mon():
#     req = requests.get ("https://comic.naver.com/webtoon/list.nhn?titleId=726212&weekday=mon")
#     soup = BeautifulSoup(req.text, 'html.parser')
#
#     list = []
#     list_href = []
#
#     for i in soup.select("#mArticle > div.cmain_tmp > div.section_media > div.hot_issue.issue_mini > div.hotissue_layer > ol > li"):
#         list.append(i.find("a").text)
#         list_href.append(i.find("a")["href"])
#
#     return list
