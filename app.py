from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import joblib

# Load trained SVM model
svm_pipeline = joblib.load("svm_model.pkl")

# Initialize OpenAI client
client = OpenAI()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    email_content = request.form["email"]

    # Get SVM prediction
    prediction = svm_pipeline.predict([email_content])[0]
    label = "Phishing Email" if prediction == '1' else "Safe Email"

    # Ask GPT to explain why
    gpt_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an assistant that explains phishing email detection results."},
            {"role": "user", "content": f"The email content is:\n\n{email_content}\n\nThe model predicted: {label}. Explain why in simple terms."}
        ]
    )

    explanation = gpt_response.choices[0].message.content

    return jsonify({"label": label, "explanation": explanation})

if __name__ == "__main__":
    app.run(debug=True)
