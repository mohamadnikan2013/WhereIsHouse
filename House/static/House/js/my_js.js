/**
 * Created by Nikan G on 7/25/2016.
 */
$(document).ready(function () {
    $.getJSON("/house/more/" + "total" + "/" + "0")
        .done(function (data) {
            counter++;
            $.each(data, function (index, cat) {
                var picture = '';
                if (cat.fields.site != null) {
                    picture = cat.fields.image_url;
                }
                else {
                    picture += '../media/';
                    picture += cat.fields.image;
                }
                var new_node = document.createElement("div");
                new_node.className = "ui card";
                var contenet = "<div class=" + "image" + "><img src=" + picture + "></div><div class=" + "content" + "><a class=" + "header" + ">" + cat.fields.title + "</a><div class=" + "meta" + "><span class=" + "date" + ">" + cat.fields.time + "</span></div><div class=" + "description" + ">" + cat.fields.price1 + "</div></div><div class=" + "extra content" + "><a href=house/details/" + cat.fields.token + "><i class=" + "user icon" + "></i>More About This</a></div>";
                new_node.innerHTML = contenet;
                document.getElementById("first").appendChild(new_node);
            });
        });

    search();
});
var counter = 1;
var city = $("#my_input").val();
$(window).scroll(function () {
    if ($(window).scrollTop() + $(window).height() == $(document).height()) {
        if (!city) {
            city = "total"
        }
        $.getJSON("/house/more/" + city + "/" + counter)
            .done(function (data) {
                counter++;
                $.each(data, function (index, cat) {
                    var new_node = document.createElement("div");
                    new_node.className = "ui card";
                    new_node.style.display =inline-block ;
                    var contenet = "<div class=" + "image" + "><img src=" + cat.fields.image + "></div><div class=" + "content" + "><a class=" + "header" + ">" + cat.fields.title + "</a><div class=" + "meta" + "><span class=" + "date" + ">" + cat.fields.time + "</span></div><div class=" + "description" + ">" + cat.fields.price1 + "</div></div><div class=" + "extra content" + "><a><i class=" + "user icon" + "></i>More About This</a></div>";
                    new_node.innerHTML = contenet;
                    document.getElementById("second").appendChild(new_node);
                });
            });
    }
});
// $("#search_key").onclick()(function () {
//     var counter = 0;
//     $.getJSON("search/" + city + "/" + counter)
//         .done(function (data) {
//             counter++;
//             $("#first").empty();
//             $("#second").empty();
//             $.each(data, function (index, cat) {
//                 var new_node = document.createElement("div");
//                 new_node.className = "ui card";
//                 var contenet = "<div class=" + "image" + "><img src=" + cat.fields.image + "></div><div class=" + "content" + "><a class=" + "header" + ">" + cat.fields.name + "</a><div class=" + "meta" + "><span class=" + "date" + ">" + cat.fields.time + "</span></div><div class=" + "description" + ">" + cat.fields.price + "</div></div><div class=" + "extra content" + "><a><i class=" + "user icon" + "></i>More About This</a></div>";
//                 new_node.innerHTML = contenet;
//                 document.getElementById("first").appendChild(new_node);
//             });
//         });
// });