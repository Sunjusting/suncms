// ccpitcrm-common.js
// 公用的js方法

function getUrlHref(){
    var url = location.href;
    var x = url.indexOf("?");
    if(x!=-1){
        var href = url.substring(0,x);
    }else{
        var href = url;
    }
    return href;
}

function getUrlParaObj(){
    var url = location.search; //获取url中"?"符后的字串
    var theParaObj = new Object();
    if (url.indexOf("?") != -1) {
        var str = url.substr(1);
        strs = str.split("&");
        for(var i = 0; i < strs.length; i ++) {
            theParaObj[strs[i].split("=")[0]]=(strs[i].split("=")[1]);
        }
    }
    return theParaObj;
}

// 显示一个对象
function writeObj(obj){ 
    var description = ""; 
    for(var i in obj){   
        var property=obj[i];   
        description+=i+" = "+property+"\n";  
    }   
    alert(description); 
}

function makeUrlPara(paraObj){
    var paraStr = "";
    for(var i in paraObj){
        var property = paraObj[i];
        paraStr += i+"="+property+"&";
    }
    var x = paraStr.length;
    if(x>0){paraStr = paraStr.substring(0,x-1);}
    return paraStr;
}