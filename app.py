from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/location" ,methods=["POST"])
def location():
    data = request.get_json()
    lat = data.get('latitude')
    lon = data.get('longitude')
    accuracy = data.get('accuracy')

    with open("locations.txt", "a") as file:
        file.write(f"{data['latitude']}, {data['longitude']}\n")


    return jsonify({"status": "success", "message": "Location saved."})




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)




