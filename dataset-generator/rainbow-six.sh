#!/bin/bash

# This script generate uniform pictures with a random color

# Options
dst="/opt/dataset-simple-blackwhite/cover-images"
nb=10

date=$(date)
mkdir -p $dst
time for i in $(seq -w $nb); do
    # 3 byte hex color
    # color=$(openssl rand -hex 3)
    color=abcdef

    echo "[$i/$nb] Creating $i.png with color $color"
    convert -size 256x256 "xc:#$color" -depth 16 -colorspace RGB $dst/$i.png
done

echo
echo "[Start] $date"
echo "[ End ] $(date)"
echo
