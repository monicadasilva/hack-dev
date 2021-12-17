from markdown import extensions
from markdown.extensions import fenced_code
from markdown import markdown
from pygments.formatters import HtmlFormatter


def home():
    readme = open("README.md", "r")
    md_template_string = markdown(readme.read(), extensions=["fenced_code"])
    formatter = HtmlFormatter(style="emacs", full=True, cssclass="codehilite")
    css_string = formatter.get_style_defs()
    md_css_string = "<style>" + css_string + "</style>"

    font = "<style>" + """
        body {
            font-family: Open Sans,sans-serif;
            max-width: 700px;
        }
        .title {
            font-size: 1.75em;
            font-weight: 600;
            margin: 24px 0 16px;
            padding-bottom: 0.3em;
            border-bottom: 1px solid #eaeaea;
            color: #303030;
        }
        h2 {
            font-size: 1.5em;
            font-weight: 600;
            margin: 24px 0 16px;
            padding-bottom: 0.3em;
            border-bottom: 1px solid #eaeaea;
            color: #303030;
        }
        p, li {
            color: #303030;
        }
        p {
            margin: 0 0 16px;
        }
        a {
            color: #1068bf;
            text-decoration: none;
        }
    """ + "</style>"

    title = "<h1 class='title'>HACK_DEV</h1>"
    link_repo = '<a href="https://gitlab.com/Anthony07M/hack_dev">GitLab</a>'
    md_template = md_css_string + font + title + md_template_string + link_repo
    return md_template
