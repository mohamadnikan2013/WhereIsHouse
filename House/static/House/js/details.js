/**
 * Created by nikang on 8/7/16.
 */

$(document).ready(function () {

    // $('.results').hide();
    $("#form2").hide();
    get_json_object();
    like();
    $('#comment_button').click(function () {
        comment_post();
    });
    $('#reply_button').click(function () {
        reply_post();
    });
    $('#reply_text ,#comment_text').change(function () {
        $(".myresults").empty();
        suggest();
    });

});
function get_json_object() {
    var house_token = $.trim($('#House_token').text());
    $.ajax({
        method: "GET",
        url: "/house/ajax/" + house_token + '/'
    })
        .done(function (data) {
            $.each(data['comments'], function (index, cat) {
                var content = "<div class=" + "comment" + "><a class=" + "avatar" + "><img src=" + cat.author_picture + "></a><div class=" + "content" + "><a class=" + "author" + ">" + cat.author_name + "</a><div class=" + "metadata" + "><div class=" + "date" + ">" + cat.date + "</div></div><div class=" + "text" + ">" + cat.text + "</div><div class=" + "actions" + "><a class=" + "reply" + " id=" + cat.comment_pk + " >Reply</a></div></div></div>";
                // $('#comments').prepend(content);
                if (cat.replies) {
                    $.each(cat.replies, function (index1, cat1) {
                        content += "<div class=" + "comments" + "><div class=" + "comment" + "><a class=" + "avatar" + "><img src=" + cat1.author_picture + "></a><div class=" + "content" + "><a class=" + "author" + ">" + cat1.author_name + "</a><a class=" + "author" + "><br>" + "@" + cat.author_name + "</a><div class=" + "metadata" + "><span class=" + "date" + ">" + cat1.date + "</span></div><div class=" + "text" + ">" + cat1.text + "</div></div></div></div>";
                    });
                }
                $('#comments').prepend(content);
            });
            $('.reply').on("click", function (event) {
                var comment_pk = $(this).attr("id");
                $('#form1').fadeOut('fast');
                $("#form2").show('slow');
                $("#comment_pk").html(comment_pk);
            });
        })
        .fail(function (data) {
            console.log("fail")
        });
}

function comment_post() {
    var house_token = $.trim($('#House_token').text());
    var comment_text = $('#comment_text').val();
    var csrf = $('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        method: "POST",
        url: "/house/ajax/" + house_token + '/',
        data: {
            text: comment_text,
            csrfmiddlewaretoken: csrf
        }

    })
        .success(function (data) {
            $('#comments').empty();
            get_json_object();

        })
        .fail(function (data) {
            alert('failed');
            console.log("fail")
        });

}

function reply_post() {
    var csrf = $('input[name=csrfmiddlewaretoken]').val();
    var reply_text = $('#reply_text').val();
    var house_pk = $.trim($('#house_pk').text());
    var comment_pk = $.trim($('#comment_pk').text());
    $.ajax({
        method: "POST",
        url: "/house/reply/" + house_pk + '/' + comment_pk + '/',
        data: {
            text: reply_text,
            csrfmiddlewaretoken: csrf
        }
    })
        .done(function (data) {
            $('#comments').empty();
            get_json_object();
        })
        .fail(function (data) {
            console.log("fail")
        });

}

function like() {
    var house_pk = $.trim($('#house_pk').text());
    $('#like_house').click(function () {
        $.get("/house/reply/" + house_pk + '/1/', function (data) {
            console.log("Load was performed.");
        });
    });
}

function suggest() {
    var text = $('#comment_text').val();
    if (text.length > 0) {
        console.log(text);
        $.ajax({
            method: "GET",
            url: "/house/suggest/" + text + '/'
        })
            .done(function (data) {
                $.each(data['my_suggest'], function (index, cat) {
                    var content = "<a class=" + "mysuggest" + ">" + cat['text'] + "</a>";
                    content += "<br>";
                    $(".myresults").prepend(content)
                });
                $(".mysuggest").click(function () {
                    var suggest = $.trim($(this).text());
                    $('#reply_text ,#comment_text').val(suggest);

                });

            });
    }
}