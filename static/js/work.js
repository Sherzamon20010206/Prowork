function search() {
    search_word = document.getElementById(`search`).value
    console.log(search_word)
    if (search_word != "") {


        var url = `search_file/`
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'search':search_word
            })
        })
            .then((response) => {
                    response.json().then((data) => {
                        data = data['data']
                        console.log(data)
                                               html=``
                           for(let i=0;i<data.length;i++){
                         html2=`
                               
                          <div class="grid-item apps wow zoomIn">
                
                            <div class="img-place" data-src=${data[i]['img']} data-fancybox data-caption="<h5 class='fg-theme'>${"data[i]['title']"}</h5> <p>ProWork</p>">
                              <img src=${data[i]['img']} alt="">
                              <div class="img-caption">
                                <h5 class="fg-theme">${data[i]['title']}</h5>
                                <p>ProWork</p>
                              </div>
                            </div>
                            <b><a href=${data[i]['file']}  download=${data[i]['file']}>Download</a></b>
                          </div>`
                               html=html2+html
                                }






                        document.getElementById("javob").innerHTML = html




                    })

                }
            )
    }

    else {

        var url = `search_file/`
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'search': "pustoy"
            })
        })
            .then((response) => {
                    response.json().then((data) => {
                        data = data['data']
                        console.log(data)
                        html=``
                           for(let i=0;i<data.length;i++){
                         html2=`
                               
                          <div class="grid-item apps wow zoomIn">
                
                            <div class="img-place" data-src=${data[i]['img']} data-fancybox data-caption="<h5 class='fg-theme'>${data[i]['title']}</h5> <p>ProWork</p>">
                              <img src=${data[i]['img']} alt="">
                              <div class="img-caption">
                                <h5 class="fg-theme">${data[i]['title']}</h5>
                                
                              </div>
                            </div>
                            <b><a href=${data[i]['file']}  download=${data[i]['file']}>Download</a></b>
                          </div>`
                               html=html2+html
                                }






                        document.getElementById("javob").innerHTML = html

                    })

                }
            )






    }


}