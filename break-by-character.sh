#!/bin/bash

infile=$1
shift 1
basedir=$(dirname $infile)
for char in "$@"; do
    pages="$(pdfgrep -n -i -e "\<$char\>" "$infile" | cut -f1 -d ":" | uniq | tr '\n' ' ')"
    outfile="${basedir}/${char}-nonhl.pdf"
    outfile_hl="${basedir}/${char}.pdf"
    pdftk "$infile" cat $pages output "$outfile" && \
    python3 ./highlight.py "$outfile" "$outfile_hl" "[^a-zA-Z\n]$char[^a-zA-Z\n]|^$char|$char$" -i -m -c "yellow" && \
	echo "$outfile_hl" && rm "$outfile"
done

