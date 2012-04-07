###
Define some useful CScript functions
    
Author: Mateusz Haligowski <mhaligowski@googlemail.com>
Date started: 07-04-2012
###

namespace = (target, name, block) ->
  [target, name, block] = [(if typeof exports isnt 'undefined' then exports else window), arguments...] if arguments.length < 3
  top    = target
  target = target[item] or= {} for item in name.split '.'
  block target, top
