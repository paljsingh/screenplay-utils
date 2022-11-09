#!/bin/bash

infile=$1
shift 1

basedir=$(dirname $infile)
for location in "$@"; do
    pages="$(pdfgrep -n -e "\<$location\>" "$infile" | cut -f1 -d ":" | uniq | tr '\n' ' ')"
    outfile="${basedir}/${location}-nonhl.pdf"
    outfile_hl="${basedir}/${location}.pdf"
    pdftk "$infile" cat $pages output "$outfile" && \
	    python3 ./highlight.py "$outfile" "$outfile_hl" "[^a-zA-Z]$location" -c "red" && \
	echo "$outfile_hl" && rm "$outfile"
done

