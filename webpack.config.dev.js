const { merge } = require('webpack-merge');
const webpackConfig = require('./webpack.config.js');

module.exports = merge(webpackConfig, {
  mode: 'development',
  devServer: {
    historyApiFallback: true,
    open: true,
    host: '0.0.0.0',
    port: 10000,
    proxy: {
      '/img/**': {
        target: 'http://localhost:5000',
        secure: false,
        logLevel: 'debug'
      }
    },
  }
});