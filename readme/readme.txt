Plugin for CudaText.
Gives command to call Pandoc tool, to convert current file to some format, which Pandoc supports.

Input format: detected by active lexer name, or, if unknown lexer, menu will be shown.
Output format: menu is always shown.

Notes:
- Plugin needs saved file, cannot handle unsaved text yet.
- Resulting file is made in the OS temp-folder, you will see filename after converting done.
- PDF is supported by Pandoc only with some additional tool (Latex), else you will see error message on converting to pdf.

Pandoc program name:
- Windows: pandoc.exe, w/o folder, so you should add it to system PATH.
- Linux: pandoc
- macOS: /usr/local/bin/pandoc


Author: Alexey T. (CudaText)
License: MIT
