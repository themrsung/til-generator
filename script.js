function generateTIL() {
    var sentences = Number(document.getElementById("sentences").value)

    // $.ajax({
    //     type: "POST",
    //     url: "~/app.py",
    //     data: {param: text}
    // }).done(function(sentences) {
        
    // })

    document.getElementById("output").innerHTML = sentences
}