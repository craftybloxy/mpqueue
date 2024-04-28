#!/bin/bash
term_lines=$(tput lines)
while [ true ]; do
    python ./mdqueue-cli/main.py --length $term_lines
    clear
    echo mpd is down! restarting .
    sleep 1
    python ./mdqueue-cli/main.py --length $term_lines
    clear
    echo mpd is down! restarting ..
    sleep 1
done
