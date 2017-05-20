import os
from cudatext import *
from .run_proc import *


FORMATS_IN = (
  'docbook',
  'haddock',
  'html',
  'json',
  'latex',
  'markdown',
  'markdown_github',
  'markdown_mmd',
  'markdown_phpextra',
  'markdown_strict',
  'mediawiki',
  'native',
  'opml',
  'rst',
  'textile',
  )

FORMATS_OUT = (
  'asciidoc',
  'beamer',
  'context',
  'docbook',
  'docx',
  'dzslides',
  'epub',
  'epub3',
  'fb2',
  'html',
  'html5',
  'json',
  'latex',
  'man',
  'markdown',
  'markdown_github',
  'markdown_mmd',
  'markdown_phpextra',
  'markdown_strict',
  'mediawiki',
  'native',
  'odt',
  'opendocument',
  'opml',
  'org',
  'pdf',
  'plain',
  'revealjs',
  'rst',
  'rtf',
  's5',
  'slideous',
  'slidy',
  'texinfo',
  'textile',
  )

def get_format_in():
    lexer = ed.get_prop(PROP_LEXER_FILE)
    res = None
    if 'HTML' in lexer:
        res = 'html'
    elif lexer=='LaTeX':
        res = 'latex'
    elif lexer=='Markdown':
        res = 'markdown'
    elif lexer=='JSON':
        res = 'json'
    elif lexer=='reStructuredText':
        res = 'rst'
    elif lexer=='Textile':
        res = 'textile'
    elif lexer=='MediaWiki':
        res = 'mediawiki'
    else:
        fmt = ['Input format: '+s for s in FORMATS_IN]
        res = dlg_menu(MENU_LIST, '\n'.join(fmt))
        if res is not None:
            res = FORMATS_IN[res]

    return res


def get_format_out():
    fmt = ['Output format: '+s for s in FORMATS_OUT]
    res = dlg_menu(MENU_LIST, '\n'.join(fmt))
    if res is not None:
        res = FORMATS_OUT[res]
    return res


class Command:
    def run(self):
        fn = ed.get_filename()
        format_in = get_format_in()
        format_out = get_format_out()
        print(format_in, format_out)



