$.ajaxSetup({
    beforeSend: function beforeSend(xhr, settings) {
        function getCookie(name) {
            let cookieValue = null;


            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');

                for (let i = 0; i < cookies.length; i += 1) {
                    const cookie = jQuery.trim(cookies[i]);

                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (`${name}=`)) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }

            return cookieValue;
        }

        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
        }
    },
});

//adding jquery to the modal

$(document).on("click",".js-modal-toggle",function(event){
    event.preventDefault()
    $(".js-modal").toggleClass("hidden")

    .on("click",".js-submit",function(event){
        event.preventDefault()

        //get text area text
        const text=$(".js-post-text").val()
       
        //enable hiding of the modal ONLY when there is some text in the textarea
        if (text.length === 0){
            $("js-submit").prop("disabled",true) //disable button if text length is zero
            
            return false
           
        }else{
            $(".js-modal").addClass("hidden")
            $(".js-post-text").val(" ") //remove  previous text after clicking js-submit button
        }
        //ajax request
        $.ajax({
            type:"POST",
            url:$(".js-post-text").data("post-url"), //go to the base.html textarea and look for the url in data-post-url
            data:{
                text:text
            },
            success:(dataHtml)=>{
                $(".js-modal").addClass("hidden")
                $(".post-container").prepend(dataHtml); //container in the feed/templates/homepage.html
                console.log("post added")

            }, 
            error:(error)=>{
                console.log(error)
                $("js-submit").text("Error")
            }
        })
        
    })
    
});

