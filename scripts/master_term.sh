#!/bin/bash
tmux ls | grep Vterm

if [[ $? -eq 0 ]]
then
    kitty --class Vterm tmux attach -t Vterm -d
else
    tmux new-session -s 'Vterm' -d
    kitty --class Vterm tmux attach -t Vterm -d &
fi

