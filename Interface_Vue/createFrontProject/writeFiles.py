from utils import *
from create_vue_app.create_form import *
from create_vue_app.create_routing import *
from create_vue_app.create_store_idx import *
from create_vue_app.create_dashboard import *
from create_vue_app.create_cards import *
from create_vue_app.create_store import *
from create_vue_app.create_cards_designs import *



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

c = {
  "c1":[
    {
      "url":"",
      "method":"get",
      "query_params":[
        ("course_name","str","like","max"),
        ("course_id","int","=","avg")
      ],
      "body_params":[
        "name","bday"
      ],
      "path_params":[
        "course_path"
      ],
      "response":{
        "field1":"value1",
        "field2":"value2",
        "field3":"value3",
        "field4":"value4",
        "field5":"value5",
        "field6":"value6"
      },
      'endpoint_name':'endpoint_name1',
    },
    {
      "url":"",
      "method":"get",
      "query_params":[
        ("course_name","str","like","max"),
        ("course_id","int","=","avg")
      ],
      "body_params":[
        "name","bday"
      ],
      "path_params":[
        "course_path"
      ],
      "response":{
        "field1":"value1",
        "field2":"value2",
        "field3":"value3",
        "field4":"value4",
        "field5":"value5",
        "field6":"value6"
      },
      'endpoint_name':'endpoint_name2'
    },
    {
      "url":"",
      "method":"post",
      "query_params":[
        ("course_name","str","like","max"),
        ("course_id","int","=","avg")
      ],
      "body_params":[
        "name","bday"
      ],
      "path_params":[
        "course_path"
      ],
      "response":{
        "field1":"value1",
        "field2":"value2"
      },
      'endpoint_name':'endpoint_name3'
    },
    {
      "url":"",
      "method":"get",
      "query_params":[
        ("course_name","str","like","max"),
        ("course_id","int","=","avg")
      ],
      "body_params":[
        "name","bday"
      ],
      "path_params":[
        "course_path"
      ],
      "response":{
        "field1":"value1",
        "field2":"value2"
      },
      'endpoint_name':'endpoint_name4'
    }
  ],
  "c2":[
    {
      "url":"",
      "method":"post",
      "query_params":[
        ("course_name","str","like","max"),
        ("course_id","int","=","avg")
      ],
      "body_params":[
        "name","bday"
      ],
      "path_params":[
        "course_path"
      ],
      "response":{
        "field1":"value1",
        "field2":"value2"
      },
      'endpoint_name':'endpoint_name5'
    },{
      "url":"",
      "method":"get",
      "query_params":[
        ("course_name","str","like","max"),
        ("course_id","int","=","avg")
      ],
      "body_params":[
        "name","bday"
      ],
      "path_params":[
        "course_path"
      ],
      "response":{
        "field1":"value1",
        "field2":"value2",
        "field3":"value3",
        "field4":"value4",
        "field5":"value5",
        "field6":"value6"
      },
      'endpoint_name':'endpoint_name6'
    }
  ]
}

cluster_names = list(c.keys())

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
    f.write('''
<template>
    <div id="home">
      <cardDesign 
      v-for="(card,i) in clusters"
          :key=i
          :title="card"
          :describtion= "''"
      />
    </div>
</template>

<script>
import cardDesign from '../components/cardDesign1.vue'
    export default{
    data() {
        return {
        clusters: %s,
        };
    },
  components: {
    cardDesign
    }
    };
</script>

<style lang='scss' scoped >
</style>
    '''
    %(cluster_names))

#create router
generate_routing(cluster_names,routerRoute)

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
  </head>
  <body>
    <div id="app"></div>
  </body>
</html>
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