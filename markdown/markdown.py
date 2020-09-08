import re

def parse(markdown: str) -> str:
    def wrap_tag(word: str, tag: str) -> str:
        return f'<{tag}>' + word + f'</{tag}>'

    def wrap_group_3(regex: str, word: str, tag: str):
        return (wrapper.group(1) + wrap_tag(wrapper.group(2), tag) + wrapper.group(3)
                if (wrapper := re.match(regex, word))
                else word)

    def format_text(text: str) -> str:
        text = wrap_group_3(r'(.*)__(.*)__(.*)', text, 'strong')
        text = wrap_group_3(r'(.*)_(.*)_(.*)', text, 'em')
        return text

    in_list_append: bool = False
    in_list: bool = False
    res: str = ''

    for line in markdown.split('\n'):
        if a := re.match(r'^(#*) (.*)', line):
            line = wrap_tag(a.group(2), f'h{len(a.group(1))}')

        if list_ := re.match(r'\* (.*)', line):
            line = ('<ul>' if not in_list else '') + wrap_tag(format_text(list_.group(1)), 'li')
            in_list = True
        else:
            if in_list:
                in_list = False
                in_list_append = True

        if not re.match('<h|<ul|<p|<li', line):
            line = wrap_tag(line, 'p')

        res += ('</ul>' if in_list_append else '') + format_text(line)
        in_list_append = False

    return res + ('</ul>' if in_list else '')
