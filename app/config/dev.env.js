'use strict'
const config = require('../config')
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

const HOST = process.env.HOST

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  API_BASE_URL: `"http://${HOST || config.dev.host}:5000"`,
  APP_BASE_URL: `"http://${HOST || config.dev.host}:8080"`,
})
