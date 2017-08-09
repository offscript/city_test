/*$.ajax({
           type: "GET",
           contentType: "application/json; charset=utf-8",
           url: '11',
           dataType: 'json',
           success: function (data) {
               draw(data);
           },
           error: function (result) {
               error();
           }
       });
*/


function draw() {
  club = $('.clubs_class').data('club')
  console.log(club.club_name)
}

function error() {
  console.log("error")
}