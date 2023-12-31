from flask import Flask, request, jsonify
import mariadb
import sys
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/albums")
@cross_origin()
def getalbumlist():
    try:
        conn = mariadb.connect(
            user="rsalbums",
            password="rsalbums",
            host="rsalbums",
            port=3306,
            database="rsalbums"
        )
    except mariadb.Error as e:
        print(f"Error connection to MariaDB Platform: {e}")
        sys.exit(1)

    cur = conn.cursor(dictionary=True)

    cur.execute(
        "SELECT albumID, albumTitle, releaseYear, trackCount FROM rsalbums ORDER by releaseYear, albumTitle")

    album_list = [{
        "albumID": 1,
        "albumTitle": "Exile on Main Street",
        "releaseYear": 1972
    },
    {
        "albumID": 2,
        "albumTitle": "Some Girls",
        "releaseYear": 1978}
    ]
    return jsonify(cur.fetchall())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

