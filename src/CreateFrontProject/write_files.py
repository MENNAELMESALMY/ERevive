import json

from sklearn import cluster
from utils import *
from CreateVueApp.create_form import *
from CreateVueApp.create_routing import *
from CreateVueApp.create_store_idx import *
from CreateVueApp.create_dashboard import *
from CreateVueApp.create_cards import *
from CreateVueApp.create_store import *
from CreateVueApp.create_cards_designs import *
from CreateVueApp.create_dashboard_style import *
from CreateVueApp.create_large_cards import *
from CreateVueApp.create_large_card_style import *





appRoute = 'FrontCode/src/App.vue'
storeRoute = 'FrontCode/src/store/modules/'
storeRouteIdx = 'FrontCode/src/store/index.js'
routerRoute = 'FrontCode/src/router/index.js'
viewsRoute = 'FrontCode/src/views/'
componentsRoute = 'FrontCode/src/components/'
styleRoute = 'FrontCode/src/scss/'


f = open('systemInfo.json','r')
systemInfoObject = json.load(f)
f.close()
c={}
with open('../Application/clusters.json') as f:
    c = json.load(f)

tempC= {}
for key,value in c.items():
    tempC[key + "_cluster"] = value
c = tempC

cluster_names = list(c.keys())
clustersAndQueries = {}
AllQueries = []
for name in cluster_names:
  tempListGet = []
  templistAllQueries = []
  for query in c[name]:
    if (query["method"]) == "get":
      tempListGet.append(query["endpoint_name"])
    templistAllQueries.append(query)
  clustersAndQueries[name] = tempListGet
  AllQueries.append(templistAllQueries)


with open (appRoute, 'w') as f:
  f.write('''
<template>
      <router-view />
</template>

<script>
    export default{
   name: "app"
    };
</script>

<style lang='scss' scoped >
    #app {
    font-size: 18px;
    font-family: 'Roboto', sans-serif;
    }
</style>
  ''')


with open(viewsRoute + "home.vue", 'w') as f:
  f.write(f'''
<template>
  <div id="home">
   <div class="mainContent">
      <h2>Welcome to ERevive</h2>
      <h3>{systemInfoObject["systemName"]}</h3>
      <p>
        {systemInfoObject["systemDescription"]}
      </p>
      <router-link to="/App"><button>CONTINUE</button></router-link>
    </div>

    <div class="animation-area">
      <ul class="box-area">
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
      </ul>
    </div>
  </div>
</template>
''')
  f.write('''
<script>
export default {
  name: "home"
};
</script>

<style lang='scss' scoped >
.mainContent {
  width: 100%;
  position: absolute;
  text-align: center;
  z-index: 1;
}
.mainContent h2,
h3,
p {
  text-align: center;
  color: white;
}
.mainContent h2 {
  margin-top: 15%;
  font-size: 50px;
  margin-bottom: 0;
  padding: 10px;
}
.mainContent h3 {
  margin-top: 12px;
  font-size: 40px;
  padding: 10px;
  margin-bottom: 0;
}
.mainContent p {
  padding-left: 30%;
  padding-right: 30%;
  font-size: 18px;
}
.mainContent button {
  margin-top: 27px;
  margin-left: auto;
  text-align: center;
  background-color: white;
  border-radius: 25px;
  width: 22%;
  height: 50px;
  padding: 15px;
  font-size: 17px;
  font-weight: 700;
  border: none;
  cursor: pointer;
  letter-spacing: 1.8px;
  box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease 0s;
   &:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
  }
}
.animation-area {
  background: linear-gradient(to left, #ffc809, #0f1136);
  width: 100%;
  height: 100vh;
}
.box-area {
  position: absolute;
  padding: 0;
  margin: 0;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
}
.box-area li {
  position: absolute;
  display: block;
  list-style: none;
  width: 25px;
  height: 25px;
  background: rgba(255, 255, 255, 0.2);
  animation: animate 20s linear infinite;
  bottom: -150px;
}
.box-area li:nth-child(1) {
  left: 86%;
  width: 80px;
  height: 80px;
  animation-delay: 0s;
}
.box-area li:nth-child(2) {
  left: 12%;
  width: 30px;
  height: 30px;
  animation-delay: 1.5s;
  animation-duration: 10s;
}
.box-area li:nth-child(3) {
  left: 70%;
  width: 100px;
  height: 100px;
  animation-delay: 5.5s;
}
.box-area li:nth-child(4) {
  left: 42%;
  width: 150px;
  height: 150px;
  animation-delay: 0s;
  animation-duration: 15s;
}
.box-area li:nth-child(5) {
  left: 65%;
  width: 40px;
  height: 40px;
  animation-delay: 0s;
}
.box-area li:nth-child(6) {
  left: 15%;
  width: 110px;
  height: 110px;
  animation-delay: 3.5s;
}
@keyframes animate {
  0% {
    transform: translateY(0) rotate(0deg);
    opacity: 1;
  }
  100% {
    transform: translateY(-800px) rotate(360deg);
    opacity: 0;
  }
}
</style>
    ''')

with open(viewsRoute + "main_page.vue", 'w') as f:
  f.write('''
<template>
    <div class="mainPage">
        <div class="content">
          <div class="sidebar">
            <sideBar />
          </div>
          <div class="rightContent">
          <router-view />
          </div>
        </div>
    </div>
</template>

<script>
import sideBar from '../components/sideBar.vue';
export default {
    name: "mainPage",
    components: {
        sideBar,
    }
};
</script>

<style lang="scss" scoped>
.content{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
.rightContent{
    width: calc(100% - 370px);
    height: 100%;
    min-height:100vh;
}
</style>
  ''')

with open(componentsRoute + "queryCard.vue", 'w') as f:
  f.write('''
<template>
  <div class="queryCard">
    <router-link :to="'/App/' + clusterName + '_' + queryName">
      <div class="content">
        <h3>{{ queryName }}</h3>
      </div>
    </router-link>
  </div>
</template>

<style lang="scss" scoped>
.queryCard{
  width: 80%;
  padding: 10px;
  margin: 30px;
  margin-left: 100px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  cursor: pointer;
  transition: all 0.3s ease 0s;
  &:hover {
  transform: translateY(-3px);
  }
  .content{
      width: 100%;
      height: 100%;
      h3{
          font-size: 25px;
          font-weight: 700;
          color: #0f1136;
          word-wrap: break-word;
          width: 100%;
          height: 100%;
      }
  }
}
a{
  text-decoration: none;
}
</style>

<script>
export default {
    name: "queryCard",
    props:{
        queryName: {
            type: String,
            required: true
        },
        clusterName: {
            type: String,
            required: true
        }
    },
};
</script>
  ''')


for cluster_name in cluster_names:
  with open(viewsRoute + cluster_name +".vue", 'w') as f:
    f.write('''
<template>
    <div class="''' + cluster_name + '''">
      <div class="title">''' + cluster_name.replace("_cluster","").replace("_"," ") + '''</div>
      <query-card v-for="(query, i) in queries" :key="i" :queryName="query" clusterName="''' + cluster_name + '''" />
      <router-link to="/App/post_''' + cluster_name +'''">
        <button class="addBtn">Add Object</button>
      </router-link>
    </div>
</template>

<script>
import queryCard from '../components/queryCard.vue';
export default {
    name:"'''+ cluster_name +'''",
    data(){
      return{
        ''' + f'''
        queries:  {clustersAndQueries[cluster_name]} ''' + '''
      }
    },
    components: {
      queryCard,
  },
    };
</script>

<style lang="scss" scoped>
.''' + cluster_name + '''{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
}
.title{
  font-size: 40px;
  font-weight: 700;
  margin-top: 30px;
  margin-bottom: 20px;
  color: #0f1136;
}
.addBtn{
  width: 100%;
  background-color: #0f1136;
  color: white;
  font-size: 18px;
  padding: 14px 20px;
  margin: 17px 20px 50px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  &:hover {
    background-color: #ffc809;
    transform: scale(1.05);
  }
}
</style>
    ''')

with open(componentsRoute + "sideBar.vue", 'w') as f:
  f.write(f'''
<template>
  <div class="sideBar">
    <div class="header">
      <h4>{systemInfoObject["systemName"]}</h4>
    </div>
  ''')
  f.write('''
    <ul class="clutsers">
      <li v-for="(card, i) in clustersNames" :key="i" class="cluster">
      <router-link :to="'/App/' + card">
        <div class="clusterName" :title="card" :id="'clustersID' + i">
           {{ card.replace("_cluster","").replace("_"," ") }}
        </div>
      </router-link>
      </li>
    </ul>
    <div class="footer">
      <h5>ERevive 2022</h5>
    </div>
  </div>
</template>

<script>
export default{
    data() {
        return {
''')
  f.write(f'''
        clustersNames: {cluster_names},
        ''')
  f.write('''
        };
    },
};
</script>

<style lang="scss" scoped>
.sideBar {
  color: white;
  background-color: #0f1136;
  float: left;
  width: 350px;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  bottom: 0;
  padding: 0.5em;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  overflow-x: hidden;
  scrollbar-width: thin;
  scrollbar-color: #0f1136 #0f1136;
  &::-webkit-scrollbar {
    width: 1px;
  }
  &::-webkit-scrollbar-track {
    background-color: #0f1136;
  }
  &::-webkit-scrollbar-thumb {
    background-color: #0f1136;
  }
}
.header,
.footer {
  text-align: center;
  font-weight: 700;
  font-size: 25px;
  word-wrap: break-word;
}
.clutsers {
  padding-top: 10px;
  padding-left: 5px;
}
.cluster {
  margin: 0;
  padding: 0;
  padding-left: 5px;
  list-style: none;
  padding-top: 5px;
  padding-bottom: 10px;
  a {
    color: white;
    text-decoration: none;
  }
}
.clusterName {
  font-size: 25px;
  word-wrap: break-word;
  font-weight: 700;
  color: white;
  padding-top: 15px;
  padding-bottom: 15px;
  padding-left: 5px;
  padding-right: 5px;
  width: 90%;
  cursor: pointer;
  &:hover {
    background-color: rgb(200, 206, 206, 0.1);
    border-radius: 7px;
  }
}
</style>
  ''')

with open(componentsRoute + "navBar.vue", 'w') as f:
  f.write('''
<template>
  <div class="navBar">
      <div class="trashIcon">
          <i class="fa fa-trash" aria-hidden="true"></i>
      </div>
      <div class="editIcon">
          <i class="fa fa-edit"></i>
      </div>
      <div class="postButton">
          <button>+ POST</button>
      </div>
  </div>    
</template>

<script>
export default {
    name:"navBar"
}
</script>

<style lang="scss" scoped>
.navBar{
    display:flex;
    justify-content:space-between;
    width: 100%;
    padding-left: 35px;
    padding-top: 35px;
}
.postButton{
    padding-top: 3px;
    button{
        background-color: #ffc809;
        width: 100px;
        color: #0f1136;
        border: none;
        border-radius: 5px;
        padding: 10px;
        font-size: 20px;
        font-weight: bold;
        cursor: pointer;
        box-shadow: 0 0 2px rgba(0,0,0,0.5);
        transition: all 0.3s ease 0s;
        &:hover {
            transform: translateY(-3px);
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.5);
            background-color: #0f1136;
            color: #ffc809;
        }
    }
}
.trashIcon, .editIcon{
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background-color: #0f1136;
    color: #ffc809;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.5);
    transition: all 0.3s ease 0s;
    &:hover{
        transform: translateY(-3px);
        background-color: #ffc809;
    }
    i{
        font-size: 30px;
        padding: 9px;
        color: #ffc809;
        cursor: pointer;
        &:hover{
            color: #0f1136;
        }
    }
}
.trashIcon{
    i{
        padding: 9px;
        padding-left: 12px;
    }
}
</style>
  ''')

generate_routing(cluster_names,AllQueries,routerRoute)

generate_store_idx(cluster_names,storeRouteIdx)

for clusterName,endpoints in c.items():
  generate_store(endpoints,storeRoute+clusterName+'.js')


requirments = [
    {
        "field_name": "First Name",
        "field_type": "text",
        "isRequired": True,
        "maxRange": 0,
        "minRange": 0,
        "options": []
    },
    {
        "field_name": "Last Name",
        "field_type": "text",
        "isRequired": True,
        "maxRange": 0,
        "minRange": 0,
        "options": []
    },
    {
        "field_name": "Email",
        "field_type": "email",
        "isRequired": True,
        "maxRange": 0,
        "minRange": 0,
        "options": []
    },
    {
        "field_name": "Phone Number",
        "field_type": "tel",
        "isRequired": True,
        "maxRange": 0,
        "minRange": 0,
        "options": []
    },
    {
        "field_name": "Password",
        "field_type": "password",
        "isRequired": True,
        "maxRange": 0,
        "minRange": 0,
        "options": []
    },
    {
        "field_name": "Github Url",
        "field_type": "url",
        "isRequired": True,
        "maxRange": 0,
        "minRange": 0,
        "options": []
    },
    {
        "field_name": "Age",
        "field_type": "number",
        "isRequired": True,
        "maxRange": 40,
        "minRange": 18,
        "options": []
    },
    {
        "field_name": "Gender",
        "field_type": "radiobutton",
        "isRequired": True,
        "maxRange": 0,
        "minRange": 0,
        "options": ["Male","Female"]
    },
    {
        "field_name": "Subjects",
        "field_type": "list",
        "isRequired": True,
        "maxRange": 0,
        "minRange": 0,
        "options": ["Math","Physics","Machine Learning","Data Science"]
    },
    {
        "field_name": "Languages",
        "field_type": "checklist",
        "isRequired": False,
        "maxRange": 0,
        "minRange": 0,
        "options": ["Arabic","English","French"]
    },
    {
        "field_name": "Description",
        "field_type": "textarea",
        "isRequired": False,
        "maxRange": 0,
        "minRange": 0,
        "options": []
    },
    {
        "field_name": "Birth Date",
        "field_type": "date",
        "isRequired": False,
        "maxRange": 0,
        "minRange": 0,
        "options": []
    }
]


f = open('userInterfaceInfo.json','r')
requirments = json.load(f)
f.close()

for cluster_name,endpoints in c.items():
  get_endpoint = "get_"+ cluster_name.replace("_cluster","").lower()
  delete_endpoint=''
  put_endpoint=''
  pks=[]
  for endpoint in endpoints:
    if endpoint["method"] == "delete": 
      delete_endpoint = endpoint["endpoint_name"]
      pks = endpoint["queryParams"]
    elif endpoint["method"] == "put": 
      put_endpoint = endpoint["endpoint_name"]
  for endpoint in endpoints:
    is_single_entity = endpoint['is_single_entity']
    filePath = componentsRoute + endpoint["endpoint_name"] + ".vue"
    if endpoint["method"] == "get":
      if len(endpoint["response"]) < 9:
        generate_dashboard(cluster_name,endpoint, filePath,is_single_entity,delete_endpoint,put_endpoint,pks)
      else:
        generate_large_cards(cluster_name,endpoint, filePath,is_single_entity,delete_endpoint,put_endpoint,pks)
 
    elif endpoint["method"] == "post":
      if is_single_entity:
        temp_cluster_name = cluster_name.replace("_cluster","")
        createForm(requirments,temp_cluster_name,endpoint, filePath,False,get_endpoint,[])
      else:
        with open(filePath, 'a') as file: 
          file.write('''
<template>
    <div class="form"></div>
</template>

<style></style>

<script>
export default {
    name:"form"
}
</script>
        ''')

    elif endpoint["method"] == "put":
      filePath = componentsRoute + endpoint["endpoint_name"] + ".vue"
      if is_single_entity:
        temp_cluster_name = cluster_name.replace("_cluster","")
        createForm(requirments,temp_cluster_name,endpoint, filePath,True,get_endpoint,pks)
      else:
        with open(filePath, 'a') as file: 
          file.write('''
<template>
    <div class="form"></div>
</template>

<style></style>

<script>
export default {
    name:"form"
}
</script>
        ''')

with open('FrontCode/src/index.html', 'w') as f:
    f.write('''
<html>
  <head>
    <title>Vue App</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"></link>
  </head>
  <body>
    <div id="app"></div>
  </body>
</html>

<style>
  body{
    margin: 0;
    padding: 0;
  }
</style>
    ''')

with open('FrontCode/src/main.js', 'w') as f:
    f.write('''
import {createApp} from 'vue';
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";

axios.defaults.baseURL = "http://localhost:'''+systemInfoObject["port"]+'''/api/";
createApp(App).use(router).use(store).mount('#app');

//new Vue({
//  router,
//  store,
//  render: (h) => h(App),
//}).$mount("#app");
    ''')


with open('FrontCode/.babelrc.js', 'w') as f:
    f.write('''
module.exports = {
  presets: ['@babel/preset-env'],
}
    ''')

with open('FrontCode/webpack.config.js', 'w') as f:
    f.write('''
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { VueLoaderPlugin } = require('vue-loader');
const webpack  = require('webpack');

module.exports = {
  entry: './src/main.js',
  module: {
    rules: [
      { test: /\.js$/, use: 'babel-loader' },
      { test: /\.vue$/, use: 'vue-loader' },
      { test: /\.scss$/, use: ['vue-style-loader','css-loader','sass-loader']},
    ]
  },
  devServer: {
    open: true,
    hot: true,
    historyApiFallback: true
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html',
    }),
    new VueLoaderPlugin(),
    new webpack.HotModuleReplacementPlugin(),
  ]
};
    ''')


f = open('FrontCode/package.json', 'r+') 
l = f.read()
f.close()
x = '"test": "echo \\"Error: no test specified\\" && exit 1"'
y = '"serve": "webpack-dev-server --mode development"'
l = l.replace(x, y)
f = open('FrontCode/package.json', 'w') 
f.write(l)
f.close()
print("Text successfully replaced")

create_card_design1(componentsRoute + "cardDesign1.vue")
create_card_design2(componentsRoute + "cardDesign2.vue")
create_card_design3(componentsRoute + "cardDesign3.vue")
create_card_design4(componentsRoute + "cardDesign4.vue")
create_color_pallete(componentsRoute + "colorPallete.vue")
create_color_pallete_module(storeRoute + "color_pallete.js")
create_dashboard_style(styleRoute+'_dashboard.scss')
create_large_card_style(styleRoute+'_big_card.scss')





