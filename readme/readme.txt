plugin for CudaText.
it calls Pandoc tool, to convert current file to some format, which Pandoc supports.

input format: detected by active lexer name, or, if some weird lexer, menu will be shown.
output format: always menu is shown.

note, than PDF is supported by Pandoc only with some additional tool, else you will see error message on converting to pdf.
resulting file is made in the OS temp-folder, you will see filename after converting done.

Pandoc program name:
- Windows: pandoc.exe, w/o folder, so you should add it to system PATH.
- Linux: pandoc
- macOS: /usr/local/bin/pandoc


author: Alexey T. (CudaText)
license: MIT
