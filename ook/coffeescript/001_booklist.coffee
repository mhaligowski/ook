namespace 'Ook.Booklists', (exports) ->
    exports.go_to_page = (page_nr) ->
        # remove the active class
        $("#booklist-view > .pagination .active").removeClass "active"

        # get the left
        current_left = parseInt $("#booklist").css "marginLeft"
        target_left = $(sprintf "#booklist > .booklist-page:nth-child(%d)", page_nr)?.position()?.left
        
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
        $(sprintf "#booklist-view .pagination li[data-nr=%d]", page_nr).addClass "active"
        
    exports.view_per_page = (count) ->
        # make the page element
        booklist_page_elem = (page_nr) ->
            $(sprintf "<div class=\"span12 booklist-page\" data-nr=\"%d\"</div>", page_nr)
        
        # remove the tops
        $("#booklist").append $("#booklist").find ".booklist-item"
        $("#booklist > .booklist-page").remove()
        
        # some init
        [page_count, page_elem_size] = [0, 0]
        [page_elem, parent_size] = [booklist_page_elem (page_count + 1)
                                    $("#booklist").width()]
        
        # if the list is empty
        if $("#booklist > .booklist-item").size() is 0
            elem = booklist_page_elem 1
            $("#booklist").append elem
            page_count = 1
        
        # pageify
        for item in $("#booklist > .booklist-item")
            do (item) ->
                page_elem.append item
                page_elem_size += 1
                
                # next page, please
                if page_elem_size == count
                    page_count += 1
                    $("#booklist").append page_elem
                    parent_size += page_elem.width()
                    page_elem = booklist_page_elem (page_count + 1)
                    page_elem_size = 0
                    
        # append the last one
        if page_elem_size isnt 0
            $("#booklist").append page_elem
            parent_size += page_elem.width()
            page_count =+ 1
        
        # make the pagination
        $("#booklist").data "page-count", page_count
        $("#booklist-view > .pagination li:not(.pagination-nav)").remove()
        
        # add the pagination elements (make sure there is at least one page there)
        page_count = 1 if page_count is 0
        for page_nr in [1..page_count]
            do (page_nr) ->
                elem = $(sprintf "<li data-nr=\"%1$d\"><a href=\"#\">%1$d</li>", page_nr )
                $("#booklist-view > .pagination li:last").before elem
                
                # page click
                elem.click ->
                    exports.go_to_page $(this).data "nr"

        # set parent size
        $("#booklist").width parent_size;
        
        # fix the main menu
        $(".booklist-view-per-page").removeClass "active"
        $(sprintf ".booklist-view-per-page[data-per-page=%d]", count).addClass "active"
        
        # just in case, go to page 1
        exports.go_to_page 1
                    
    exports.add_book_form_handler = ->
        $.post(
            sprintf "/api/booklist/%d/books", $("#booklist").data "booklist-id"
            $(this).serialize()
            (data) ->
                alert data
        )
        
        false
        
    exports.init_view = (booklist_id) ->
        # set the view
        $("#booklist").data "booklist-id", booklist_id
        
        # get the data
        $.get(
            sprintf "/api/booklist/%d", booklist_id
            (data) ->
                # set title
                $("#booklist-title").text data.name
                
                # clear ALL the books! and add the new ones
                $("#booklist").empty().append templates.booklist_item.render "booklist-items": data.book_set
                
                # make the view visible
                $("#booklist-view").show()

                # make 9 books per page
                exports.view_per_page 9
                exports.go_to_page 1

        )
        
        
        
    exports.init = ->
        # handler fo changing number of books per page
        $(".booklist-view-per-page").click ->
            exports.view_per_page ($(this).data "per-page") unless $(this).is ".active"
    
        # Init the navigation
        $("#booklist-view .pagination-nav.prev").click ->
            exports.go_to_page ($("#booklist").data "current-page") - 1 unless $(this).is ".disabled"

        $("#booklist-view .pagination-nav.next").click ->
            exports.go_to_page ($("#booklist").data "current-page") + 1 unless $(this).is ".disabled"
            
        # init modal
        $('#add-book-modal').modal show:false
        $('#add-book-modal form').submit exports.add_book_form_handler
        $("#add-book-modal-help").popover()