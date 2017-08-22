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
                    ];

  var svg = d3.select("div.col.s12.m9.l10") //check here
            .append("svg")
            .attr("width", finish_w + 100)
            .attr("height", finish_h + 100);


  var xScale = d3.scaleLinear()
                .domain([2011, 2016])
                .range([0, finish_w]);

  var yScale = d3.scaleLinear()
                .domain([1, 20])
                .range([0, finish_h]);

/**
  var svg = d3.select("div.col.s12.m9.l10") //check here
            .append("svg")
            .attr("width", finish_w + 100)
            .attr("height", finish_h + 100);

      svg.selectAll("circle")
         .data(finish_array)
         .enter()
         .append("circle")
         .attr("cx", function(d) {
            return xScale(d[0]);
          })
         .attr("cy", function(d) {
              return yScale(d[1]);
         })
         .attr("r", 5);

    console.log('executed');
    //return svg;

    var xAxis = d3.axisBottom(xScale).ticks(5).tickValues(["2012", "2013", "2014", "2015", "2016"]);
                  //.ticks(5)
                  

    d3.select("div.col.s12.m9.l10")
    svg.append("g")
      .attr("transform", "translate(0," + finish_h + ")")
      .call(xAxis);

    **/

}

function draw() {
  //club = $('.clubs_class').data('club')
  console.log(club["2012/13"]["finish"]);
}