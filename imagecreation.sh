#!/bin/bash

VERBOSE=false;

WORDS="$1";
IMAGE="$2";
DONE="$3";

if [ "$VERBOSE" = true ] ; then
	echo "Start Conversion"
fi

if [ "$VERBOSE" = true ] ; then
	echo "Creating Words"
fi
convert -size 1000x380 -background transparent -font DroidSansMono -weight Bold -density 90 caption:"$WORDS" words.png

if [ "$VERBOSE" = true ] ; then
	echo "Creating White"
fi
convert -size 1000x380 xc:white white.png

if [ "$VERBOSE" = true ] ; then
	echo "Resizing $IMAGE"
fi
convert $IMAGE -resize 300x image-resized.png

if [ "$VERBOSE" = true ] ; then
	echo "Combining white and $IMAGE"
fi
composite -blend 50 -gravity east image-resized.png white.png image-combined.png

if [ "$VERBOSE" = true ] ; then
	echo "Combining words and new $IMAGE"
fi
composite words.png image-combined.png $DONE

if [ "$VERBOSE" = true ] ; then
	echo "Cleaning Up"
fi
rm words.png image-combined.png image-resized.png white.png

if [ "$VERBOSE" = true ] ; then
	echo "Done"
fi