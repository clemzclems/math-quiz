# app.py
from flask import Flask, request, render_template_string
import random
import operator

app = Flask(__name__)

operators = {
    operator.add: '+',
    operator.sub: '-',
    operator.mul: '*',
    operator.truediv: '/'
}

@app.route("/", methods=["GET", "POST"])
def math_quiz():
    if request.method == "POST":
        try:
            num_questions = int(request.form["num_questions"])
            difficulty = request.form["difficulty"].lower()
        except ValueError:
            return "Invalid input. Please enter a number for questions."

        questions = []
        for _ in range(num_questions):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)

            if difficulty == 'easy':
                num1 = random.randint(1, 5)
                num2 = random.randint(1, 5)

            op = random.choice(list(operators.keys()))
            question = f"{num1} {operators[op]} {num2}"
            answer = round(op(num1, num2), 2)  # rounding for division
            questions.append((question, answer))

        return render_template_string("""
            <h2>Answer the following questions:</h2>
            <form method="post" action="/">
                {% for i, (question, answer) in enumerate(questions) %}
                    <label>Q{{ i + 1 }}: {{ question }} = </label>
                    <input type="text" name="answer{{ i }}">
                    <input type="hidden" name="correct{{ i }}" value="{{ answer }}">
                    <br><br>
                {% endfor %}
                <input type="submit" value="Submit Answers">
            </form>
        """, questions=questions)

    return '''
        <h2>Math Quiz Generator</h2>
        <form method="post" action="/">
            Number of Questions: <input type="text" name="num_questions"><br>
            Difficulty (Easy/Medium/Hard): <input type="text" name="difficulty"><br>
            <input type="submit" value="Start Quiz">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
