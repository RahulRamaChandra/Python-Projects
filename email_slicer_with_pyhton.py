"""An Email slicer is a very useful program for separating the username and domain name of an email address.
This  program can retrieve the username and the domain name of the email."""

email = input("Enter Your Email: ").strip()
username = email[:email.index('@')]
domain_name = email[email.index('@')+1:]
format_ = (f"Your username is '{username}' and your domain is '{domain_name}'")
print(format_)