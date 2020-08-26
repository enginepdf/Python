test='@'
account=['email_id','gmail.com']
new_test=test.join(account)

id, email=account
id_check, email_check=id, email

print(id, email) # email_id gmail.com
print(id_check, email_check) # email_id gmail.com
print(test) # @
print(new_test) # email_id@gmail.com