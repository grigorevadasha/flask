from flask import Flask, render_template, request

app = Flask(__name__)

# Главная страница
@app.route('/')
def home():
    return render_template('web.html')

# Страница со списком лекарств
@app.route('/list', methods=['GET', 'POST'])
def list():
    return render_template('list.html')

# Страница календаря-планировщика
@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

if __name__ == '__main__':
    app.run(debug=True)
