function logout(){
        $.removeCookie('mytoken', { path: '/' });
        alert('๋ก๊ทธ์์!');
        window.location.href='/';
  }