// import express from 'express'
// import history from 'connect-history-api-fallback'
// import serveStatic from 'serve-static'
// import path from 'path'
const express = require('express')
const history = require('connect-history-api-fallback')
const serveStatic = require('serve-static')
const path = require('path')

// const port = process.env.PORT
const port = process.env.PORT || 80

const app = express()
console.log(port)

/* eslint-disable */
const fullPath = path.join(__dirname + '/dist/spa')
/* eslint-enable */

app.use(history())
app.use(serveStatic(fullPath))
app.listen(port)