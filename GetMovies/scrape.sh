#!/bin/sh
cat meta.txt | sed -rn 's|^.*<a href="/movie/(.*)">(.*)</a>.*$|\1#\2|p'
