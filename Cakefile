fs = require 'fs'
wrench = require 'wrench'

# init options
option '-s', '--source [DIR]', 'source directory'
option '-o', '--output [DIR]', 'directory for compiled code'
option '-i', '--img [DIR]', 'directory suffix for images'


# default options
default_options =
    source: 'webapp/src/'
    coffee_suffix: 'coffeescript/'
    img: 'img/'
    output: 'tmp/media/'

task 'mkdirs', 'create the output directory (if it does not exist)', (options) ->
    output_dir = options.output ? default_options.output
    wrench.mkdirSyncRecursive output_dir, 0o0777;
    
    parts = ['img/', 'js/', 'css/']
        
    for p in parts
        wrench.mkdirSyncRecursive output_dir + p
        
task 'copy:images', 'copy images from source dir to target', (options) ->
    s = options.img ? default_options.img
    source = options.source ? default_options.source
    output = options.output ? default_options.output
    
    wrench.copyDirSyncRecursive (source + s), (output + s)
    
    
task 'all', 'compile everything and copy to output directory', (options) ->
    invoke 'mkdirs'
    invoke 'copy:images'