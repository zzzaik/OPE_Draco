function SubmitFormEnviarToken(){
    document.getElementById("formEnviarToken").submit();
}

function SubmitFormReSenha(){
    document.getElementById("formReSenha").submit();
}

function SubmitFormLogin(){
    document.getElementById("formLogin").submit();
    //toggleDisplayNone();
}

function SubmitFormCadastro(){
    document.getElementById("formCadastro").submit();
}


function SubmitFormInfoUser(){
    let text = document.getElementById("btn1");
    text.innerHTML='Disabled';
}

function toggleDisplayNone() {
    let div = document.getElementById("clientPage");
    let login = document.getElementById("loginDiv");
    if (div.classList.contains("displayNone")) {
        div.classList.remove("displayNone");
        login.classList.add("displayNone");
    }
}

function toggleHighlight2(z){
    let top5 = document.getElementsByClassName("itemtop5");
    let img5 = document.getElementsByClassName("imgtop5");
    for(i=0;i<=4;i++){
        if(top5[i].classList.contains("highlight")){
            top5[i].classList.remove("highlight");
            img5[i].classList.remove("imgHighlight");
        };
    };
    top5[z].classList.add("highlight");
    img5[z].classList.add("imgHighlight");
};

function initMap() {
    var uluru = {lat: -23.68625006, lng: -46.77043178};
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 18,
      center: uluru
    });
    var marker = new google.maps.Marker({
      position: uluru,
      map: map
    });
  };
/*
function urlinsta(){
    var frm = document.getElementById("instagram");
    frm.action = "https://api.instagram.com/oauth/access_token";
    return true;
}*/
