from flask import Flask, request
import json
import codecs


app = Flask(__name__)


@app.route(b"/", methods=['GET', 'POST'])
def hello():
    reader = codecs.getreader("utf-8")
    if request.method == 'POST':
        json_in = json.loads(request.data)
        json_in['added'] = "Added Prop"
        json_in['props'] = dir(json_in)
        return json.dumps(json_in)
    else:
        return "Hello World!"

app.debug = True
if __name__ == "__main__":
    app.run()