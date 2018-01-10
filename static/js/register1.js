$(function(){
	var error_name = false;
	var error_password = false;
	var error_confirm = false;
	var error_email = false;
	var error_check = false;
	var username = $('#username');
	var password = $('#password');
	var confirm = $('#confirm');
	var email = $('#email');
	var allow = $('#allow');
	var form_submit = document.getElementById('register_form');

	username.blur(function(){
		check_user_name();
	});
	
	password.blur(function(){
		check_password();
	});
	
	confirm.blur(function(){
		check_password_confirm();
	});
	
	email.blur(function(){
		check_email()
	});

	allow.click(function() {
		if($(this).is(':checked'))
		{
			error_check = false;
			$(this).siblings('span').hide();
		}
		else
		{
			error_check = true;
			$(this).siblings('span').html(' * 请勾选同意');
			$(this).siblings('span').show(300);
		}
	});

	function check_user_name(){
		var len = username.val().length;
		if (len<5||len>20)
		{
			username.next().html(" * 请输入5-20个汉字");
			username.next().show(300);
			error_name = true;
		}
		else {
			$.get('/user/register_exist/?uname='+username.val(), function (data) {
				if(data.count != 0) {
					username.next().html('用户名已存在').show();
					error_name = true;
				}
				else {
					username.next().hide();
					error_name = false;
				}
            })
		}
	}
	
	function check_password(){
		var len = password.val().length;
		if(len<6 || len>20) {
			password.next().html(" * 密码长度应为6-20位");
			password.next().show(300);
			error_password = true;
		}
		else{
			password.next().hide();
		}
	}
	
	function check_password_confirm(){
		var temp = confirm.val();
		var pwd1 = password.val();
		if(temp !== pwd1 || temp === '') {
			error_confirm = true;
			confirm.next().html(' * 两次密码输入不一致');
			confirm.next().show(300);
		}
		else {
			confirm.next().hide();
		}
	}
	
	function check_email() {
		var re = /^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
		if(re.test(email.val())){
			email.next().hide();
			error_email = false;
		}
		else {
			error_email = true;
			email.next().html(" * 邮箱格式有误，请重新输入");
			email.next().show(300);
		}
	}

	function register_check() {
		check_user_name();
		check_password();
		check_password_confirm();
		check_email();
		return(!(error_name === false && error_password === false && error_confirm === false && error_email === false && error_check === false));
	}

	window.onload = function() {
		form_submit.onclick = function (ev) {
			if(register_check()){
			ev.preventDefault();
			}
			else{
			}
		}
	}
});
