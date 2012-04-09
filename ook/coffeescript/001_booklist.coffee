namespace 'Ook.Booklists', (exports) ->
    exports.go_to_page = (page_nr) ->
        # remove the active class
        $("#booklist-view > .pagination .active").removeClass "active"

        # get the left
        current_left = parseInt $("#booklist").css "marginLeft"
        target_left = $("#booklist > .booklist-page:nth-child(" + page_nr + ")").position().left
        
        # animate the page switching
        $("#booklist").animate 
            "margin-left": -target_left
            600
            "swing"
            -> 
                $(this).data "current-page", page_nr
            
        # fix the pagination
        $("#booklist-view .pagination-nav.prev").toggleClass "disabled", page_nr == 1
        $("#booklist-view .pagination-nav.next").toggleClass "disabled", page_nr == $("#booklist").data "page-count"
        $("#booklist-view .pagination li[data-nr="+ page_nr + "]").addClass "active"
        
        
    exports.view_per_page = (count) ->
        # remove the tops
        $("#booklist").append $("#booklist").find ".booklist-item"
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
        $("#booklist").data "page-count", page_count

        $("#booklist-view > .pagination li:not(.pagination-nav)").remove()
        
        for page_nr in [1..page_count]
            do (page_nr) ->
                elem = $("<li data-nr=\"" + page_nr + "\"><a href=\"#\">" + page_nr + "</li>")
                $("#booklist-view > .pagination li:last").before elem
                
                # page click
                elem.click ->
                    exports.go_to_page $(this).data("nr")
                    

        # set parent size
        $("#booklist").width parent_size;
        
        # just in case, go to page 1
        exports.go_to_page 1
                    
    exports.init = ->
        exports.view_per_page 9
        
        $(".booklist-view-per-page").click ->
            unless $(this).is ".active"
                exports.view_per_page ($(this).data "per-page")
    
        ###
        Init the navigation
        ###
        $("#booklist-view .pagination-nav.prev").click ->
            unless $(this).is ".disabled"
                exports.go_to_page ($("#booklist").data "current-page") - 1
                
        $("#booklist-view .pagination-nav.next").click ->
            unless $(this).is ".disabled"
                exports.go_to_page ($("#booklist").data "current-page") + 1