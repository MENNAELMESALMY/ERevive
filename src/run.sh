#kill port 5000 if it is running
sudo kill $(lsof -t -i:5000)
#run the server
python3 server.py &
#run the client
cd AppUI
npm run serve &