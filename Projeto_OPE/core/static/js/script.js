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
    var uluru = {lat: -23.68620668, lng: -46.77054162};
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 18,
      center: uluru
    });
    var marker = new google.maps.Marker({
      position: uluru,
      map: map
    });
  }
/*
function urlinsta(){
    var frm = document.getElementById("instagram");
    frm.action = "https://api.instagram.com/oauth/access_token";
    return true;
}*/
function testeInsta(){
    var url
    url = "https://api.instagram.com/v1/users/self/media/recent/?access_token=3251373559.1556bce.467e8e9f0219425abf9915fa978bb275"
    
}