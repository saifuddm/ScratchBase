import requests
import urllib

url = "https://www.nike.com/w/graphql"

query = {
    'queryid' : 'products',
    'endpoint' : '/product_feed/rollup_threads/v2?filter=marketplace(CA)',
    'filter': 'language(en-GB)',
    'filter': 'employeePrice(true)',
    'filter': 'attributeIds(0f64ecc7-d624-4e91-b171-b83a03dd8550,16633190-45e5-4830-a068-232ac7aea82c)',
    'anchor': '0',
    'count': '24',
    'consumerChannelId': 'd9a5bc42-4b9c-4976-858a-f159cf99c647',
    'sort': 'effectiveStartSellDateDesc'
}
urllib.urlencode(query)
BASE_URL = "https://www.nike.com/w/graphql?queryid=products&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(CA)%26filter%3Dlanguage(en-GB)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(0f64ecc7-d624-4e91-b171-b83a03dd8550%2C16633190-45e5-4830-a068-232ac7aea82c)%26anchor%3D0%26count%3D50%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26sort%3DeffectiveStartSellDateDesc"

r = requests.get(url, params=urllib.urlencode(query))
q = requests.get(BASE_URL)

print(q.content)
print(q.url)
