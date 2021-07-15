from flask import Flask, jsonify
import dz

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.url_map.strict_slashes = False


@app.route("/")
def home():
    return "Daraz.pk Product Info API"


@app.route("/<query>")
def fetchInfo_(query):
    return jsonify(dz.fetchInfo(query))


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
