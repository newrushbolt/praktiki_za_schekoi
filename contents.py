import sys
import re


header_re = re.compile('^#{2,10}.*', re.MULTILINE)
src_md = sys.stdin.read()
headers = header_re.findall(src_md)

txt_headers_lines = []

for header in headers:
    header_level = (len(re.findall('#', header)) - 2) * '    '
    header_text = re.sub('^#{2,10} ', '', header, re.MULTILINE)
    header_key = header_text.lower()
    header_key = header_key.replace('.', '')
    header_key = header_key.replace('_', '-')
    header_key = header_key.replace(',', '-')
    header_key = header_key.replace(' ', '-')
    header_line = "{}* [{}](#{})".format(header_level, header_text, header_key)
    txt_headers_lines.append(header_line)

txt_headers = '  \n'.join(txt_headers_lines)
print(txt_headers)
