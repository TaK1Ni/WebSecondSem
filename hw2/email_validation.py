import re

def is_valid_email(mail):
    format_mail = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$"
    return bool(re.match(format_mail, mail))

def fun(s):
    return is_valid_email(s)

def filter_mail(mail):
    return list(filter(fun, mail))


if __name__ == '__main__':
    n = int(input())
    mail = []
    for _ in range(n): mail.append(input())

    result_mail = filter_mail(mail)
    result_mail.sort()
    print(result_mail)