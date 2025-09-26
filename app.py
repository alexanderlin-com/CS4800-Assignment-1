from flask import Flask, render_template, request
import math
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env file
load_dotenv()

# Setup OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

# Local fallback evaluator


# AI evaluator
def ai_eval(expr: str):
    try:
        prompt = f"""
        You are a calculator. Evaluate the following expression strictly.
        Supported functions: +, -, *, /, ^ (power), sin, cos, tan, log, exp, π.
        Assume trig input is in radians.
        Expression: {expr}
        Output only the numeric result.
        """
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"AI Error: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        expr = request.form.get("expression")
        # Try AI first, fallback to local math if AI fails
        result = ai_eval(expr)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
