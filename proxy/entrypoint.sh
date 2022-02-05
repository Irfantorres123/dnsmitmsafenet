#!/bin/bash
mitmdump -p 443 -s anatomy.py --mode reverse:http://example.com/ --set keep_host_header &
P1=$!
mitmdump -p 80 --mode reverse:http://localhost:443/ &
P2=$!
wait $P1 $P2