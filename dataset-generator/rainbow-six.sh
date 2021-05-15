#!/bin/bash

# This script generate uniform pictures with a random color

# Options
dst="/opt/dataset-simple-1000/cover-images"
nb=1000

date=$(date)
mkdir -p $dst
time for i in $(seq -w $nb); do
    # 3 byte hex color
    color=$(openssl rand -hex 3)

    echo "[$i/$nb] Creating $i.png with color $color"
    convert "xc:#$color[512x512]" -colorspace RGB $dst/$i.png
done

echo
echo "[Start] $date"
echo "[ End ] $(date)"
echo
