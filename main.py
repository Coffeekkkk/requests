import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
resp = requests.get(url)
# newlist = sorted(resp.json(), key=lambda d: d['powerstats']['intelligence'])
comparison_hero = ['Hulk', 'Captain America', 'Thanos']
new_list = []
for i in resp.json():
    for j in comparison_hero:
        if i['name'].lower() == j.lower():
            new_list.append(i)
list_sort = sorted(new_list, key=lambda d: d['powerstats']['intelligence'])
print(f'Самый умный списка героев: {list_sort[-1]["name"]}')
