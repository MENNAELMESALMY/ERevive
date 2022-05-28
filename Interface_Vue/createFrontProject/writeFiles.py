with open('FrontCode/src/App.vue', 'w') as f:
    f.write('''
<template>
    <div id="app">
        {{ message }}
        <p>Try scss</p>
    </div>
</template>

<script>
    export default {
    data() {
        return {
        message: 'Hello World',
        };
    },
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
    ''')
    


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
