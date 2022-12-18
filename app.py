from flask import Flask, render_template, request
app=Flask(__name__)


count_visit = []
total = []
cat_url_set = []
visited=[]
percent=[]
for _ in range(0,4):
    cat_url_set.append(list())
    visited.append(list())
    count_visit.append(0)
    total.append(0)
    percent.append(0)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        value = request.form.get('value')
        value=int(value)

        url = request.form.get('url')

        read = request.form.get('read')
        if value != 100:
            
            if read == 'on':
                read=1
                count_visit[value]= count_visit[value]+1
                print("Visited blogs count:")
                print(count_visit)
                
            else :
                read=0
            if url not in cat_url_set[value]:
                cat_url_set[value].append(url)
                total[value]=total[value]+1
                print("Total blogs :")
                print(total)
            
                visited[value].append(read)
            i = cat_url_set[value].index(url)
            visited[value][i] = read
            print("Urls")
            print(cat_url_set)
            print("Visited")
            print(visited)
          
        else:
            if read == 'on':
                read=1
                if url in cat_url_set:
                    i = cat_url_set.index(url)
                    visited[i] = 1

        percent[value]= (count_visit[value]/total[value])*100
        print("Percentage of completion:")
        print(percent)        
    return render_template('index.html')
       
if __name__ == "__main__":
    app.debug=True
    app.run() 