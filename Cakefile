fs = require 'fs'
wrench = require 'wrench'
# path = require 'path'

{print} = require 'util'
{spawn} = require 'child_process'

# init options
option '-s', '--source [DIR]', 'source directory'
option '-o', '--output [DIR]', 'directory for compiled code'
option '-i', '--img [DIR]', 'directory suffix for images'
option '-j', '--js [DIR]', 'directory suffix for javascript'
option '-l', '--less_src file', 'main file for less'
option '-t', '--less_out file', 'target file for less'

# default options
default_options =
    source: 'webapp/src/'
    coffee: 'coffeescript/'
    less_src: 'less/ook.less'
    less_out: 'css/ook.css'
    output: 'tmp/media/'
    img: 'img/'
    js: 'js/'
    css: 'css/'

task 'mkdirs', 'create the output directory (if it does not exist)', (options) ->
    print "[mkdirs]\n"
    
    output_dir = options.output ? default_options.output

    print "Creating output dir " + output_dir + "...\n"
    wrench.mkdirSyncRecursive output_dir, 0o0777;
    
    parts = ['img/', 'js/', 'css/']
        
    for p in parts
        print "Creating output dir " + output_dir + p + "...\n"
        wrench.mkdirSyncRecursive output_dir + p, 0o0777
        
task 'copy:images', 'copy images from source dir to target', (options) ->
    print "[copy:images]\n"
    s = options.img ? default_options.img
    source = options.source ? default_options.source
    output = options.output ? default_options.output
    
    wrench.copyDirSyncRecursive (source + s), (output + s)

task 'copy:js', 'copy static javascript (libs)', (options) ->
    print "[copy:js]\n"
    ###
    Copies javascript files (not compiled)
    ###
    s = options.js ? default_options.js
    source = options.source ? default_options.source
    output = options.output ? default_options.output
    
    wrench.copyDirSyncRecursive (source + s), (output + s)
    
task 'compile:coffee', 'compiles coffescript', (options) ->
    print "[compile:coffee]\n"
    ###
    Compiles coffeescript files
    ###
    
    # set the directories
    source_dir = options.source ? default_options.source
    output_dir = options.output ? default_options.output
    
    coffee_dir = options.coffee ? default_options.coffee
    js_dir = options.js ? default_options.js
    
    coffee = spawn 'coffee', ['-c', '-o', (output_dir + js_dir), (source_dir + coffee_dir)]
  
    coffee.stderr.on 'data', (data) ->
        process.stderr.write data.toString()
    
    coffee.stdout.on 'data', (data) ->
        print data.toString()
    
    coffee.on 'exit', (code) ->
        callback?() if code is 0
    
task 'compile:less', 'compiles less', (options) ->
    print "[compile:less]\n"
    # set the paths
    src_dir = options.source ? default_options.source
    output_dir = options.output ? default_options.output
    
    less_file = options.less_src ? default_options.less_src
    inputLessFile = src_dir + less_file

    css_file = options.less_out ? default_options.less_out
    outputLessFile = output_dir + css_file
        
    # run lessc
    less = spawn 'lessc', [inputLessFile, '-x', outputLessFile]

    less.stderr.on 'data', (data) ->
        process.stderr.write data.toString()
    
    less.stdout.on 'data', (data) ->
        print data.toString()
    
    less.on 'exit', (code) ->
        callback?() if code is 0

task 'clean', 'cleans the given directory', (options) ->
    print "[clean]\n"
    
    output_dir = options.output ? default_options.output
    
    wrench.rmdirRecursive output_dir
    
task 'all', 'compile everything and copy to output directory', (options) ->
    # make dirs first
    invoke 'mkdirs'
    
    # copy jobs first
    invoke 'copy:images'
    invoke 'copy:js'
    
    # compile jobs are last
    invoke 'compile:less'
    invoke 'compile:coffee'
