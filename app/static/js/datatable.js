$(document).ready(function(){
      var date_from=$('input[name="date_from"]'); //our date input has the name "date"
      var date_to=$('input[name="date_to"]');
      var options={
        format: 'dd.mm.yyyy',
        orientation: "left top",
        todayHighlight: true,
        autoclose: true,
      };
      date_from.datepicker(options);
      date_to.datepicker(options);
    });

$(document).ready(function() {
  setTimeout(function() {
    $("#message").slideUp('slow');
  }, 5000);
});

// function call_modal() { 
//   $("#exampleModal").modal();
// }

// function getQuestions() {
//           $.getJSON('/admin.sli.do/events/questions', {
//           }, function(data) {
//           output = ""
//           for (var i = 0; i < data.length; i++) {
//             output +="<div class='container' id='card'>"
//             output +="<div class='row justify-content-md-center'>"
//             output +="<div class='col-sm col-md-8 col-lg-6'>"
//             output +="<div class='card shadow bg-white'>"
//             output +="<div class='card-body text-secondary'>"
//             output += "<i class='fa fa-user-circle fa-2x'></i>"
//             output += "<p class='card-text1'>" + data[i].username + "</p>"
//             output += "<p class='card-text2'>" + data[i].registered_on + "</p>"
//             output += "<p class='card-text'>" + data[i].question + "</p>"
//             output += "</div>"
//             output += "</div>"
//             output += "</div>"
//             output += "</div>"
//             output += "</div>"
//           };
//           $('#questions').html(output)
//       });
//       }
//       getQuestions();
//       setInterval(function(){
//         // getQuestions();
//   }, 3000);
