git clone https://github.com/denny0223/scrabble.git --quiet
cd scrabble
./scrabble https://edu-ctf.csie.org:44302
git checkout 2577aafa9bf476037cb011d59cf433d8a0c09c96 --quiet
cat admin_portal_non_production/.htpasswd
cd ..