function LeftSideBarIn(){
    document.getElementById("LeftSideBarImg").setAttribute(
           "style", "filter: blur(0); -webkit-filter: blur(0); -moz-filter: blur(0); -o-filter: blur(0); -ms-filter: blur(0); transform:scale(1.00);");
    }
    function LeftSideBarOut(){
        document.getElementById("LeftSideBarImg").setAttribute(
           "style", "filter: blur(0.156vw); -webkit-filter: blur(0.156vw); -moz-filter: blur(0.156vw); -o-filter: blur(0.156vw); -ms-filter: blur(0.156vw); transform:scale(1.05);");
    }
    function RightSideBarIn(){
    document.getElementById("RightSideBarimg").setAttribute(
           "style", "filter: blur(0); -webkit-filter: blur(0); -moz-filter: blur(0); -o-filter: blur(0); -ms-filter: blur(0); transform:scale(1.00);");
    }
    function RightSideBarOut(){
        document.getElementById("RightSideBarimg").setAttribute(
           "style", "filter: blur(0.156vw); -webkit-filter: blur(0.156vw); -moz-filter: blur(0.156vw); -o-filter: blur(0.156vw); -ms-filter: blur(0.156vw); transform:scale(1.05);");
    }