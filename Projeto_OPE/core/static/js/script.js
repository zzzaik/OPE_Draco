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
/*
function fix_menu(){
    var top
    top = scrolltop()
    document.write(top)
    if (top < 0){
        document.getElementById("topMenu").style.position = "fixed";
        document.getElementById("topMenu").style.top = "0";
    } else {
        document.getElementById("topMenu").style.position = "relative";
    };
};
*/
