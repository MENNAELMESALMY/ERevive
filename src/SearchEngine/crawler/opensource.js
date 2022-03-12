process.env.NODE_TLS_REJECT_UNAUTHORIZED='0'
const fetch = require('node-fetch')
const fs = require('fs');   
opensourceFile = fs.createWriteStream(`./opensource.txt`);
async function getAllSqlSearch() { 
    url = "https://searchcode.com/api/codesearch_I/?q=SELECT&lan=37"
    max_page = 49;
    for(let i = 0; i <= max_page; i++) {  
        response = await fetch(url + "&p=" + i);
        data = await response.json();
        results = data.results; 
        for(let j = 0; j < results.length; j++) {
            opensourceFile.write(JSON.stringify(results[j]) + "\n");
        }
    }
}
getAllSqlSearch()


