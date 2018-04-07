import random, string
domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com", "rediffmail.com", "zoho.com",  "mail.com", "fastmail.com", "gmx.com", "hushmail.com",  "yahoo.com"]
letters = string.ascii_lowercase[:12]

def generate_random_email(length):
    return ''.join(random.choice(letters) for i in range(length)) + '@' + random.choice(domains)
