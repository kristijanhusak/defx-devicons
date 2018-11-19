# Defx devicons

Custom implementation of devicons for [defx.nvim](https://github.com/Shougo/defx.nvim).


## Usage
```vimL
:Defx -columns=devicons:filename:type
```
This column is a replacement for mark column. It will properly highlight selected files.

## Configuration
This is the default configuration:

```vimL
let g:defx_devicons_enable_syntax_highlight = 1
let g:defx_devicons_column_length = 2
let g:defx_devicons_directory_icon = ''
let g:defx_devicons_mark_icon = '*'
let g:defx_devicons_parent_icon = ''
let g:defx_devicons_default_icon = ''
```

Note: Syntax highlighting can cause some performance issues in defx window. Just disable it with the `let g:defx_devicons_enable_syntax_highlight = 0`
