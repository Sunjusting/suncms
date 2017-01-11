/**
Custom module for you to write your own javascript functions
**/
var Notif = function () {

    // private functions & variables

    var loadMessage = function(el) {
        var nid = el.attr('nid');
        var url = 'getNotification';
        $('.message-content').html('');
        $.get( url, {nid:nid}, function(json){
            var data = jQuery.parseJSON(json);
            var msg = '<h4>['+ data['type'] + '] ' + data['title']+'</h4>';
            msg += '<small>' + data['ctime'].substr(5,11) + ' | ';
            msg += '<small>发件人：' + data['sender'] + '</small> | ';
            msg += '<small>收件人：' + data['recipients'] + '</small>'
            msg += '<br><br><p>' + data['body'] + '</p>';
            $('.message-content').html(msg);
        });        
    }

    var updateUnreadCount = function(){
        var url = 'updateUnreadCount';
        $.get(url,function(count){
            $('.notif-count').html(count);
        });
    }

    // public functions
    return {

        //main function
        init: function () {
            //initialize here something.  
            $('.view-message').on('click',function(){
                loadMessage($(this));
                updateUnreadCount();
            });
        },

        //some helper function
        doSomeStuff: function () {
            myFunc();
        }

    };

}();

/***
Usage
***/
//Custom.init();
//Custom.doSomeStuff();