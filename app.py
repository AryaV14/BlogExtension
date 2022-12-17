from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        value = request.form.get('value')
        print(value)
        url = request.form.get('url')
        print(url)
    return render_template('index.html')
       
if __name__ == "__main__":
    app.debug=True
    app.run()