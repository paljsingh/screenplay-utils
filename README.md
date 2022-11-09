virtualenv venv
source venv/bin/activate

pip3 install git+https://github.com/paljsingh/txtmarker.git

./break-by-xxxxxx.sh infile.pdf NAME [NAME]...

example:
./break-by-character.sh test/2001-a-space-odyssey.pdf BOWMAN HAL POOLE

./break-by-location.sh test/2001-a-space-odyssey.pdf CENTRIFUGE "POD BAY"
