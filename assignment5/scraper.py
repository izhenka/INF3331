import re

def find_emails(text):
    regex = r"\w+@\w+(?:\.\w+)+"
    name = server = r"[\w\.#$%&~’\*\+\-/=?‘|{}.]+"
    regex = f"{name}@{server}"+r"(?:\.[a-zA-Z](?:\w+)*[a-zA-Z])"
    result = re.findall(regex, text)
    return result



if __name__ == '__main__':
    text = ""
    print(find_emails(text))
