namespace 'Ook.Booklists', (exports) ->
    exports.go_to_page = (page_nr) ->
        # get the left
        current_left = parseInt $("#booklist").css("marginLeft")
        target_left = $("#booklist > .booklist-page:nth-child(" + page_nr + ")").position().left
        $("#booklist").animate 
            "margin-left": -target_left
            600
            "swing"
        
    exports.view_per_page = (count) ->
        # remove the tops
        $("#booklist").append $("#booklist").find(".booklist-item")        
        $("#booklist > .booklist-page").remove()
        
        # some init
        page_count = 0
        page_elem = $("<div class=\"span12 booklist-page\" data-nr=\"" + (page_count + 1) + "\"></div>")
        page_elem_size = 0
        parent_size = $("#booklist").width()
        
        # pageify
        for item in $("#booklist > .booklist-item")
            do (item) ->
                page_elem.append(item)
                page_elem_size += 1
                
                # next page, please
                if page_elem_size == count
                    page_count += 1
                    $("#booklist").append page_elem
                    parent_size += page_elem.width()
                    page_elem = $("<div class=\"span12 booklist-page\" data-nr=\"" + (page_count + 1) + "\"></div>")
                    page_elem_size = 0
                    
        # append the last one
        if page_elem_size != 0
            $("#booklist").append page_elem
            parent_size += page_elem.width()
            page_elem = $("<div class=\"span12 booklist-page\" data-nr=\"" + page_count + "\"></div>")
            page_elem_size = 0
        
        # make the pagination
        $("#booklist-view > .pagination li:not(.pagination-nav)").remove()
        
        for page_nr in [1..page_count]
            do (page_nr) ->
                elem = $("<li data-nr=\"" + page_nr + "\"><a href=\"#\">" + page_nr + "</li>")
                $("#booklist-view > .pagination li:last").before elem
                
                # page click
                elem.click ->
                    exports.go_to_page $(this).data("nr")
                    

        # set parent size
        $("#booklist").width(parent_size);
                    
    exports.init = ->
        exports.view_per_page 9
        
        $(".booklist-view-per-page").click ->
            exports.view_per_page $(this).data("per-page")
    