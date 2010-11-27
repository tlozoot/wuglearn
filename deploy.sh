#! /bin/sh

ssh -T jon-levine.com <<\EOI

cd wuglearn/
git checkout .
git pull
ps -e | grep python | egrep -o '^[0-9]*' | xargs kill
nohup python server.py &

exit

EOI