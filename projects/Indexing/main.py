from flask import Flask, render_template, request, url_for, Response
from get_data import data
from thefuzz import fuzz, process
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET"])
def start():
    return render_template("index.html", data=data)


@app.route("/search", methods=["POST"])
def search():
    search_query = request.form.get("search")
    # print("val", search_query)
    # print("data[:5]", data[:3])
    # df1 = pd.DataFrame(data)
    # df1.to_excel('data.xlsx')
    # with open(mycaptions.txt, 'w') as f:

    
    # captions = [(item['id'], item['caption'], item['permalink'], item['media_type'], item.get('thumbnail_url'), '*********************') for item in data]
    results_r =   []
    results_p =   []
    results_ts =  []
    results_tsr = []
    ids_url = []

    for each_dict in data:
        ids_url.append(each_dict)
        results_r.append(fuzz.ratio(search_query, each_dict['caption']))
        results_p.append(fuzz.partial_ratio(search_query, each_dict['caption']))
        results_ts.append(fuzz.token_sort_ratio(search_query, each_dict['caption']))
        results_tsr.append(fuzz.token_set_ratio(search_query, each_dict['caption']))
    final = list(zip(results_r, results_p, results_ts, results_tsr))
    result = [sum(val)/len(val) for val in final]
    arr = list(zip(ids_url, result))
    arr.sort(key=lambda x: x[1], reverse=True)
    new_data = []
    for idx, item in enumerate(arr[:5]):
        new_data.append(item[0])
    # print("new_data", new_data[:2])
    return render_template("index.html", data=new_data)
    # return Response("Worked")

if __name__ == "__main__":
    app.run(debug=True)
