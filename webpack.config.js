var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  context: __dirname,

  entry: './assets/js/main.js', // これがエントリーポイント
  mode: 'development',
  output: { // コンパイルされたファイルの設定
      path: path.resolve('./assets/bundles/'),
      filename: "[name]-[hash].js",
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
    new webpack.ProvidePlugin({
        $: 'jquery',
        jQuery: 'jquery',
        'window.jQuery': 'jquery',
        Popper: ['popper.js', 'default'],
    })
  ],

  module: {
    rules:[
      {
      test: /\.css$/,
      use: [ 'style-loader', 'css-loader' ]
      },
    ],
  },
}
