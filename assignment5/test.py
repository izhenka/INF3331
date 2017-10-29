def verify(function, inputs, outputs):
    for sample_input, expected_output in zip(inputs, outputs):
        actual_output = function(sample_input)
        try:
            assert actual_output == expected_output
        except AssertionError:
            print(
                (
                    "Something seems to be wrong with your code! On the input:\n{}\n"
                    "it should have returned:\n{}\nbut returned:\n{}\n instead!"
                ).format(sample_input, expected_output, actual_output)
            )



#############################
#### email_scraper tests ####
#############################


from scraper import find_emails


sample_inputs = [
    """
    This is a long string
    without an email address
    It is what it is
    """,


    """
    This string has an email!
    karl@erik.no
    (don't expect replies!)
    """,

    """
    Here is an email:simon@funke.no. It's probably not going to work.
    You could try funsim@uio.no, but I don't think that's the right one either.
    """,

    """
    This is a bit of html:
	<span id="vrtx-person-change-language-link">
	  <a href="http://www.mn.uio.no/ifi/personer/vit/karleh/index.html">Norwegian<span class="offscreen-screenreader"> version of this page</span></a>
	</span>



            <div class="vrtx-person-contact-info-line vrtx-email"><span class="vrtx-label">Email</span>

                <a class="vrtx-value" href="mailto:karleh@ifi.uio.no">karleh@ifi.uio.no</a>

            </div>
    """,

    """This is text which contains some email-like strings which aren't emails
    according to the definition of the assignment:
    the string name@server.1o has a number at the start of thedomain,
    the string name@server.o1 has a number at the end,
    the string name@ser<ver.domin has an illegal character in its server,
    as does the string name@ser"ver.domain,

    however, the string na&me@domain.com is actually an email!
    as is n~ame@dom_ain.com
    but name@domain._com is bad
    (name@domain.c_o.uk is allowed though)
    """
]

expected_outputs = [
    [],
    ["karl@erik.no"],
    ["simon@funke.no", "funsim@uio.no"],
    ["karleh@ifi.uio.no", "karleh@ifi.uio.no"],
    ["na&me@domain.com", "n~ame@dom_ain.com", "name@domain.c_o.uk"]

]


verify(find_emails, sample_inputs, expected_outputs)

#############################
####  url_scraper tests  ####
#############################

from scraper import find_urls

sample_inputs = [
    """
    This is a bit of html:
	<span id="vrtx-person-change-language-link">
	  <a href="http://www.mn.uio.no/ifi/personer/vit/karleh/index.html">Norwegian<span class="offscreen-screenreader"> version of this page</span></a>
	</span>



            <div class="vrtx-person-contact-info-line vrtx-email"><span class="vrtx-label">Email</span>

                <a class="vrtx-value" href="mailto:karleh@ifi.uio.no">karleh@ifi.uio.no</a>

            </div>

    This URL is not inside a hyperlink tag, so should be ignored: "http://www.google.com"
    """,

    """
    This is almost a hyperlink, but the quotes are mismatched, so it shouldn't be captured:

    <a href="http://www.google.com/super_secret/all_the_user_data/'>Please don't click</a>

    <a href="http://www.google.com/super_secret/user_data/'>Please don't click</a>



    """,


    """
<b>Lorem</b> ipsum <i>dolor sit amet</i>, consectetur <i>adipiscing elit. Nullam tempor</i> nunc at justo tincidunt congue. <b>Aliquam hendrerit mollis pretium! Praesent id</b> mi est. <a href='http://www.praesent.com'>Praesent,</a> sed orci aliquet, dapibus elit sed, maximus dolor. Donec ut viverra velit, in sollicitudin nisl. Aliquam nec orci sit amet sem congue condimentum. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.

    <blockquote>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse a nulla <i>eget eros euismod volutpat. Suspendisse</i> id luctus lorem. Vivamus non erat bibendum lacus sodales convallis scelerisque ac diam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus eget quam eros. Nulla lectus turpis, porttitor sed laoreet id, varius eget dolor. Proin non sapien et risus dictum suscipit quis id leo. Aenean at mauris vel eros gravida gravida. Sed feugiat <b>molestie *libero vel%% pulvinar? Sed</b> a accumsan risus, at vehicula felis. Nullam eget est blandit eros consectetur facilisis. Etiam ligula augue, fringilla ac nibh sit amet, posuere dignissim libero. Nunc accumsan odio leo, et mollis turpis aliquam eu. Proin sed maximus erat. Maecenas diam velit, tristique et posuere ut, placerat sit amet diam.</blockquote>

    Curabitur finibus, turpis viverra rutrum consequat, ligula tortor consectetur ex, eu malesuada lacus ipsum in %<b> urna. % Fusce</b> in <i>sapien <b>mau*ris.</b> Duis purus dui</i>, viverra in tellus eu, imperdiet fringilla <a href='http://inf3331.no'>felis. Curabitur rhoncus tincidunt varius. Cras</a> gravida metus ut <a href='https://en.wikipedia.org/w/index.php?title=Special:Search&search=vestibulum'>Search Wikipedia for vestibulum</a> vestibulum. *Integer cursus<i> ex* in rutrum volutpat</i>. Nunc scelerisque gravida risus sed ullamcorper. Proin <a href='https://www.maLEsuada.com'>lorem,</a> massa <img src='https://www.mn.uio.no/astro/english/services/it/help/basic-services/latex/uiologo.gif' style='width:100px;height:40px' ;> quam in, scelerisque elementum arcu. Nunc scelerisque sem ac lectus porttitor, sed molestie odio <i>bibendum.</i>

    """,
    """
    <ul class="vrtx-breadcrumb-menu">
            <li class="vrtx-ancestor"> <a href="http://www.ceres.no/om"><span>Om CERES</span></a></li>
            <li class="vrtx-parent"><a class="vrtx-marked" href="http://www.ceres.no/om/ansatte"><span>Ansatte</span></a>

      <ul>
          <li class="vrtx-child"><a href="http://www.ceres.no/om/ansatte/395800/"><span>Seksjon for forskningstjenester</span></a></li>
          <li class="vrtx-child"><a href="http://www.ceres.no/om/ansatte/395400/"><span>Seksjon for stab og støtte</span></a></li>
          <li class="vrtx-child"><a href="http://www.ceres.no/om/ansatte/395600/"><span>Seksjon for systemforvaltning</span></a></li>
          <li class="vrtx-child"><a href="http://www.ceres.no/om/ansatte/395500/"><span>Seksjon for systemutvikling</span></a></li>
      </ul>

    </li>

  </ul>
    """



]

expected_outputs = [
    [
        "http://www.mn.uio.no/ifi/personer/vit/karleh/index.html",
    ],

    [],
    ["http://www.praesent.com", "http://inf3331.no", "https://www.maLEsuada.com"],
    ["http://www.ceres.no/om", "http://www.ceres.no/om/ansatte",
    "http://www.ceres.no/om/ansatte/395800/", "http://www.ceres.no/om/ansatte/395400/",
    "http://www.ceres.no/om/ansatte/395600/", "http://www.ceres.no/om/ansatte/395500/"],

]

verify(find_urls, sample_inputs, expected_outputs)


################################
####  parse_nwodkram tests  ####
################################

from parser import parse_nwodkram



sample_input = r"""
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






expected_output = r"""
This is some Nwodkram text. Note that <i>this</i> is in italic, and <b>this</b> is in bold.
If you want to write an * or an equal sign and not have the parser eat them,
that's easy -  note that * this * is not in italic even though it's between two *s,
and % this % is not in bold.

<a href='http://www.google.com'>here</a> is a hyperlink.
<a href='http://www.google.com'>here</a> is another.
<a href='https://www.weird?$|site.weird/path/'>and here</a> is a third with some weird characters.
Follow it at your own peril.

Ideally, it would be good if your hyperlinks can contain parentheses and underscores.
But don't worry too much if some weird combination is ambiguous or results in
weird stuff.
"""
verify(parse_nwodkram, [sample_input], [expected_output])
