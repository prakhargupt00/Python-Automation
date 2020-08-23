#checks  the number of unread messages in your mail account 

import imaplib
#imaplib is used for accessing email over IMAP(internet mail access protocol)
#It is a built-in library

#connect to imap gmail server using socket connection
host='imap.gmail.com'
gmail_connection = imaplib.IMAP4_SSL(host)

#login into  gmail
email=input("Enter your  Gmail ID: ")
passw=input("Enter your Password: ")

# .login authenticates the client
gmail_connection.login(email,passw)

# .select helps to select a mailbox to access the messages 
gmail_connection.select(mailbox='INBOX')

status, num_of_unseen_messages = gmail_connection.status('INBOX','(UNSEEN)')

print(b)  #[b'"INBOX" (UNSEEN 5818)']
print(type(b)) #list 
print(type(b[0])) #bytes

num = str(b[0])
num = num[18:22]

print("There are " + num + "unread messages in your account")
