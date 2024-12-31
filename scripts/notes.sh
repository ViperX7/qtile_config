#!/bin/bash
tmux ls | grep Notes

if [[ $? -eq 0 ]]
then
    kitty --class kittynotes tmux attach -t Notes -d
else
    tmux new-session -s 'Notes' -d
    tmux send-keys -t Notes "cd ~/blog" c-m
    tmux send-keys -t Notes "clear" c-m
    tmux send-keys -t Notes "pypy3 -m mkdocs serve --dirty -a 0.0.0.0:8000" c-m
    tmux  new-window -t Notes zsh
    tmux send-keys -t Notes "cd ~/blog/docs" c-m
    tmux send-keys -t Notes "nvim index.md" c-m
    # tmux command-prompt -t Notes "set status off"
    # tmux send-keys -t Notes c-m
    kitty --class kittynotes tmux attach -t Notes -d &
fi

