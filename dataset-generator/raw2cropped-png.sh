#!/bin/bash

# Lancer depuis le dossier contenant les images RAW
dst="/opt/dataset/cover-images"

nb=1
tot=$(ls -1 | wc -l)
date=$(date)

mkdir -p $dst
time for file in *.dng; do
    file=${file%.*}

    echo -n "[$nb/$tot] converting ${file} ... "
    dcraw -c -w ${file}.dng | pnmtopng > $dst/${file}.png

    echo "and cropping"
    # https://infoheap.com/crop-image-using-imagemagick-convert/
    # keep original png, uncomment only for tests
    # cp $dst/${file}.png $dst/${file}_orig.png
    X=$(identify -format '%[fx:w/4]' $dst/${file}.png)
    Y=$(identify -format '%[fx:h/4]' $dst/${file}.png)
    mogrify -crop 512x512+$X+$Y $dst/${file}.png

    nb=$((nb+1))
done

echo
echo "[Start] $date"
echo "[ End ] $(date)"
