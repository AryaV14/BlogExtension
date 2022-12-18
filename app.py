from flask import Flask, render_template, request
app=Flask(__name__)



cat_url_set = []
visited=[]
for _ in range(0,4):
    cat_url_set.append(set())
    visited.append(list())
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        value = request.form.get('value')
        url = request.form.get('url')
        value=int(value)
        print(value)
        read = request.form.get('read')
        if value != 100:
            
            if read == 'on':
                read=1
            else :
                read=0
            print(read)
            
            print(url)
            cat_url_set[value].add(url)
            visited[value].append(read)
            print(cat_url_set)
            print(visited)
            if url in cat_url_set:
                i = cat_url_set.index(url)
                if read == 'on':
                    visited[i] = 1
        else:
            if read == 'on':
                read=1
                if url in cat_url_set:
                    i = cat_url_set.index(url)
                    visited[i] = 1


        
    return render_template('index.html')
       
if __name__ == "__main__":
    app.debug=True
    app.run() 