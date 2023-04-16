from flask import Flask, render_template, request
import requests

app = Flask(__name__)

subscription_key = "50557c8f4f514d33a94d20c68951ac23" # YOUR_SUBSCRIPTION_KEY: Bing Search API 구독 키
endpoint = "https://api.bing.microsoft.com/" # YOUR_ENDPOINT: Bing Search API 엔드포인트

@app.route('/', methods=['GET', 'POST'])
def index():
    videos = []
    message = None
    search_term = ""
    if request.method == 'POST':
        search_term = request.form['search_term']
        headers = {"Ocp-Apim-Subscription-Key": subscription_key}
        params = {"q": search_term, "responseFilter": "Videos"}
        response = requests.get(endpoint + "/v7.0/search", headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
        if search_results.get('rankingResponse', {}) == {}:
            message = "검색 결과가 없습니다. 다시 검색해주세요."
        else:
            videos = search_results.get("videos", {}).get("value", [])
    return render_template('index.html', videos=videos, message=message, search_term=search_term)


if __name__ == '__main__':
    app.run(port=5003)


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         search_term = request.form['search_term']
#         headers = {"Ocp-Apim-Subscription-Key": subscription_key}
#         params = {"q": search_term, "responseFilter": "Videos"}
#         response = requests.get(endpoint + "/v7.0/search", headers=headers, params=params)
#         response.raise_for_status()
#         search_results = response.json()
#         ### videos = search_results.get("videos", {}).get("value", [])[:3]

#         if search_results['rankingResponse']=={}:
#             print('검색 결과가 없습니다./n')

#         videos = search_results.get("videos", {}).get("value", []) ###[:3]
#         for video in videos:
#             print('* * * 영상 제목 : ' + video["name"])
#             print('* * * 영상 주소 : ' + video["contentUrl"])
#             print('* * * 영상 스크립트 : ' + video['description'])
#             print()

#         return render_template('index.html', videos=videos)
#     return render_template('index.html')