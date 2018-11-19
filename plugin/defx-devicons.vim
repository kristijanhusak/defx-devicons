if exists('g:loaded_defx_devicons')
  finish
endif
let g:loaded_defx_devicons = 1

let g:defx_devicons_enable_syntax_highlight = get(g:, 'defx_devicons_enable_syntax_highlight', 1)
let g:defx_devicons_column_length = get(g:, 'defx_devicons_column_length', 2)
let g:defx_devicons_directory_icon = get(g:, 'defx_devicons_directory_icon', '')
let g:defx_devicons_mark_icon = get(g: , 'defx_devicons_mark_icon', '*')
let g:defx_devicons_parent_icon = get(g:, 'defx_devicons_parent_icon', '')
let g:defx_devicons_default_icon = get(g:, 'defx_devicons_default_icon', '')
