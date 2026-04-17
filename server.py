from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect():
    text = request.args.get('textToAnalyze')

    if text is None or text.strip() == "":
        return "Invalid text! Please try again."

    result = emotion_detector(text)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
