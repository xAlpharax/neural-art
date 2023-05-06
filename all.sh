#!/bin/bash

for style in Images/* ; do
    for content in Images/* ; do
        if [ $style != $content ] && [ ! -f $(basename ${content%.*})'_in_'$(basename ${style%.*})'.mp4' ]; then
            ./stylize.sh $style $content
        fi ; done ; done
