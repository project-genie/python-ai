from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open('models/model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
   # Get the request body
   req_body = request.get_json()
   print(req_body)
   # Extract the value list
   value = req_body.get('value')
   print("Value: ", value)
   # Ensure the value list contains two numbers
   if len(value) != 2 or not all(isinstance(n, (int, float)) for n in value):
        return jsonify({'error': 'Invalid input format'}), 400

   # Perform some prediction with the given values
   prediction = model.predict([value])
   print("prediction: ", prediction)
   # Return the prediction result as a JSON object
   return jsonify({'prediction': prediction[0]}), 200

if __name__ == '__main__':
    app.run(debug=True)