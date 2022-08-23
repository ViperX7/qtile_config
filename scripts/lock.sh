#!/bin/bash

betterlockscreen -l &
betterlockscreen -u ~/wall/`ls ~/wall/|sort -R|tail -n1` --fx blur
