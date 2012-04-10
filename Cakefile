fs = require 'fs'

{print} = require 'util'
{spawn} = require 'child_process'

build_coffee = (callback) ->
  coffee = spawn 'coffee', ['-c', '-j', './ook/media/js/ook.js', './ook/coffeescript/']
  
  coffee.stderr.on 'data', (data) ->
    process.stderr.write data.toString()
    
  coffee.stdout.on 'data', (data) ->
    print data.toString()
    
  coffee.on 'exit', (code) ->
    callback?() if code is 0

build_less = (callback) ->
  less = spawn 'lessc', ['./ook/less/ook.less', '-x', './ook/media/css/ook.css']

  less.stderr.on 'data', (data) ->
    process.stderr.write data.toString()
    
  less.stdout.on 'data', (data) ->
    print data.toString()
    
  less.on 'exit', (code) ->
    callback?() if code is 0

task 'build', 'Build all', ->
  build_coffee()
  build_less()
