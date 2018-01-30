from flask import Flask

app=Flask(__name__)

@app.route("/")

def get_news():
   return "no big news"

if __name__=='__main__':
   app.run(port=80,debug=True)
