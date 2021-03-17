import smtplib, ssl


address = 'j4nk0test@gmail.com'
password = 't35tPassword'
port = 465  # For Gmail SSL
common_message = """Subject: Automated E-mail\n\nHello, I'm automated system for sending e-mails. You received this email because of """

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(address, password)
    with open('mail_data.csv', 'r') as in_file:
        for line in in_file:
            to_email, custom_message = line.split(',')
            print('sending e-mail to ' + to_email)
            server.sendmail(address, to_email, common_message + custom_message)
    print('All e-mails send succesfully')
            

