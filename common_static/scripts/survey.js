/**
Custom module for you to write your own javascript functions
**/
function writeObj(obj){ 
    var description = ""; 
    for(var i in obj){   
        var property=obj[i];   
        description+=i+" = "+property+"\n";  
    }   
    alert(description); 
}


var Survey = function () {

    // private functions & variables

    var myFunc = function(text) {
        alert(text);
    }

    var makeUrl = function(url){
        // return "http://localhost/ccpitcrm"+url;        
        return "http://qiyeshujuku.ccpit.org"+url;
    }


    // public functions
    return {

        //main function
        init: function () {
            //initialize here something.            
        },

        //some helper function
        doSomeStuff: function () {
            myFunc();
        },

        doAddQuestion: function() {            
            $(".more-block-1").hide();
            $(".more-1").click(function(){
                $(".more-block-1").show();
            });
            $(".more-block-2").hide();
            $(".more-2").click(function(){
                $(".more-block-2").show();
            });
            $(".more-block-4").hide();
            $(".more-4").click(function(){
                $(".more-block-4").show();
            });
            $(".more-block-5").hide();
            $(".more-5").click(function(){
                $(".more-block-5").show();
            });


            $(".cancel-btn").click(function(){
                history.back();          
            });

            $("#submit1").click(function(url){
                var sid = $(".sid1").val();
                var type = $(".type1").val();
                var sort = $(".sort1").val();
                var question = $(".question1").val();
                var remark = $(".remark1").val();
                var showtype = $(".showtype1").find(".checked").find("input").val();                
                var url = makeUrl("/Survey/doAddQuestion");

                var select = new Array();
                var select1 = $("input[name^='select1_'");
                var i = 1;
                var select_json = '';
                select1.each(function(){
                    var x = $(this).val();  
                    select_json = select_json + '"select_' + i + '":"' + x + '",';
                    i = i+1;
                });
               
                select_json = select_json.substring(0,select_json.length-1);
                select_json = "{" + select_json + "}";
                                
                $.post( url, {sid:sid,type:type,sort:sort,question:question,remark:remark,showtype:showtype,select_json:select_json}, function(text){
                    if(text=="1"){
                        alert("Good, Add Question Successfully!");
                    }else{
                        alert('Ooops, Error');
                    }
                    window.location.href = makeUrl('/Survey/listQuestions/sid/'+sid);
                });
                
                
            });

            $("#submit2").click(function(url){
                var sid = $(".sid2").val();
                var type = $(".type2").val();
                var sort = $(".sort2").val();
                var question = $(".question2").val();
                var remark = $(".remark2").val();
                var showtype = $(".showtype2").find(".checked").find("input").val();
                var url = makeUrl("/Survey/doAddQuestion");


                var select = new Array();
                var select2 = $("input[name^='select2_'");
                var i = 1;
                var select_json = '';
                select2.each(function(){
                    var x = $(this).val();  
                    select_json = select_json + '"select_' + i + '":"' + x + '",';
                    i = i+1;
                });
               
                select_json = select_json.substring(0,select_json.length-1);
                select_json = "{" + select_json + "}";
                                
                $.post( url, {sid:sid,type:type,sort:sort,question:question,remark:remark,showtype:showtype,select_json:select_json}, function(text){
                    if(text=="1"){
                        alert("Good, Add Question Successfully!");
                    }else{
                        alert('Ooops, Error');
                    }
                    window.location.href = makeUrl('/Survey/listQuestions/sid/'+sid);
                });               
            });

            $("#submit3").click(function(url){
                var sid = $(".sid3").val();
                var type = $(".type3").val();
                var sort = $(".sort3").val();
                var question = $(".question3").val();
                var remark = $(".remark3").val();
                var showtype = $(".showtype3").find(".checked").find("input").val();

                var url = makeUrl("/Survey/doAddQuestion");
                $.post( url, { sid:sid, type:type, sort:sort, question:question, remark:remark,showtype:showtype}, function(text){
                    if(text=="1"){
                        alert("Good, Add Question Successfully!");
                    }else{
                        alert('Ooops, Error');
                    }
                    window.location.href = makeUrl('/Survey/listQuestions/sid/'+sid);
                });
                
            });

            $("#submit4").click(function(url){
                var sid = $(".sid4").val();
                var type = $(".type4").val();
                var sort = $(".sort4").val();
                var question = $(".question4").val();
                var remark = $(".remark4").val();
                var showtype = $(".showtype4").find(".checked").find("input").val();
                var ext_question = $(".ext_question").val();
                var url = makeUrl("/Survey/doAddQuestion");


                var select = new Array();
                var select4 = $("input[name^='select4_'");
                var i = 1;
                var select_json = '';
                select4.each(function(){
                    var x = $(this).val();  
                    select_json = select_json + '"select_' + i + '":"' + x + '",';
                    i = i+1;
                });
               
                select_json = select_json.substring(0,select_json.length-1);
                select_json = "{" + select_json + "}";
                         
                
                $.post( url, {sid:sid,type:type,sort:sort,question:question,remark:remark,showtype:showtype,select_json:select_json,ext_question:ext_question}, function(text){
                    if(text=="1"){
                        alert("Good, Add Question Successfully!");
                    }else{
                        alert('Ooops, Error');
                    }
                    window.location.href = makeUrl('/Survey/listQuestions/sid/'+sid);
                });
                

            });

            $("#submit5").click(function(url){
                var sid = $(".sid5").val();
                var type = $(".type5").val();
                var sort = $(".sort5").val();
                var question = $(".question5").val();
                var remark = $(".remark5").val();
                var showtype = $(".showtype5").find(".checked").find("input").val();
                var ext_question = $(".ext_question_5").val();
                var url = makeUrl("/Survey/doAddQuestion");

                var select = new Array();
                var select5 = $("input[name^='select5_'");
                var i = 1;
                var select_json = '';
                select5.each(function(){
                    var x = $(this).val();  
                    select_json = select_json + '"select_' + i + '":"' + x + '",';
                    i = i+1;
                });
               
                select_json = select_json.substring(0,select_json.length-1);
                select_json = "{" + select_json + "}";                         
                
                $.post( url, {sid:sid,type:type,sort:sort,question:question,remark:remark,showtype:showtype,select_json:select_json,ext_question:ext_question}, function(text){
                    if(text=="1"){
                        alert("Good, Add Question Successfully!");
                    }else{
                        alert('Ooops, Error');
                    }
                    window.location.href = makeUrl('/Survey/listQuestions/sid/'+sid);
                });
                
            });

        },

        doEditQuestion: function() { 

            $(".cancel-btn").click(function(){
                history.back();          
            });

            $("#submit-1").click(function(){

                var qid = $(".qid-1").val();                
                var sid = $(".sid-1").val();
                var type = $(".type-1").val();
                var sort = $(".sort1").val();
                var question = $(".question1").val();
                var remark = $(".remark1").val();
                var showtype = $(".showtype1").find(".checked").find("input").val();
                var url = makeUrl("/Survey/doEditQuestion");


                var select = new Array();
                var select1 = $("input[name^='select1_'");
                var i = 1;
                var select_json = '';
                select1.each(function(){
                    var x = $(this).val();  
                    select_json = select_json + '"select_' + i + '":"' + x + '",';
                    i = i+1;
                });
               
                select_json = select_json.substring(0,select_json.length-1);
                select_json = "{" + select_json + "}";
                                
                $.post( url, {qid:qid,sid:sid,type:type,sort:sort,question:question,remark:remark,showtype:showtype,select_json:select_json}, function(text){
                    if(text=="1"){
                        alert("Good, Edit Question Successfully!");
                    }else{
                        alert('Ooops, Error');
                    }
                    window.location.href = makeUrl('/Survey/listQuestions/sid/'+sid);
                });
                
                
            });

            $("#submit-2").click(function(){
                var qid = $(".qid-2").val(); 
                var sid = $(".sid-2").val();
                var type = $(".type-2").val();
                var sort = $(".sort2").val();
                var question = $(".question2").val();
                var remark = $(".remark2").val();
                var showtype = $(".showtype2").find(".checked").find("input").val();
                var url = makeUrl("/Survey/doEditQuestion");


                var select = new Array();
                var select2 = $("input[name^='select2_'");
                var i = 1;
                var select_json = '';
                select2.each(function(){
                    var x = $(this).val();  
                    select_json = select_json + '"select_' + i + '":"' + x + '",';
                    i = i+1;
                });
               
                select_json = select_json.substring(0,select_json.length-1);
                select_json = "{" + select_json + "}";        
                
                $.post( url, {qid:qid,sid:sid,type:type,sort:sort,question:question,remark:remark,showtype:showtype,select_json:select_json}, function(text){
                    if(text=="1"){
                        alert("Good, Edit Question Successfully!");
                    }else{
                        alert('Ooops, Error');
                    }
                    window.location.href = makeUrl('/Survey/listQuestions/sid/'+sid);
                });
                
                
            });

            $("#submit-3").click(function(){
                var qid = $(".qid-3").val(); 
                var sid = $(".sid-3").val();
                var type = $(".type-3").val();
                var sort = $(".sort3").val();
                var question = $(".question3").val();
                var remark = $(".remark3").val();
                var showtype = $(".showtype3").find(".checked").find("input").val();

                var url = makeUrl("/Survey/doEditQuestion");
                $.post( url, { qid:qid,sid:sid, type:type, sort:sort, question:question, remark:remark,showtype:showtype}, function(text){
                    if(text=="1"){
                        alert("Good, Edit Question Successfully!");
                    }else{
                        alert('Ooops, Error');
                    }
                    window.location.href = makeUrl('/Survey/listQuestions/sid/'+sid);
                });

                
            });

            $("#submit-4").click(function(){
                var qid = $(".qid-4").val();
                var sid = $(".sid-4").val();
                var type = $(".type-4").val();
                var sort = $(".sort4").val();
                var question = $(".question4").val();
                var remark = $(".remark4").val();
                var showtype = $(".showtype4").find(".checked").find("input").val();
                var ext_question = $(".ext_question").val();
                var url = makeUrl("/Survey/doEditQuestion");


                var select = new Array();
                var select4 = $("input[name^='select4_'");
                var i = 1;
                var select_json = '';
                select4.each(function(){
                    var x = $(this).val();  
                    select_json = select_json + '"select_' + i + '":"' + x + '",';
                    i = i+1;
                });
               
                select_json = select_json.substring(0,select_json.length-1);
                select_json = "{" + select_json + "}";
                         
                
                $.post( url, {qid:qid,sid:sid,type:type,sort:sort,question:question,remark:remark,showtype:showtype,select_json:select_json,ext_question:ext_question}, function(text){
                    if(text=="1"){
                        alert("Good, Edit Question Successfully!");
                    }else{
                        alert('Ooops, Error');
                    }
                    window.location.href = makeUrl('/Survey/listQuestions/sid/'+sid);
                });
                
                
            });

            $("#submit-5").click(function(){
                var qid = $(".qid-5").val();
                var sid = $(".sid-5").val();
                var type = $(".type-5").val();
                var sort = $(".sort5").val();
                var question = $(".question5").val();
                var remark = $(".remark5").val();
                var showtype = $(".showtype5").find(".checked").find("input").val();
                var ext_question = $(".ext_question").val();
                var url = makeUrl("/Survey/doEditQuestion");


                var select = new Array();
                var select5 = $("input[name^='select5_'");
                var i = 1;
                var select_json = '';
                select5.each(function(){
                    var x = $(this).val();  
                    select_json = select_json + '"select_' + i + '":"' + x + '",';
                    i = i+1;
                });
               
                select_json = select_json.substring(0,select_json.length-1);
                select_json = "{" + select_json + "}";
                         
                
                $.post( url, {qid:qid,sid:sid,type:type,sort:sort,question:question,remark:remark,showtype:showtype,select_json:select_json,ext_question:ext_question}, function(text){
                    if(text=="1"){
                        alert("Good, Edit Question Successfully!");
                    }else{
                        alert('Ooops, Error');
                    }
                    window.location.href = makeUrl('/Survey/listQuestions/sid/'+sid);
                });
                
                
            });


        }

    };

}();

