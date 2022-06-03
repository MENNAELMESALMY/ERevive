
cluster_names = ['cluster1','cluster2','cluster3','cluster4']
appString = '''
<template>
    <div id="app">
      <div 
      v-for="card in cards"
          :key="card.name"
          :title="card.name"
          :describtion="card.describtion"
      ></div>
        <p>Try scss</p>
    </div>
</template>

<script>
import cardDesign from './components/cardDesign.vue'
    export default{
    data() {
        return {
        message: 'Hello World',
        "clusters": {cluster_names},
        };
    },
  components: {
    cardDesign
    }
    };
</script>

<style lang='scss' scoped >
    #app {
    font-size: 18px;
    font-family: 'Roboto', sans-serif;
    color: red;
    p{
        color: blue;
    }
    }
</style>
    '''


with open('FrontCode/src/App.vue', 'w') as f:
    f.write()
    


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

with open('FrontCode/src/main.js', 'w') as f:
    f.write('''
import * as Vue from 'vue';
import App from './App.vue';

Vue.createApp(App).mount('#app');
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

'''
list of apis:
  app/home -> card/clusters -> route(-------) to cluster view(each of them has get/post/put/delete)
  view -> iterate over all apis and generate components(card button convert to delete)
  store -> modules ()
  (url, method)

  query1:{
    url:jjjj,
    method:kkk,
  }
'''
#getClusterNames()
cluster_names = ['cluster1','cluster2','cluster3','cluster4']
