$(function () {
    var error_username = false;
    var error_password = false;
    var username = $('#username');
    var password = $('#password');
    var submitBtn = document.getElementById('submit');

    window.onload = function () {
        submitBtn.onclick = function (ev) {
            alert("the loginCheck result is:"+ login_check());
            if(login_check()) {
                ev.preventDefault();
            }
            else {
                alert("congratulations!");
            }
        }
    };

    username.blur(function () {
        check_username();
    });

    password.blur(function () {
        check_password();
    });

    function check_username() {
        var uname = username.val();
        var len = uname.length;
        if(len === 0) {
            error_username = true;
            username.next().html("* 请输入用户名");
            username.next().show(300);
        }
        else{
            $.get('/user/user_exist/?uname='+uname, function (data) {
                if(data.is_exist){
                    error_username = false;
                    username.next().hide();
                }
                else{
                    error_username = true;
                    username.next().html("* 用户不存在");
                    username.next().show(300);
                }

            })
        }
    }

    function check_password() {
        var pwd_len = password.val().length;
        if(pwd_len < 6){
            error_password = true;
            password.next().html("* 密码错误，请重新输入");
            password.next().show(300);
        }
        else{
            password.next().hide();
            error_password = false;
        }
    }

    function login_check() {
        alert('hello');
        check_username();
        check_password();
        alert(error_username);
        alert(error_password);
        return ((error_username === true || error_password === true));
    }

});