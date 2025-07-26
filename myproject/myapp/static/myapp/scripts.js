document.addEventListener('DOMContentLoaded', (event) => {
    const signupButton = document.getElementById('signupButton');
    const loginButton = document.getElementById('loginButton');

    signupButton.addEventListener('click', function() {

        // サインアップページへのナビゲーション
        window.location.href = '/myapp/signup/';
    });

    loginButton.addEventListener('click', function() {
       
        // ログインページへのナビゲーション
        window.location.href = '/myapp/login/';
    });
});
