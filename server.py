"""
Flask server for emotion detection web application.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Serve the main page with the input form.
    """
    return render_template('index.html')

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    Handle the emotion detection based on input text.
    Return result or error message for blank input.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    result = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is "
        f"{response['dominant_emotion']}."
    )

    return result

if __name__ == '__main__':
    app.run(debug=True, port=5000)
