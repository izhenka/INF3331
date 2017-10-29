import re

def find_emails(text):
    name = server = r"[\w\.#$%&~’\*\+\-/=?‘|{}.]+"
    regex = f"{name}@{server}"+r"(?:\.[a-z](?:\w+)*[a-z])"
    result = re.findall(regex, text, flags=re.IGNORECASE)
    return result


def find_urls(text):
    regex = r"<a\s+(?:class.+)?href\s*=\s*(\"|\')(http[s]?://(?:www\.)?[a-z1-9\.\-~]+\.[a-z1-9\.\-~]+[a-z1-9/\.\-~]*)\1>"
    matches = re.findall(regex, text,flags=re.IGNORECASE)
    return list(map(lambda x: x[1], matches))
