import requests

subscription_key = "50557c8f4f514d33a94d20c68951ac23" # YOUR_SUBSCRIPTION_KEY: Bing Search API 구독 키
endpoint = "https://api.bing.microsoft.com/" # YOUR_ENDPOINT: Bing Search API 엔드포인트
#search_term = "비빔밥 요리 방법"
#search_term = "How to use ChatGPT" # SEARCH_QUERY: 사용자 입력 검색 쿼리
search_term = "MBTI별 성격"
headers = {"Ocp-Apim-Subscription-Key": subscription_key}
params = {"q": search_term, "responseFilter": "Videos"}
response = requests.get(endpoint + "/v7.0/search", headers=headers, params=params)
response.raise_for_status()
search_results = response.json()

####print(search_results)
'''
json
{
  "_type": "SearchResponse",
  "queryContext": {
    "originalQuery": "How to use ChatGPT"
  },
  "videos": {
    "id": "https://api.bing.microsoft.com/api/v7/#Videos",
    "readLink": "https://api.bing.microsoft.com/api/v7/videos/search?q=How+to+use+ChatGPT",
    "webSearchUrl": "https://www.bing.com/videos/search?q=How+to+use+ChatGPT",
    "isFamilyFriendly": true,
    "value": [
        {
        "webSearchUrl": "",
        "name": "",
        "description": "",
        "thumbnailUrl": "",
        "datePublished": "",
        "publisher": [
            {
                "name": ""
            }
        ],
        "creator": {
            "name": ""
        },
        "isAccessibleForFree": "",
        "contentUrl": "",
        "hostPageUrl": "",
        "encodingFormat": "",
        "hostPageDisplayUrl": "",
        "width": "",
        "height": "",
        "duration": "",
        "motionThumbnailUrl": "",
        "embedHtml": "",
        "allowHttpsEmbed": "",
        "viewCount": "",
        "thumbnail": {
            "width": "",
            "height": ""
        },
        "allowMobileEmbed": "",
        "isSuperfresh": ""
    }
    ]
  }
  "rankingResponse": {
    "mainline": {
        "items": [{
            "answerType":,
            "value"
        }]
    }
  }
}
'''

# for (k, v) in search_results.items():
#     print(k)


if search_results['rankingResponse']=={}:
    print('검색 결과가 없습니다./n')

videos = search_results.get("videos", {}).get("value", [])
for video in videos:
    print('* * * 영상 제목 : ' + video["name"])
    print('* * * 영상 주소 : ' + video["contentUrl"])
    print('* * * 영상 스크립트 : ' + video['description'])
    print()