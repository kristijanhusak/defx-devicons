#! /usr/bin/env python3
# ============================================================================
# FILE: devicons.py
# AUTHOR: Mike Hartington <mhartington at gmail.com>
# License: MIT license
# ============================================================================

import re
from pathlib import Path
from defx.base.column import Base
from defx.context import Context
from neovim import Nvim

color_brown = "905532"
color_aqua = "3AFFDB"
color_blue = "689FB6"
color_darkBlue = "44788E"
color_purple = "834F79"
color_lightPurple = "834F79"
color_red = "AE403F"
color_beige = "F5C06F"
color_yellow = "F09F17"
color_orange = "D4843E"
color_darkOrange = "F16529"
color_pink = "CB6F6F"
color_salmon = "EE6E73"
color_green = "8FAA54"
color_lightGreen = "31B53E"
color_white = "FFFFFF"

extensions = {
    'styl': {'icon': '', 'color': color_green},
    'sass': {'icon': '', 'color': color_white},
    'scss': {'icon': '', 'color': color_pink},
    'htm': {'icon': '', 'color': color_darkOrange},
    'html': {'icon': '', 'color': color_darkOrange},
    'slim': {'icon': '', 'color': color_orange},
    'ejs': {'icon': '', 'color': color_yellow},
    'css': {'icon': '', 'color': color_blue},
    'less': {'icon': '', 'color': color_darkBlue},
    'md': {'icon': '', 'color': color_yellow},
    'markdown': {'icon': '', 'color': color_yellow},
    'rmd': {'icon': '', 'color': color_white},
    'json': {'icon': '', 'color': color_beige},
    'js': {'icon': '', 'color': color_beige},
    'jsx': {'icon': '', 'color': color_blue},
    'rb': {'icon': '', 'color': color_red},
    'php': {'icon': '', 'color': color_purple},
    'py': {'icon': '', 'color': color_yellow},
    'pyc': {'icon': '', 'color': color_yellow},
    'pyo': {'icon': '', 'color': color_yellow},
    'pyd': {'icon': '', 'color': color_yellow},
    'coffee': {'icon': '', 'color': color_brown},
    'mustache': {'icon': '', 'color': color_orange},
    'hbs': {'icon': '', 'color': color_orange},
    'conf': {'icon': '', 'color': color_white},
    'ini': {'icon': '', 'color': color_white},
    'yml': {'icon': '', 'color': color_white},
    'yaml': {'icon': '', 'color': color_white},
    'bat': {'icon': '', 'color': color_white},
    'jpg': {'icon': '', 'color': color_aqua},
    'jpeg': {'icon': '', 'color': color_aqua},
    'bmp': {'icon': '', 'color': color_aqua},
    'png': {'icon': '', 'color': color_aqua},
    'gif': {'icon': '', 'color': color_aqua},
    'ico': {'icon': '', 'color': color_aqua},
    'twig': {'icon': '', 'color': color_green},
    'cpp': {'icon': '', 'color': color_blue},
    'c++': {'icon': '', 'color': color_blue},
    'cxx': {'icon': '', 'color': color_blue},
    'cc': {'icon': '', 'color': color_blue},
    'cp': {'icon': '', 'color': color_blue},
    'c': {'icon': '', 'color': color_blue},
    'h': {'icon': '', 'color': color_white},
    'hpp': {'icon': '', 'color': color_white},
    'hxx': {'icon': '', 'color': color_white},
    'hs': {'icon': '', 'color': color_beige},
    'lhs': {'icon': '', 'color': color_beige},
    'lua': {'icon': '', 'color': color_purple},
    'java': {'icon': '', 'color': color_purple},
    'sh': {'icon': '', 'color': color_lightPurple},
    'fish': {'icon': '', 'color': color_green},
    'bash': {'icon': '', 'color': color_white},
    'zsh': {'icon': '', 'color': color_white},
    'ksh': {'icon': '', 'color': color_white},
    'csh': {'icon': '', 'color': color_white},
    'awk': {'icon': '', 'color': color_white},
    'ps1': {'icon': '', 'color': color_white},
    'ml': {'icon': 'λ', 'color': color_yellow},
    'mli': {'icon': 'λ', 'color': color_yellow},
    'diff': {'icon': '', 'color': color_white},
    'db': {'icon': '', 'color': color_blue},
    'sql': {'icon': '', 'color': color_darkBlue},
    'dump': {'icon': '', 'color': color_blue},
    'clj': {'icon': '', 'color': color_green},
    'cljc': {'icon': '', 'color': color_green},
    'cljs': {'icon': '', 'color': color_green},
    'edn': {'icon': '', 'color': color_green},
    'scala': {'icon': '', 'color': color_red},
    'go': {'icon': '', 'color': color_beige},
    'dart': {'icon': '', 'color': color_white},
    'xul': {'icon': '', 'color': color_darkOrange},
    'sln': {'icon': '', 'color': color_purple},
    'suo': {'icon': '', 'color': color_purple},
    'pl': {'icon': '', 'color': color_blue},
    'pm': {'icon': '', 'color': color_blue},
    't': {'icon': '', 'color': color_blue},
    'rss': {'icon': '', 'color': color_darkOrange},
    'f#': {'icon': '', 'color': color_darkBlue},
    'fsscript': {'icon': '', 'color': color_blue},
    'fsx': {'icon': '', 'color': color_blue},
    'fs': {'icon': '', 'color': color_blue},
    'fsi': {'icon': '', 'color': color_blue},
    'rs': {'icon': '', 'color': color_darkOrange},
    'rlib': {'icon': '', 'color': color_darkOrange},
    'd': {'icon': '', 'color': color_red},
    'erl': {'icon': '', 'color': color_lightPurple},
    'hrl': {'icon': '', 'color': color_pink},
    'vim': {'icon': '', 'color': color_green},
    'ai': {'icon': '', 'color': color_darkOrange},
    'psd': {'icon': '', 'color': color_darkBlue},
    'psb': {'icon': '', 'color': color_darkBlue},
    'ts': {'icon': '', 'color': color_blue},
    'tsx': {'icon': '', 'color': color_white},
    'jl': {'icon': '', 'color': color_purple},
    'pp': {'icon': '', 'color': color_white},
    'vue': {'icon': '﵂', 'color': color_green},
}

exact_matches = {
    'exact-match-case-sensitive-1.txt': {'icon': '1', 'color': color_white},
    'exact-match-case-sensitive-2': {'icon': '2', 'color': color_white},
    'gruntfile.coffee': {'icon': '', 'color': color_yellow},
    'gruntfile.js': {'icon': '', 'color': color_yellow},
    'gruntfile.ls': {'icon': '', 'color': color_yellow},
    'gulpfile.coffee': {'icon': '', 'color': color_pink},
    'gulpfile.js': {'icon': '', 'color': color_pink},
    'gulpfile.ls': {'icon': '', 'color': color_pink},
    'dropbox': {'icon': '', 'color': color_white},
    '.ds_store': {'icon': '', 'color': color_white},
    '.gitconfig': {'icon': '', 'color': color_white},
    '.gitignore': {'icon': '', 'color': color_white},
    '.bashrc': {'icon': '', 'color': color_white},
    '.zshrc': {'icon': '', 'color': color_white},
    '.vimrc': {'icon': '', 'color': color_white},
    '.gvimrc': {'icon': '', 'color': color_white},
    '_vimrc': {'icon': '', 'color': color_white},
    '_gvimrc': {'icon': '', 'color': color_white},
    '.bashprofile': {'icon': '', 'color': color_white},
    'favicon.ico': {'icon': '', 'color': color_yellow},
    'license': {'icon': '', 'color': color_white},
    'node_modules': {'icon': '', 'color': color_green},
    'react.jsx': {'icon': '', 'color': color_blue},
    'procfile': {'icon': '', 'color': color_purple},
    'dockerfile': {'icon': '', 'color': color_blue},
    'docker-compose.yml': {'icon': '', 'color': color_yellow},
}

pattern_matches = {
    '.*jquery.*\.js$': {'icon': '', 'color': color_blue},
    '.*angular.*\.js$': {'icon': '', 'color': color_red},
    '.*backbone.*\.js$': {'icon': '', 'color': color_darkBlue},
    '.*require.*\.js$': {'icon': '', 'color': color_blue},
    '.*materialize.*\.js$': {'icon': '', 'color': color_salmon},
    '.*materialize.*\.css$': {'icon': '', 'color': color_salmon},
    '.*mootools.*\.js$': {'icon': '', 'color': color_white},
    '.*vimrc.*': {'icon': '', 'color': color_white},
    'Vagrantfile$': {'icon': '', 'color': color_white},
}


class Column(Base):
    def __init__(self, vim: Nvim) -> None:
        super().__init__(vim)
        self.vim = vim
        self.name = 'devicons'
        self.column_length = self.vim.vars['defx_devicons_column_length']
        self.enable_highlight = self.vim.vars[
            'defx_devicons_enable_syntax_highlight'
        ]
        self.directory_icon = self.vim.vars['defx_devicons_directory_icon']
        self.mark_icon = self.vim.vars['defx_devicons_mark_icon']
        self.parent_icon = self.vim.vars['defx_devicons_parent_icon']
        self.default_icon = self.vim.vars['defx_devicons_default_icon']

    def get(self, context: Context, candidate: dict) -> str:
        if 'mark' not in context.columns and candidate['is_selected']:
            return self.icon(self.mark_icon)

        if candidate.get('is_root', False):
            return self.icon(self.parent_icon)

        if candidate['is_directory']:
            return self.icon(self.directory_icon)

        path: Path = candidate['action__path']
        ext = path.suffix[1:].lower()
        filename = path.name.lower()

        for pattern, pattern_data in pattern_matches.items():
            if re.search(pattern, filename) is not None:
                return self.icon(pattern_data['icon'])

        if filename in exact_matches:
            return self.icon(exact_matches[filename]['icon'])

        if ext in extensions:
            return self.icon(extensions[ext]['icon'])

        return self.icon(self.default_icon)

    def length(self, context: Context) -> int:
        return self.column_length

    def icon(self, icon: str) -> str:
        return format(icon, f'<{self.column_length}')

    def highlight(self) -> None:
        self.vim.command((
            'syntax match {0}_{1} /[{2}]/ contained containedin={0}'
        ).format(self.syntax_name, 'devicon_mark', self.mark_icon))
        self.vim.command('highlight default link {0}_{1} Statement'.format(
            self.syntax_name, 'devicon_mark'
        ))

        if not self.enable_highlight:
            return

        self.vim.command((
            'syntax match {0}_{1} /[{2}]/ contained containedin={0}').format(
                self.syntax_name, 'directory', self.directory_icon
            ))
        self.vim.command('highlight default link {0}_{1} Directory'.format(
            self.syntax_name, 'directory'
        ))
#
        for pattern, pattern_data in pattern_matches.items():
            self.vim.command((
                'syntax match {0}_{1} /[{2}]/ contained containedin={0}'
            ).format(
                self.syntax_name, pattern_data['icon'], pattern_data['icon']))
            self.vim.command('highlight default {0}_{1} guifg=#{2}'.format(
                self.syntax_name, pattern_data['icon'], pattern_data['color']
            ))

        for exact_match_file, exact_match_data in exact_matches.items():
            self.vim.command((
                'syntax match {0}_{1} /[{2}]/ contained containedin={0}'
            ).format(self.syntax_name, exact_match_file,
                     exact_match_data['icon']))
            self.vim.command('highlight default {0}_{1} guifg=#{2}'.format(
                self.syntax_name, exact_match_file, exact_match_data['color']
            ))

        for ext, ext_data in extensions.items():
            self.vim.command((
                'syntax match {0}_{1} /[{2}]/ contained containedin={0}'
            ).format(self.syntax_name, ext, ext_data['icon']))
            self.vim.command('highlight default {0}_{1} guifg=#{2}'.format(
                self.syntax_name, ext, ext_data['color']
            ))
