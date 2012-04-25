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

build_hogan = (callback) ->
    ws = fs.createWriteStream( './ook/media/js/templates.js', { 'flags': 'w' } )

    hogan = spawn 'hulk', ['./ook/hogan/*.mustache']
    
    hogan.stderr.on 'data', (data) ->
        process.stderr.write data.toString()

    # open file
    hogan.stdout.on 'data', (data) ->
        output = data.toString()
        ws.write(output)
    
    hogan.on 'exit', (code) ->
        ws.end()
        callback?() if code is 0

task 'build_coffee', 'Build coffeescript', -> build_coffee()
task 'build_hogan', 'Build mustache templates', -> build_hogan()
task 'build_less', 'Build less', -> build_less
task 'build', 'Build all', ->
  build_coffee()
  build_less()
  build_hogan()
  
