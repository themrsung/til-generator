function generateTIL() {
    var sentences = document.getElementById("sentences").value

    if (sentences < 1) {
        document.getElementById("output").innerHTML = "1 이상의 정수를 입력해주세요."
        return
    }

    $.ajax({
        type: "POST",
        url: "/til",
        data: {sentences_give : sentences},
        success: function(response) {
            document.getElementById("output").innerHTML = response["TIL"]
            console.log("t")
        }
    })
}