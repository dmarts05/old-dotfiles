set fish_greeting ""
set -x SSH_AUTH_SOCK $XDG_RUNTIME_DIR/ssh-agent.socket

# Colors

set fish_color_normal brblue
set fish_color_autosuggestion '#7d7d7d'
set fish_color_command brblue
set fish_color_error '#ff6c6b'
set fish_color_param brcyan


# Aliases

alias grep "grep --color=auto"
alias cat "bat --style=plain --paging=never"
alias ls "exa --group-directories-first"
alias tree "exa -T"
alias dotfiles "git --git-dir $HOME/.dotfiles/ --work-tree $HOME"
alias mirror "sudo reflector --save /etc/pacman.d/mirrorlist --protocol https --country Germany --latest 10 --sort rate"
alias orphans "sudo pacman -Rns (pacman -Qqtd)"

# Abbreviations

abbr p "sudo pacman"
abbr SS "sudo systemctl"

# Prompt

starship init fish | source
