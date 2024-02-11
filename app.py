from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('index'))    
    return render_template('index.html')


@app.route('/shop', methods=['GET', 'POST'])
def shop():
    if request.method == 'POST':
        return redirect(url_for('shop'))
    return render_template('shop.html')

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        return redirect(url_for('checkout'))
    return render_template('chackout.html')

@app.route('/shopdetail', methods=['GET', 'POST'])
def shopdetail():
    if request.method == 'POST':
        return redirect(url_for('shopdetail'))
    return render_template('shop-detail.html')

@app.route('/testimonial', methods=['GET', 'POST'])
def testimonial():
    if request.method == 'POST':
        return redirect(url_for('testimonial'))
    return render_template('testimonial.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return redirect(url_for('contact'))
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)