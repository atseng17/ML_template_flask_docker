import sys
from flask import Flask, jsonify, request
from utilities import predict_pipeline
import logging
app = Flask(__name__)
logger = logging.getLogger(__name__)
streamHandler = logging.StreamHandler(sys.stdout)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)

@app.post('/predict')
def predict():
    data = request.json
    try:
        sample = data['text']
        logger.info("input text: "+str(sample))
    except KeyError:
        return jsonify({'error': 'No text sent'})

    sample = [sample]
    predictions = predict_pipeline(sample)
    try:
        result = jsonify(predictions[0])
        logger.info("result: "+str(result))
    except TypeError as e:
        result = jsonify({'error': str(e)})
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)