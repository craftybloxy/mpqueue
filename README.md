#history
28/04/24: I got no idea on how to run that app outside my virtual env..
28/04/24: added poetry

#bash script
```
#!/bin/bash
term_lines=$(tput lines)
while [ true ]; do
    python ./src/mpqueue_cli/main.py --length $term_lines
    clear
    echo mpd is down! restarting .
    sleep 1
    python ./src/mpqueue_cli/main.py --length $term_lines
    clear
    echo mpd is down! restarting ..
    sleep 1
done
```