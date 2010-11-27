#! /bin/sh

ssh -T dailyoperations@phonetics.fas.harvard.edu <<\EOI

cd wuglearn/
git checkout .
git pull
exit

EOI