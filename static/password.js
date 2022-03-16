function myFunction() {
  var x = document.getElementById("myInput");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}
function sherzamon() {
    login = document.getElementById(`login`).value
    password = document.getElementById(`myInput`).value
    console.log(login,password)



        var url = `user_login/`
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'login':login,
                'password':password
            })
        })
            .then((response) => {
                    response.json().then((data) => {
                        data = data['data']
                        console.log(data)
                        if(data=='ok'){

                            location.href="/"




                        }
                        else
                        {
                             document.getElementById("ok1").innerHTML=`<h2>Login yoki parol noto'g'ri</h2>`
                        }








                    })

                }
            )



}
