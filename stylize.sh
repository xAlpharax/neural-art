#!/bin/zsh

### You must be in the 'neural-art' directory when you run this

if [ $# -eq 0 ]
  then
    echo "Style Image and Content Image need to be specified as arguments"
    echo "Example: ./stylize.sh Images/Jitter_Doll.jpg Images/cute.jpg"
    exit 1
fi

if [ $# -eq 1 ]
  then
    echo "Content image needs to be specified"
    exit 1
fi

# stylize data [pair (style, content)]
python neuralart.py $1 $2

# render images (actual frames) from (an) images.npy
python renderer.py $1 $2

# turn everything into a video
ffmpeg -framerate 60 -pattern_type glob -i 'Output/neural_art_*.png' -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" ${${2/*\/}/.*}_in_${${1/*\/}/.*}.mp4
