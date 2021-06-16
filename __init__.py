import os
import tempfile
from cudatext import *
from .run_proc import *

TEMP_DIR = tempfile.gettempdir()

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
        res = dlg_menu(DMENU_LIST, fmt, caption='Input formats')
        if res is not None:
            res = FORMATS_IN[res]

    return res


def get_format_out():
    fmt = ['Output format: '+s for s in FORMATS_OUT]
    res = dlg_menu(DMENU_LIST, fmt, caption='Output formats')
    if res is not None:
        res = FORMATS_OUT[res]
    return res


class Command:
    def run(self):
        fn_in = ed.get_filename()
        if not fn_in:
            msg_status('[Pandoc] Cannot convert untitled tab')
            return

        if ed.get_prop(PROP_MODIFIED):
            msg_status('[Pandoc] Please save file first')
            return

        format_in = get_format_in()
        if format_in is None: return

        format_out = get_format_out()
        if format_out is None: return

        fn_out = os.path.join(TEMP_DIR, '_pandoc.'+format_out)
        if os.path.isfile(fn_out):
            os.remove(fn_out)
        if os.path.isfile(fn_out):
            msg_status('[Pandoc] Cannot delete temp file')
            return

        args = [
            fn_in,
            '-f', format_in,
            '-t', format_out,
            '-o', fn_out
            ]
        run_pandoc(args)

        ok = os.path.isfile(fn_out)
        if ok:
            res = 'converted!'
        else:
            res = 'failed...'

        msg_status('[Pandoc] %s (%s) -> %s ... %s' % (
            os.path.basename(fn_in),
            format_in,
            os.path.basename(fn_out),
            res
            ))

        if ok:
            res = msg_box('Pandoc: converted to file:\n%s\n\nOpen resulting file?'%fn_out, MB_YESNO+MB_ICONINFO)
            if res==ID_YES:
                file_open(fn_out)
        else:
            msg_box('Pandoc: failed to run with args:\n'+repr(args), MB_OK+MB_ICONERROR)
