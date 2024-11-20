from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/health-benefits')
def health_benefits():
    return render_template('health_benefits.html')

@app.route('/workouts')
def workouts():
    return render_template('workouts.html')

@app.route('/diet')
def diet():
    return render_template('diet.html')

if __name__ == '__main__':
    app.run(debug=True)