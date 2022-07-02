import json
from utils import *
from CreateVueApp.create_form import *
from CreateVueApp.create_routing import *
from CreateVueApp.create_store_idx import *
from CreateVueApp.create_dashboard import *
from CreateVueApp.create_cards import *
from CreateVueApp.create_store import *
from CreateVueApp.create_cards_designs import *



appRoute = 'FrontCode/src/App.vue'
storeRoute = 'FrontCode/src/store/modules/'
storeRouteIdx = 'FrontCode/src/store/index.js'
routerRoute = 'FrontCode/src/router/index.js'
viewsRoute = 'FrontCode/src/views/'
componentsRoute = 'FrontCode/src/components/'

# appRoute = '../gpinterface/src/App.vue'
# storeRoute = '../gpinterface/src/store/modules/'
# storeRouteIdx = '../gpinterface/src/store/index.js'
# routerRoute = '../gpinterface/src/router/index.js'
# viewsRoute = '../gpinterface/src/views/'
# componentsRoute = '../gpinterface/src/components/'

# c = {
#   "c1":[
#     {
#       "url":"",
#       "method":"get",
#       "query_params":[
#         ("course_name","str","like","max"),
#         ("course_id","int","=","avg")
#       ],
#       "body_params":[
#         "name","bday"
#       ],
#       "path_params":[
#         "course_path"
#       ],
#       "response":{
#         "field1":"value1",
#         "field2":"value2",
#         "field3":"value3",
#         "field4":"value4",
#         "field5":"value5",
#         "field6":"value6"
#       },
#       'endpoint_name':'endpoint_name1',
#     },
#     {
#       "url":"",
#       "method":"get",
#       "query_params":[
#         ("course_name","str","like","max"),
#         ("course_id","int","=","avg")
#       ],
#       "body_params":[
#         "name","bday"
#       ],
#       "path_params":[
#         "course_path"
#       ],
#       "response":{
#         "field1":"value1",
#         "field2":"value2",
#         "field3":"value3",
#         "field4":"value4",
#         "field5":"value5",
#         "field6":"value6"
#       },
#       'endpoint_name':'endpoint_name2'
#     },
#     {
#       "url":"",
#       "method":"post",
#       "query_params":[
#         ("course_name","str","like","max"),
#         ("course_id","int","=","avg")
#       ],
#       "body_params":[
#         "name","bday"
#       ],
#       "path_params":[
#         "course_path"
#       ],
#       "response":{
#         "field1":"value1",
#         "field2":"value2"
#       },
#       'endpoint_name':'endpoint_name3'
#     },
#     {
#       "url":"",
#       "method":"get",
#       "query_params":[
#         ("course_name","str","like","max"),
#         ("course_id","int","=","avg")
#       ],
#       "body_params":[
#         "name","bday"
#       ],
#       "path_params":[
#         "course_path"
#       ],
#       "response":{
#         "field1":"value1",
#         "field2":"value2"
#       },
#       'endpoint_name':'endpoint_name4'
#     }
#   ],
#   "c2":[
#     {
#       "url":"",
#       "method":"post",
#       "query_params":[
#         ("course_name","str","like","max"),
#         ("course_id","int","=","avg")
#       ],
#       "body_params":[
#         "name","bday"
#       ],
#       "path_params":[
#         "course_path"
#       ],
#       "response":{
#         "field1":"value1",
#         "field2":"value2"
#       },
#       'endpoint_name':'endpoint_name5'
#     },{
#       "url":"",
#       "method":"get",
#       "query_params":[
#         ("course_name","str","like","max"),
#         ("course_id","int","=","avg")
#       ],
#       "body_params":[
#         "name","bday"
#       ],
#       "path_params":[
#         "course_path"
#       ],
#       "response":{
#         "field1":"value1",
#         "field2":"value2",
#         "field3":"value3",
#         "field4":"value4",
#         "field5":"value5",
#         "field6":"value6"
#       },
#       'endpoint_name':'endpoint_name6'
#     }
#   ]
# }
# open file clusters.json
systemInfoObject = {
    "system_name": "Learning Management System",
    "system_description": '''sum is simply dummy text of the printing and typesetting industry. Lorem
        Ipsum has been the industry's standard dummy text ever since the 1500s,
        when an unknown printer took a galley of type and scrambled it to make a
        type specimen book. It has survived not only five centuries.'''
}
c={}
with open('../Application/api/clusters.json') as f:
    c = json.load(f)

cluster_names = list(c.keys())
clustersAndQueries = []
AllQueries = []
for name in cluster_names:
  tempListGet = []
  templistAllQueries = []
  for query in c[name]:
    if (query["method"]) == "get":
      tempListGet.append(query["endpoint_name"])
    templistAllQueries.append(query["endpoint_name"])
  clustersAndQueries.append(tempListGet)
  AllQueries.append(templistAllQueries)


#create application
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


#create home
with open(viewsRoute + "home.vue", 'w') as f:
  f.write(f'''
<template>
  <div id="home">
   <div class="mainContent">
      <h2>Welcome to ERevive</h2>
      <h3>{systemInfoObject["system_name"]}</h3>
      <p>
        {systemInfoObject["system_description"]}
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

#creating the main page
with open(viewsRoute + "main_page.vue", 'w') as f:
  f.write('''
<template>
    <div class="mainPage">
        <div class="content">
          <div class="sidebar">
            <sideBar />
          </div>
          <div class="rightContent">
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
    justify-content: space-around;
}
</style>
  ''')

#create SideBar
with open(componentsRoute + "sideBar.vue", 'w') as f:
  f.write(f'''
<template>
  <div class="sideBar">
    <div class="header">
      <h4>{systemInfoObject["system_name"]}</h4>
    </div>
  ''')
  f.write('''
    <ul class="clutsers">
      <li v-for="(card, i) in clustersNames" :key="i" class="cluster">
        <div class="clusterName" :id="'clustersID' + i" @click="openClusterQueries('clustersID' + i,'queriesID' + i)">
           {{ card.substring(0, 19) + "..." }}
        </div>
        <ul class="queries" :id="'queriesID' + i">
          <li v-for="(item, j) in clusters[i]" :key="j" class="query">
            <router-link :to="item">
              <span class="queryName">{{ item.substring(0, 19) + "..."}}</span>
            </router-link>
          </li>
        </ul>
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
        clusters: {clustersAndQueries},
        ''')
  f.write('''
        };
    },
    methods: {
    openClusterQueries(clusterid,queryid) {
      if (document.getElementById(queryid).style.display == "none"){
        document.getElementById(queryid).style.display = "block";
        document.getElementById(clusterid).style.backgroundColor = "rgba(200,206,206,0.1)";
        document.getElementById(clusterid).onmouseover = function() {
          document.getElementById(clusterid).style.backgroundColor = "rgba(200,206,206,0.1)";
        }
        document.getElementById(clusterid).onmouseout = function() {
          document.getElementById(clusterid).style.backgroundColor = "rgba(200,206,206,0.1)";
        }
      }else{
        document.getElementById(queryid).style.display = "none";
        document.getElementById(clusterid).style.backgroundColor = "#0f1136";
        document.getElementById(clusterid).onmouseover = function() {
          document.getElementById(clusterid).style.backgroundColor = "rgba(200,206,206,0.1)";
        }
        document.getElementById(clusterid).onmouseout = function() {
          document.getElementById(clusterid).style.backgroundColor = "#0f1136";
        }
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.sideBar {
  color: white;
  background-color: #0f1136;
  float: left;
  width: 230px;
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
}
.clutsers,
.queries {
  margin: 0;
  padding: 0;
}
.clutsers {
  padding-top: 20px;
}
.queries {
  margin-top: 15px;
  margin-bottom: 15px;
  display: none;
  transition: all 0.4s ease;
}
.cluster,
.query {
  margin: 0;
  padding: 0;
  padding-left: 5px;
  list-style: none;
  padding-top: 5px;
  padding-bottom: 10px;
  a {
    color: white;
    text-decoration: none;
    padding-left: 10px;
  }
}
.clusterName {
  font-size: 16px;
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
.query {
  padding-top: 12px;
  width: 90%;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  &:hover {
    background-color: rgb(200, 206, 206, 0.1);
  }
}
</style>
  ''')

#create navbar
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

#create router
generate_routing(cluster_names,AllQueries,routerRoute)

#create store idx
generate_store_idx(cluster_names,storeRouteIdx)

#create store
for clusterName,endpoints in c.items():
  generate_store(endpoints,storeRoute+clusterName+'.js')


# create views
for cluster_name,endpoints in c.items():
  with open(f"{viewsRoute}/{cluster_name}_view.vue", 'w') as f:
    f.write('''
<template>
    <div>
    ''')
    for endpoint in endpoints:
      f.write(f'''
      <{endpoint["endpoint_name"].replace('_','-')}/>
      ''')
    f.write('''
    </div>
</template>

    <style lang="scss" scoped>
    .home {
    padding: 30px;
    }
    </style>

    <script>
    ''')
    for i in endpoints:
      f.write(f'''
      import {convertToCamelCase(i['endpoint_name'])} from '../components/{i['endpoint_name']}.vue'
      ''')
    f.write('''
export default {
  components: {
    ''')
    for i in endpoints:
      f.write(f'''
      {convertToCamelCase(i['endpoint_name'])},
      ''')
    f.write('''
  },
};
</script>
    ''')
  
#### to be deleted ####
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
##########################

# create components
for cluster_name,endpoints in c.items():
  for endpoint in endpoints:
    filePath = componentsRoute + endpoint["endpoint_name"] + ".vue"
    if endpoint["method"] == "get":
      if len(endpoint["response"]) > 5:
        generate_dashboard(cluster_name,endpoint, filePath)
      else:
        generate_cards(endpoint, filePath)
    elif endpoint["method"] == "post":
      createForm(requirments,endpoint, filePath)

#Index code generation
with open('FrontCode/src/index.html', 'w') as f:
    f.write('''
<html>
  <head>
    <title>Vue Hello World</title>
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

# create main
with open('FrontCode/src/main.js', 'w') as f:
    f.write('''
import {createApp} from 'vue';
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";

axios.defaults.baseURL = "http://localhost:3000/api/";
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

### create cards designs
create_card_design1(componentsRoute + "cardDesign1.vue")
create_card_design2(componentsRoute + "cardDesign2.vue")
create_card_design3(componentsRoute + "cardDesign3.vue")
create_card_design4(componentsRoute + "cardDesign4.vue")
create_color_pallete(componentsRoute + "colorPallete.vue")
create_color_pallete_module(storeRoute + "color_pallete.js")

# '''
# list of apis:
#   app/home -> card/clusters -> route(-------) to cluster view(each of them has get/post/put/delete)
#   view -> iterate over all apis and generate components(card button convert to delete)
#   store -> modules ()
#   (url, method)

#   query1:{
#     url:jjjj,
#     method:kkk,
#   }
# '''
#getClusterNames()

'''
1- read json file
2- made requirements object and other demo object for some requests
3- connect form, cards, complete function create cards
4- design project interface
5- implement project interface
6- implement validation interface
7- connect validation object as the requirements object
8- complete and integrate put and delete
9- fix style of every thing
10- how to make this folder be downloaded
'''

'''
entity (check name)
        ,attributes(change name(ocr)or change (data types) ,requirement
        or input field type or add new attribute)
        ,relationships(change name 
        or add new relationship or check cardinality and participation)
'''

# creating app

'''
sql (schema/queries)[ edit query/add query/delete query] -> call python code/endpoints
api -> navigate to api
interface -> navigate to interface
download folder
'''