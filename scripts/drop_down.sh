#!/bin/bash
tmux ls | grep termdrop

if [[ $? -eq 0 ]]
then
    kitty --class termdrop tmux attach -t termdrop -d
else
    tmux new-session -s 'termdrop' -d
    tmux send-keys -t termdrop "htop" c-m
    tmux split-window -h 'ipython'
    # tmux send-keys -t termdrop "mkdocs serve --dirty -a 0.0.0.0:8000" c-m
    tmux  new-window -t termdrop zsh
    # tmux command-prompt -t termdrop "set status off"
    # tmux send-keys -t termdrop c-m
    kitty --class termdrop tmux attach -t termdrop -d &
fi

