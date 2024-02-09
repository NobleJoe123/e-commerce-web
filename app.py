from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shop', methods=['GET', 'POST'])
def shop():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('shop.html')

if __name__ == '__main__':
    app.run(debug=True)