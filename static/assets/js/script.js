window.onscroll = function () {
    myFunction();
};

let data = {{ other_data|safe }}
for (let i = 0; i < data.length; i++) {
    var n = data[i]
    let speed = $("#" + n.id);
    let updatedSpeedd
    updatedSpeedd = Math.round(n.performance * 180 / 100) - 45;
    $("#speedbox-score-" + n.id).css("transform", "rotate(" + updatedSpeedd + "deg)");
 }