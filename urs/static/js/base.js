function clickplace(place) {
    var xhr = new XMLHttpRequest();
    xhr.onload = function() {
        if(xhr.status==200){
            documenet.getElementById("expln").innerHTML = xhr.responseText;
        }
    };
    xhr.open('GET', 'bonwon/place', true); //요청 준비 - 방법/처리할페이지경로/비동기로할거
    xhr.send('place=place'); //요청 전송냐 - 여기서 서버 접속하고 응답 오면 위의 onload가 호출.

}
