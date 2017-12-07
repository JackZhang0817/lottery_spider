from database import MySQL

datebase = MySQL()

id = '1'
sql = "SELECT name FROM user WHERE id=" + id
result = datebase.query(sql)
print(result)


result2 = datebase.query_dic({
    'insert': 'user',
    'domain_array': [
        'name',
    ],
    'value_array': [
        '李师玲2'
    ]
})
print(result2)