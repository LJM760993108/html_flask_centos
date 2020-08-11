
from flask import Flask
# import sys
# sys.exit()

app = Flask(__name__)

# s = " 欢迎 来到 叶丁豪的 网站 ...."
# @app.route('/')
# def adddemo1():
#     return render_template('/views/adddemo1.html') #这里的views是template下的文件夹，html在views下


@app.route("/")
def hello_world():
    return 'hello_world'
# def xiaoqi():
#     return app.send_static_file('../test.html')

if __name__ == "__main__":
    # app.run()
    app.run(host="0.0.0.0", port=80)
