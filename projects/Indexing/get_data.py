import requests

url = "https://graph.instagram.com/me/media?"
fields = "id,media_type,media_url,permalink,thumbnail_url,caption"
# fields = "id"
# token = "IGQWRQbnBwZAVg2b1ZAXVjFxVlVUeVBMN1RqazBBSTRmVlBJSnBRTDA5Vl84QV9TM29sblRZAMGxCNVlTdG53dENQTExNd05Gd1diaDVFWC05YnJLcDJKTThhUWpSa1NHeXltaGRuS19QTF9rOXFxME5WM1B4SldYelUZD"
token = "IGQWRQUERDMzM4RTRKSlJWRklSdEJIaVEtNUYwR3Nnb0xHNk8xVnI2SS1seE9xU005Ri1OX2xiRUlTWVBEY25NX0R1TWhpa2FQd3YzU2NueXNidmk0Vnl1MkdkR0p4bTZAsR0x6S3hsVmNBdUwzazZAVQXd1enZAWZAm8ZD"
s = f'{url}fields={fields}&access_token={token}'
# res = requests.get(s)
# data = res.json()['data']
def get_all(s):
    res = requests.get(s)
    result = res.json()['data']

    while requests.get(s).json()['paging'].get('next'):
        s = res.json()['paging']['next']
        res = requests.get(s)
        res.json()   # dictionary
        val = res.json()['data']
        result.extend(val)
    return result

data = get_all(s)
# print("data[0]", data[0])



'''import requests
num = 1

url = "https://graph.instagram.com/me/media?"
fields = "id,media_type,permalink,thumbnail_url, caption"
# token = "IGQWRQbnBwZAVg2b1ZAXVjFxVlVUeVBMN1RqazBBSTRmVlBJSnBRTDA5Vl84QV9TM29sblRZAMGxCNVlTdG53dENQTExNd05Gd1diaDVFWC05YnJLcDJKTThhUWpSa1NHeXltaGRuS19QTF9rOXFxME5WM1B4SldYelUZD"
token = "IGQWRQUERDMzM4RTRKSlJWRklSdEJIaVEtNUYwR3Nnb0xHNk8xVnI2SS1seE9xU005Ri1OX2xiRUlTWVBEY25NX0R1TWhpa2FQd3YzU2NueXNidmk0Vnl1MkdkR0p4bTZAsR0x6S3hsVmNBdUwzazZAVQXd1enZAWZAm8ZD"

res = requests.get(f'{url}fields={fields}&access_token={token}')
res.json()
data = res.json()['data']

print("data", data)'''