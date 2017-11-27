#!/bin/sh
echo GENERATING raidreport.html

python ./city.py
python ./loadGyms.py
python ./gymsarr.py
python ./raidreport.py

echo DONE!!!!