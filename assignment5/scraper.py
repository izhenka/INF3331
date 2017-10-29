import re
import urllib.request

def find_emails(text):
    name = server = r"[\w\.#$%&~’\*\+\-/=?‘|{}.]+"
    regex = f"{name}@{server}"+r"(?:\.[a-z](?:\w+)*[a-z])"
    result = re.findall(regex, text, flags=re.IGNORECASE)
    return result


def find_urls(text):
    regex = r"<a\s+(?:class.+)?href\s*=\s*(\"|\')(http[s]?://(?:www\.)?[a-z1-9\.\-~]+\.[a-z1-9\.\-~]+[a-z1-9/\.\-~]*)\1>"
    matches = re.findall(regex, text,flags=re.IGNORECASE)
    return list(map(lambda x: x[1], matches))

def all_the_emails(url, depth):
    emails = []
    all_the_emails_recursive(url, depth, emails)
    return list(set(emails))


def all_the_emails_recursive(url, depth, all_emails):
    response = str(urllib.request.urlopen(url).read())
    emails = find_emails(response)

    print(f"\n----depth {depth}, url '{url}'---")
    print(f"emails:\n{emails}")

    if depth == 0:
        all_emails.extend(emails)
        return

    urls = find_urls(response)
    print(f"urls:\n{urls}")

    for inner_url in urls:
        all_the_emails_recursive(inner_url, depth-1, all_emails)



if __name__ == '__main__':
    emails = all_the_emails("https://www.uio.no/", 1)
    print(f"*** Result ****\nemails:\n{emails}")
