import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("kshitijsangar@gmail.com", "")

# message to be sent
message = "Message : This is my Demo Project for Python...from KIT 2019"

# sending the mail
s.sendmail("kshitijsangar@gmail.com", "harshithhk98@gmail.com", message)

# terminating the session
s.quit()