echo $PWD

if [ ! -d "FrontCode" ]; then
    mkdir FrontCode
fi

find FrontCode -mindepth 1 ! -regex '^FrontCode/node_modules\(/.*\)?' -delete



cd ./FrontCode
touch .babelrc.js
touch webpack.config.js
npm init -y

mkdir src
mkdir src/components
mkdir src/store
mkdir src/store/modules
mkdir src/views
mkdir src/router
mkdir src/scss

touch src/main.js
touch src/App.vue
touch src/index.html

if [ ! -d "node_modules" ]; then
    npm install moment axios vue@3.2.33 vue-loader@17.0.0 vuex vue-router@4.0.0 vue-template-compiler@2.6.14 webpack webpack-cli webpack-dev-server babel-loader @babel/core @babel/preset-env sass sass-loader css-loader vue-style-loader html-webpack-plugin rimraf -D
fi

cd ../
python3 writeFiles.py