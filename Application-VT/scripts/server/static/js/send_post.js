elem.onclick = function() {
    var log = login_web.value
    var passwd = password_web.value
    console.log(log, passwd)
    var data = {
      login: log,
      password: passwd
    }
    var json = JSON.stringify(data);
    var request = new XMLHttpRequest();
    request.open("POST", "http://192.168.16.70:5555/api/v2/registration/");
    request.setRequestHeader('Content-type', 'application/json; charset=utf-8');
    request.send(json);
    request.onload = () => console.log(request.response)
    request.onload = function () {
        if (request.status == "200") {
            console.log(request.json)
            document.write('Регистрация прошла успешно!');
    }
   
}
  };