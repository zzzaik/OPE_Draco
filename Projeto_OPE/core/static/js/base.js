function fix_menu(){
    var top
    top = scrolltop()
    if (top < 0){
        document.getElementById("topMenu").style.position = "fixed";
    } else {
        document.getElementById("topMenu").style.position = "relative";
    }
}