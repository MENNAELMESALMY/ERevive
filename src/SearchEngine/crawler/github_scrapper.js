const fs = require('fs');
const { Octokit } = require("@octokit/core");

//change personal token
const octokit = new Octokit({ auth: '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' });
octokit.request.defaults({
    headers: {
        'Connection': 'keep-alive'
    }
});


async function getBulkPublicRepos(since) {
    return await octokit.request('GET /repositories',{
        since:since
    });
}

async function getStargazerCount(owner,repo){
    let stragerz=  await octokit.request('GET /repos/{owner}/{repo}',{
        owner:owner,
        repo:repo
    });
    return stragerz.data.stargazers_count;
}

async function downloadZipRepo(owner,repo) {
    let res = await octokit.request('GET /repos/{owner}/{repo}/zipball',{
        owner:owner,
        repo:repo
    });
    let arrayBuffer = res.data;
    downloadSaveZip(arrayBuffer,owner,repo);
}
function downloadSaveZip(arrayBuffer,owner,repo) {
    let buffer = Buffer.from(arrayBuffer);
    fs.writeFileSync(`./repos/${owner}_${repo}.zip`, buffer);
}
function downloadRepos() {
    let repos = fs.readFileSync('./repos.txt').toString().split('\n');
    for(let i = 0; i < repos.length; i++) {
        let repoUrl = repos[i];
        let owner= repoUrl.split('/')[3];
        let repoName = repoUrl.split('/')[4];
        downloadZipRepo(owner,repoName);
    }
}

async function saveBulkPublicRepos(data) {
    for(let i = 0; i < data.length; i++) {
        let repo = data[i];
        let repoUrl = repo.html_url;
        let owner= repoUrl.split('/')[3];
        let repoName = repoUrl.split('/')[4];
        let stragerzCount = await getStargazerCount(owner,repoName);
        if (stragerzCount > 20) {
            
            fs.appendFileSync('./repos.txt', repoUrl + '\n');
        }
    }

}
//write append to repos.txt file
reposFile = fs.open('./repos.txt', 'a', (err, file) => {
    if (err) throw err;
    console.log('The file has been saved!');
});

async function getAllPublicRepos(num) {
    
    while(true) {
        try{
        let result = await getBulkPublicRepos(num);
        if(result.data.length == 0) {
            fs.closeSync(reposFile);
            break;
        }
        //await downloadBulkPublicRepos(result.data);
        saveBulkPublicRepos(result.data);
        num += result.data.length;
        console.log(num);
    }
    catch(err) {
        //check if error is API rate limit
        if(err.status == 403) {
            console.log(err);
            waitForHour(num);
            break;
        }
    }
}
}

function waitForHour(num){
    setTimeout(() => {
        getAllPublicRepos(num);
    }
    , 3600000);
}

getAllPublicRepos(117000);
//downloadRepos();
