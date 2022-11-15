function generateTIL() {
    var sentences = Number(document.getElementById("sentences").value)

    var result = error

    $.ajax({
        type: "GET",
        url: "/til",
        data: {sentences_give : sentences},
        success: function(response) {
            result = response["TIL"]
        }
    })

    document.getElementById("output").innerHTML = result
}