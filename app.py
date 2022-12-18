from flask import Flask, render_template, request
app=Flask(__name__)



cat_url_set = []
visited=[]
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        value = request.form.get('value')
        value=int(value)
        cat_url_set.append(set())
        print(value)

        visited.append(list())

        url = request.form.get('url')
        print(url)
        cat_url_set[value].add(url)
        visited[value].append(0)
        print(cat_url_set)
        
    return render_template('index.html')
       
if __name__ == "__main__":
    app.debug=True
    app.run() 