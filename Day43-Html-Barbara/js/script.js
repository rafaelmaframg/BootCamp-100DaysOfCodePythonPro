var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
    console.log("hello")
var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("menu").style.top = "0";
  } else {
    document.getElementById("menu").style.top = "-50px";
  }
  prevScrollpos = currentScrollPos;
}
