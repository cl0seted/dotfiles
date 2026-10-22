#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias l1='ls -1'
alias grep='grep --color=auto'
alias jctl_NM='sudo journalctl -u NetworkManager.service -f'
alias la='ls -la --color=auto'
alias prose0='scrcpy --audio-buffer=30 --no-video'
alias prose1='scrcpy --audio-buffer=30'
alias hyprexec='hyprctl dispatch exec'

alias tailson='tailstart && tailsup'
alias tailsoff='tailsdown && tailstop'
alias tailstatus='tailscale status'

alias tailsup='notify-send "Connecting to Tailscale" -t 1500 && sudo tailscale up'
alias tailsdown='notify-send "Disconnection from Tailscale" -t 1500 && sudo tailscale down'
alias tailstart='notify-send "Starting Tailscale Daemon" -t 1500 && sudo systemctl start tailscaled'
alias tailstop='notify-send "Stopping Tailscale Daemon" -t 1500 && sudo systemctl stop tailscaled'

alias xppen="systemctl restart --user xppentablet"


alias hddin='sudo mount /dev/sdb1 /mnt/extdrive'
alias hddout='sudo umount /dev/sdb1'

PS1='[\u@\h \W]\$ '



. "$HOME/.local/bin/env"
