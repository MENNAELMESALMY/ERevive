sudo kill $(lsof -t -i:5000)
sudo kill $(lsof -t -i:8080)

if [ ! -f "SearchEngine/nGrams/ngrams.pickle" ]; then
    cd SearchEngine/nGrams
    unzip nGrams.zip
    cd ./../..
fi

. venv/bin/activate

python3 -m spacy download en_core_web_sm

python3 server.py &

cd AppUI
if [ ! -d "AppUI/node_modules" ]; then
    npm i
fi
npm run serve &
