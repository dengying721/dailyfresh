$(function () {
    var error_username = false;
    var error_password = false;
    var username = $('#username');
    var password = $('#password');

    username.blur(function () {
        check_username();
    })

    function check_username() {
        var uname = username.val();
        $.get('/user/user_exist/?uname='+uname, function (data) {
            if(data.is_exist){
                error_username = false;
            }
            else{
                error_username = true;
                username.next().html("用户不存在");
            }

        })
    }
})