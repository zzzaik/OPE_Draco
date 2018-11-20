function saveCatalogo () {
    let data = [];
    let images = $("name=semClassificacao");
    for(let i=0;i<images.length;i++){
        imgId = images.children[0].value
        estilo = images.children[2].val()
        data.push({'imgId': imgId,'estilo':estilo})
    };

    $.ajax({
        url:'http://zzzaik.pythonanywhere.com/tatuador/gestao_catalogo/save_catalogo',
        type:'POST',
        contentType:'application/json; charset=utf-8',
        data: $.toJSON(data),
        dataType: 'text',
        success: function(result){
            alert(result.Result);
        }
    });
}

$("#btnTest").click(function() {
    alert("<span>Testo de texte</span>");
    }
    /*$.getJSON('core/backend/dataJson.py', function(json) {
    return json
    }))*/
);

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
    let text = document.getElementById("btnSalvarFormUser");
    text.innerHTML='Disabled';

    let btnSave = document.getElementById("btnSalvarFormUser");
    let inputs = document.getElementsByTagName("input");
    for (let i=0; i<inputs.length;i++) {
        if (!inputs[i].disabled) {
            inputs[i].disabled = true;
        }
    }
    let txt = document.getElementsByTagName("textarea");
    txt[0].disabled = true;
    if (!btnSave.classList.contains("displayNone")) {
        btnSave.classList.add("displayNone");
    }
}

function AtualizarFormInfoUser(){
    let inputs = document.getElementsByTagName("input");
    for (let i=0; i<inputs.length;i++) {
        if (inputs[i].disabled) {
            inputs[i].disabled = false;
        }
    }
    let txt = document.getElementsByTagName("textarea");
    txt[0].disabled = false;
    let btnSave = document.getElementById("btnSalvarFormUser");
    if (btnSave.classList.contains("displayNone")) {
        btnSave.classList.remove("displayNone")
    }
}

function showMore(id) {
    let displayElements = document.getElementById(id).children
    for (let i=0;i<displayElements.length;i++) {
        if (displayElements.classList.contains("displayNone")) {
            displayElements.classList.remove("displayNone")
        }
    }
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

function loadClassificacao() {

}
/*
function urlinsta(){
    var frm = document.getElementById("instagram");
    frm.action = "https://api.instagram.com/oauth/access_token";
    return true;
}*/
