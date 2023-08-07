sudo kill $(lsof -t -i:5000)
sudo kill $(lsof -t -i:8080)

if [ ! -d "SearchEngine/nGrams" ]; then
    unzip -d /SearchEngine SearchEngine/nGrams.zip
fi

python3 server.py &

cd AppUI
if [ ! -d "AppUI/node_modules" ]; then
    npm i
fi
npm run serve &
