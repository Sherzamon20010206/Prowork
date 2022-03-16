function login11() {
    login = document.getElementById(`login`).value
    password = document.getElementById(`myInput`).value
    console.log(search_word)



        var url = `user/`
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
                            document.getElementById("ok").innerHTML=`<h1>Succsesful!</h1>`

                        }
                        else
                        {
                             document.getElementById("ok").innerHTML=`<h1>bad</h1>`
                        }







                    })

                }
            )



}