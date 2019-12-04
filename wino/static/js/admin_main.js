$(function () {
    // inspect html to check id of category select dropdown.
    $(document).on('change', "select#id_country", function () {
        $.getJSON("/getRegion/", {id: $(this).val()}, function (j) {
            var options = '<option value="">---------</option>';
            for (var i = 0; i < j.length; i++) {
                options += '<option value="' + j[i].id + '">' + j[i].name + '</option>';
            }
            // inspect html to check id of subcategory select dropdown.
            $("select#id_region").html(options);
        });
    });
});
$(function () {
    // inspect html to check id of category select dropdown.
    $(document).on('change', "select#id_region", function () {
        $.getJSON("/getArea/", {id: $(this).val()}, function (j) {
            var options = '<option value="">---------</option>';
            for (var i = 0; i < j.length; i++) {
                options += '<option value="' + j[i].id + '">' + j[i].name + '</option>';
            }
            // inspect html to check id of subcategory select dropdown.
            $("select#id_area").html(options);
        });
    });
});
