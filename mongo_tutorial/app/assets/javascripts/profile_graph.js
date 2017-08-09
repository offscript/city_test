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

//Width and height
var finish_w = 500;
var finish_h = 100;

var dataset = [ 5, 10, 13, 19, 21, 25, 22, 18, 15, 13,
              11, 12, 15, 20, 18, 17, 16, 18, 23, 25 ];

//Grabs data profile data from the empty div
function profile_init() {
  club = $('.clubs_class').data('club')
}

function finish_graph() {
  //figure out a way to do this automatically... 
  var finish_array = [  [1, club["2012/13"]["finish"]], 
                        [2, club["2013/14"]["finish"]], 
                        [3, club["2014/15"]["finish"]],
                        [4, club["2015/16"]["finish"]],
                        [5, club["2016/17"]["finish"]]
                    ]

  var svg = d3.select("body")
            .append("svg")
            .attr("width", finish_w)
            .attr("height", finish_h);

      svg.selectAll("circle")
         .data(finish_array)
         .enter()
         .append("circle")
         .attr("x", function(d, i) {
            return i * 21;  //Bar width of 20 plus 1 for padding
         })
         .attr("y", 0)
         .attr("width", 20)
         .attr("height", 100);
}

function draw() {
  //club = $('.clubs_class').data('club')
  console.log(club["2012/13"]["finish"]);
}