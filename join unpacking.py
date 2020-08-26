test='@'
item1, item2, *rest, spam, mails=['email_id','gmail.com','500','emails unread','1000','spams']
account=[item1,item2]
new_test=test.join(account)

id, email=account
id_check, email_check=id, email

print(id, email) # email_id gmail.com
print(id_check, email_check) # email_id gmail.com
print(test) # @
print(new_test) # email_id@gmail.com
print(rest) # ['500', 'emails unread']
print(spam, mails) # 1000 spams