import re

def parse_bold(text):
    tag = r"(?:(?<!\\)%)"
    regex_in = tag + r"((?:\\%|[^%])+)" + tag
    regex_out = r"<b>\1</b>"
    return re.sub(regex_in, regex_out, text)

def parse_italic(text):
    tag = r"(?:(?<!\\)\*)"
    regex_in = tag + r"((?:\\\*|[^\*])+)" + tag
    regex_out = r"<i>\1</i>"
    return re.sub(regex_in, regex_out, text)

def parse_escaped_tags(text):
    regex_in = r"\\([%\*])"
    return re.sub(regex_in, r"\1", text)

def parse_links(text):
    regex_in = r"\[([^\[\]]+)\]\(((http[s]?:\/\/)?.+)\)"
    regex_out = r"<a href='\2'>\1</a>"
    return re.sub(regex_in, formate_link, text)

def formate_link(matchobj):
    prefix = ""
    if matchobj.group(3) == None:
        prefix = "http://"

    group1 = matchobj.group(1)
    group2 = matchobj.group(2)
    return f"<a href='{prefix}{group2}'>{group1}</a>"

def parse_nwodkram(text):
    result = parse_bold(text)
    result = parse_italic(result)
    result = parse_escaped_tags(result)
    result = parse_links(result)
    return result

if __name__ == '__main__':

    source_text = r"""
    This is some Nwodkram text. Note that *this* is in italic, and %this% is in bold.
    If you want to write an \* or an equal sign and not have the parser eat them,
    that's easy -  note that \* this \* is not in italic even though it's between two \*s,
    and \% this \% is not in bold.

    [here](www.google.com) is a hyperlink.
    [here](http://www.google.com) is another.
    [and here](https://www.weird?$|site.weird/path/) is a third with some weird characters.
    Follow it at your own peril.

    Ideally, it would be good if your hyperlinks can contain parentheses and underscores.
    But don't worry too much if some weird combination is ambiguous or results in
    weird stuff.
    """
    result = parse_nwodkram(source_text)
    with open('out.html', 'w') as f:
        print(result, file=f)
