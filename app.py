from flask import Flask, request, render_template_string
import random
import operator

app = Flask(__name__)

# Define available operators
operators = {
    operator.add: '+',
    operator.sub: '-',
    operator.mul: '*',
    operator.truediv: '/'
}

# Simple HTML Template
quiz_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Math Quiz</title>
</head>
<body>
    <h1>Math Quiz</h1>
    <form method="post">
        <label>Number of Questions:</label><br>
        <input type="number" name="num_questions" required><br><br>

        <label>Difficulty (Easy/Medium/Hard):</label><br>
        <input type="text" name="difficulty" required><br><br>

        <button type="submit">Start Quiz</button>
    </form>

    {% if questions %}
        <h2>Quiz Questions:</h2>
        <ul>
            {% for q in questions %}
                <li>{{ q }}</li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def math_quiz():
    questions = []
    if request.method == 'POST':
        num_questions = int(request.form.get('num_questions'))
        difficulty = request.form.get('difficulty').lower()

        for i in range(num_questions):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)

            if difficulty == 'easy':
                num1 = random.randint(1, 5)
                num2 = random.randint(1, 5)
            elif difficulty == 'hard':
                num1 = random.randint(1, 20)
                num2 = random.randint(1, 20)

            op = random.choice(list(operators.keys()))
            question = f"Question {i + 1}: {num1} {operators[op]} {num2} = ?"
            questions.append(question)

    return render_template_string(quiz_template, questions=questions)

if __name__ == "__main__":
    app.run(debug=True)
