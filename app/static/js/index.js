$(document).ready(function(){
    var socket = io();

    var index_local = 1;

    btn_1 = ".main .webcam .webcam__btn .webcam__btn_1 button"
    btn_2 = ".main .webcam .webcam__btn .webcam__btn_2 button"
    contro = ".main .webcam .webcam__contro .cam__contro p"

    $(btn_1).click(function(){
        socket.emit('on_camera',"turn_on")
        $(contro).html("Camera: ON")
        $(".main .webcam .webcam__show .img").html("<p>"+"Đang bật Camera!"+"</p>")
    })
    $(btn_2).click(function(){
        socket.emit('on_camera',"turn_of")
        $(contro).html("Camera: OFF")
        $(".main .webcam .webcam__contro .model__contro p").html("Detect: OFF")
        $(".main .webcam .phat_thanh").html("");
        $(".main .webcam .thong_bao_phat_thanh p").html("")
    })
    socket.on('get_img',function(img){
        $(".main .webcam .webcam__show .img").html("<img src=data:image/png;base64,"+img+">")
    })
    socket.on('get_not_img',function(text_){
        $(".main .webcam .webcam__show .img").html("<p>"+text_+"</p>")
        $(".main .webcam .webcam__text .text").html("<p>"+"</p>")
    })
    socket.on('get_text',function(text){
        let arr = text.split('');
        if (arr[(arr.length)-1]=="_"){
            text = ''
            for(let i=0;i<(arr.length)-1;i++){
                text+=arr[i]
            }
            socket.emit("debug_ok_","no")
            $(".main .webcam .thong_bao_phat_thanh p").html("Đang tạo âm thanh!")
            socket.emit('phat_thanh',text)
            console.log(text)
        }
        $(".main .webcam .webcam__text .text p").html(text)
    })
    socket.on('audio_complete',function(text){
        try{
            $(".main .webcam .phat_thanh").html("<audio id=myAudio "+" controls "+"src=/static/audio.mp3?v="+index_local.toString()+"></audio>");
            console.log("<audio id=myAudio "+" controls "+"src=/static/audio.mp3?v="+index_local.toString()+"></audio>")
            index_local+=1
            var x = document.getElementById("myAudio");
            x.play()
            $(".main .webcam .thong_bao_phat_thanh p").html("Đang phát âm thanh!")
            $('#myAudio').on('ended', function() {
                socket.emit("delete_"," ")
                $(".main .webcam .thong_bao_phat_thanh p").html("Đã phát xong!")
                $(".main .webcam .thong_bao_phat_thanh p").html("")
                $(".main .webcam .phat_thanh").html("");
                socket.emit("debug_ok_","yes")
                // socket.emit("end_task",".")
                // socket.emit('on_camera',"turn_of")
                // $(contro).html("Camera: OFF")
                // $(".main .webcam .webcam__text .text").html("<p>"+"</p>")
                $(".main .webcam .webcam__text .text").html("<p>"+"</p>")
            });
        }catch{
            socket.emit('phat_thanh',text)
            console.log("loi file audio dang tao lai file - loi do modelApi")
        }
    })
    socket.on('get_deley_time',function(text){
        $(".main .webcam .webcam__contro .model__contro p").html("Detect: "+text)
    })
    
})