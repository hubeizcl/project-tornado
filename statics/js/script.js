$(document).ready(function () {
    $("login").click(function () {
        var user = $("#username").val();
        var password = $("#password").val();
        var pd = {"username": user, "password": password};
        $.ajax({
            type: "post",
            url: "/",
            data: pd,
            success: function (data) {
                alert(data)
            },
            error: function () {
                alert("error")
            },
        });
    });
});