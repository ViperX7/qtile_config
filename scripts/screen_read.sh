#!/bin/env bash

tmpfile="/tmp/snap.$RANDOM"
flameshot gui --raw >"$tmpfile"

txt=$(tesseract $tmpfile stdout)
echo "$txt"
echo "$txt" | xclip

notify-send.py "Copied to clipboard"

rm $tmpfile
