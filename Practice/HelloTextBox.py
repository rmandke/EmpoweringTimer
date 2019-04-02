from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('Form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['textbox']
    return text
if __name__ == "__main__":
	app.run(host='127.0.0.1', port=8000)

