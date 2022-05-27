mkdir FrontCode
cd ./FrontCode
touch .babelrc.js
touch webpack.config.js
npm init -y
mkdir src
touch src/main.js
touch src/App.vue
touch src/index.html
npm install vue vue-loader vue-template-compiler webpack webpack-cli webpack-dev-server babel-loader @babel/core @babel/preset-env sass sass-loader css-loader vue-style-loader html-webpack-plugin rimraf -D

cd ../
python3 writeFiles.py
cd ./FrontCode
npm run serve