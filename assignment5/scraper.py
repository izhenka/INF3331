import re
import urllib.request
import urllib.error

def find_emails(text):
    name = server = r"[\w\.#$%&~’\*\+\-/=?‘|{}.]+"
    regex = f"{name}@{server}"+r"(?:\.[a-z](?:\w+)*[a-z])"
    result = re.findall(regex, text, flags=re.IGNORECASE)
    return result


def find_urls(text):
    regex = r"<a\s+(?:class.+)?href\s*=\s*(\"|\')(http[s]?://(?:www\.)?[a-z0-9\.\-~]+\.[a-z0-9\.\-~]+[a-z0-9/\.\-~]*)\1"
    matches = re.findall(regex, text,flags=re.IGNORECASE)
    return list(map(lambda x: x[1], matches))

def all_the_emails(url, depth):
    emails = []
    urls_checked = []

    all_the_emails_recursive(url, depth, emails, urls_checked)
    return list(set(emails))


def all_the_emails_recursive(url, depth, all_emails, urls_checked):

    # print(f"\ndepth {depth}, url '{url}'")

    if url in urls_checked:
        return

    print(f"cheking '{url}' ...")
    urls_checked.append(url)

    try: response = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        print(e.reason)
        return

    response = str(response.read())
    emails = find_emails(response)

    # print(f"\temails:\n{emails}")

    urls = find_urls(response)
    # print(f"\turls:\n{urls}")


    if depth == 0:
        all_emails.extend(emails)
        return


    for inner_url in set(urls):
        all_the_emails_recursive(inner_url, depth-1, all_emails, urls_checked)



if __name__ == '__main__':
    emails = all_the_emails("https://www.ceres.no/", 3)
    print(f"*** Result ****\nemails:\n{emails}")
