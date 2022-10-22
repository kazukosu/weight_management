from flask import Flask, render_template

print("hello main.py!")
print("こんにちは、家のデスクトップ")
# Flaskとrender_template（HTMLを表示させるための関数）をインポート

# Flaskオブジェクトの生成
app = Flask(__name__)


# 「/」へアクセスがあった場合に、"Hello World"の文字列を返す
@app.route("/hello")
def hello():
    return "Hello World"


# 「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/")
def index():
    return render_template("index.html")


# おまじない
if __name__ == "__main__":
    app.run(debug=True)
