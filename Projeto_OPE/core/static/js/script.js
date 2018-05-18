imgSrc = [
    {"imgNumber":"1","source":"{% static 'img/luoping.jpg' %}"},
    {"imgNumber":"2","source":"{% static 'img/planalto putorana-russia.jpg' %}"},
    {"imgNumber":"3","source":"{% static 'img/planalto putorana-russia2.jpg' %}"},
    {"imgNumber":"4","source":"{% static 'img/planalto putorana-russia3.jpg' %}"},
    {"imgNumber":"5","source":"{% static 'img/praia do silencio - espanha.jpg' %}"},
];


function toggleImgSrc(x){
    for(i=1;i<=5;i++){
        if(i == imgSrc[i]["imgNumber"]){
            Document.getElementById("carousel").src = imgSrc["source"];
        };
    };
};


/*var top5HL = document.getElementsByClassName("imgHighlight");
var top5Urls = document.getElementsByClassName("imgtop5");

function toggleHighlight(x){
    aux = top5Urls[x].src;
    top5Urls[x].src = top5HL.src;
    top5HL.src = aux;
};*/

function toggleHighlight2(z){
    var top5 = document.getElementsByClassName("itemtop5");
    var img5 = document.getElementsByClassName("imgtop5");
    for(i=0;i<=4;i++){
        if(top5[i].classList.contains("highlight")){
            top5[i].classList.remove("highlight");
            img5[i].classList.remove("imgHighlight");
        };
    };
    top5[z].classList.add("highlight");
    img5[z].classList.add("imgHighlight");
};

/*function fix_menu(){
    var top
    top = scrolltop()
    if (top < 0){
        document.getElementById("topMenu").style.position = "fixed";
    } else {
        document.getElementById("topMenu").style.position = "relative";
    }
}*/
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