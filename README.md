# __RacingLineinator__
This repository aims to calculate the ideal racing line of any given track. Ways of achieving this will be discussed below.

## Methods
1. Reading geospatial data from open-source sites to obtain the satellite imagery of the track.
2. Using object detection to find the extent of the track inside the image (This step eases the heavy calculation).
3. Using instance segmentation on cropped satellite imagery to draw the racing track.
4. Doing normalization on the obtained data to achieve the best results.
5. Doing mathematical calculations -as explained in the paper- to find the racing line.

## Research Paper
As of now, the paper is not published.
It can be found on the following link: https://docs.google.com/document/d/17AolFfOulLF-DohZUfYPa1hk0Vbyj0CiuKn-bftANhQ/edit?usp=sharing
