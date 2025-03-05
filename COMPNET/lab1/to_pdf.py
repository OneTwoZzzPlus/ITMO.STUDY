# https://pypi.org/project/markdown-pdf/

from markdown_pdf import MarkdownPdf, Section

pdf = MarkdownPdf(toc_level=2)

pdf.add_section(Section(open('README.MD', 'r', encoding='utf-8').read()))

pdf.save('README.pdf')