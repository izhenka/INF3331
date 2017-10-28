import re

def parse_nwodkram(text):
    result = parse_bold(text)
    result = parse_italic(result)
    result = parse_escaped_tags(result)
    result = parse_links(result)
    result = parse_images(result)
    result = parse_blockquotes(result)
    result = parse_wiki_searches(result)
    return result

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
    regex_in = r"\[([^\]]+)\]\(((http[s]?:\/\/)?[^)]+)\)"
    regex_out = r"<a href='\2'>\1</a>"
    return re.sub(regex_in, formate_link, text)

def formate_link(matchobj):
    prefix = ""
    if matchobj.group(3) == None:
        prefix = "http://"

    group1 = matchobj.group(1)
    group2 = matchobj.group(2)
    return f"<a href='{prefix}{group2}'>{group1}</a>"

def parse_images(text):
    regex_in = r"<(http.+)>\(w=(\d+),h=(\d+)\)"
    regex_out = r"<img src='\1' style='width:\2px;height:\3px' ;>"
    return re.sub(regex_in, regex_out, text)

def parse_blockquotes(text):
    regex_in = r">>(.+)"
    regex_out = r"<blockquote>\1</blockquote>"
    return re.sub(regex_in, regex_out, text)

def parse_wiki_searches(text):
    regex_in = r"\[wp:(.+)\]"
    # print(re.findall(regex_in, text))
    regex_out = r"<a href='https://en.wikipedia.org/w/index.php?title=Special:Search&search=\1'>Search Wikipedia for \1</a>"
    return re.sub(regex_in, regex_out, text)



if __name__ == '__main__':

    source_text = """%Lorem% ipsum *dolor sit amet*, consectetur *adipiscing elit. Nullam tempor* nunc at justo tincidunt congue. %Aliquam hendrerit mollis pretium! Praesent id% mi est. [Praesent,](www.praesent.com) sed orci aliquet, dapibus elit sed, maximus dolor. Donec ut viverra velit, in sollicitudin nisl. Aliquam nec orci sit amet sem congue condimentum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.

    >>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse a nulla *eget eros euismod volutpat. Suspendisse* id luctus lorem. Vivamus non erat bibendum lacus sodales convallis scelerisque ac diam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus eget quam eros. Nulla lectus turpis, porttitor sed laoreet id, varius eget dolor. Proin non sapien et risus dictum suscipit quis id leo. Aenean at mauris vel eros gravida gravida. Sed feugiat %molestie \*libero vel\%\% pulvinar? Sed% a accumsan risus, at vehicula felis. Nullam eget est blandit eros consectetur facilisis. Etiam ligula augue, fringilla ac nibh sit amet, posuere dignissim libero. Nunc accumsan odio leo, et mollis turpis aliquam eu. Proin sed maximus erat. Maecenas diam velit, tristique et posuere ut, placerat sit amet diam.

    Curabitur finibus, turpis viverra rutrum consequat, ligula tortor consectetur ex, eu malesuada lacus ipsum in \%% urna. \% Fusce% in *sapien %mau\*ris.% Duis purus dui*, viverra in tellus eu, imperdiet fringilla [felis. Curabitur rhoncus tincidunt varius. Cras](inf3331.no) gravida metus ut [wp:vestibulum] vestibulum. \*Integer cursus* ex\* in rutrum volutpat*. Nunc scelerisque gravida risus sed ullamcorper. Proin [lorem,](https://www.malesuada.com) massa <https://www.mn.uio.no/astro/english/services/it/help/basic-services/latex/uiologo.gif>(w=100,h=40) quam in, scelerisque elementum arcu. Nunc scelerisque sem ac lectus porttitor, sed molestie odio *bibendum.*
    """

    result = parse_nwodkram(source_text)
    with open('out.html', 'w') as f:
        print(result, file=f)
