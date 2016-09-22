var path = require('path')
var webpack = require('webpack')
var ExtractTextPlugin = require("extract-text-webpack-plugin");
var AssetsPlugin = require('assets-webpack-plugin');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  entry: [
    'expose?$!expose?jQuery!jquery',
    'bootstrap-webpack!./src/bootstrap.config.js',
    'expose?main!./src/main.js'
  ],
  output: {
    path: 'dist/',
    publicPath: '/frontend/dist/',
    filename: 'build.js'
  },
  resolveLoader: {
    root: path.join(__dirname, 'node_modules/'),
  },
  module: {
    loaders: [
      {
        test: /\.vue$/,
        loader: 'vue'
      },
      {
        test: /\.js$/,
        loader: 'babel',
        exclude: /node_modules/
      },
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'file',
        include: [
          path.resolve(__dirname, "./src/assets")
        ],
        query: {
          name: '[name].[ext]?[hash]'
        }
      },
      {
        test: /\.(woff|woff2)(\?v=\d+\.\d+\.\d+)?$/,
        loader: 'url?limit=10000&mimetype=application/font-woff'
      },
      {
        test: /\.ttf(\?v=\d+\.\d+\.\d+)?$/,
        loader: 'url?limit=10000&mimetype=application/octet-stream'
      },
      {
        test: /\.eot(\?v=\d+\.\d+\.\d+)?$/,
        loader: 'file'
      },
      {
        test: /\.svg(\?v=\d+\.\d+\.\d+)?$/,
        loader: 'url?limit=10000&mimetype=image/svg+xml'
      }
    ]
  },
  vue: {
    loaders: {
      css: ExtractTextPlugin.extract('css'),
    },
  },
  plugins: [
    new ExtractTextPlugin('style.css'),
  ],
  devServer: {
    historyApiFallback: true,
    noInfo: true
  },
  devtool: '#source-map',
  watchOptions: {
    poll: true,
  },
}

if (process.env.USE_WEBPACK_DEV_SERVER === 'true') {
  module.exports.entry = Array.prototype.concat.apply(
    [
      'webpack-dev-server/client?/frontend/sockjs-node',
      'webpack/hot/only-dev-server',
    ],
    module.exports.entry
  );

  module.exports.output.publicPath = '/frontend/dist/';

  module.exports.plugins = Array.prototype.concat.apply(
    module.exports.plugins,
    [
      new webpack.HotModuleReplacementPlugin(),
      new AssetsPlugin({filename: '/tmp/webpack-assets.json'}),
      new BundleTracker({filename: '/tmp/webpack-stats.json'}),
    ]
  );

  module.exports.devtool = '#eval-source-map';
}

if (process.env.NODE_ENV === 'production') {
  module.exports.devtool = '#source-map'
  // http://vue-loader.vuejs.org/en/workflow/production.html
  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: '"production"'
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      compress: {
        warnings: false
      }
    }),
    new webpack.optimize.OccurenceOrderPlugin()
  ])
}
