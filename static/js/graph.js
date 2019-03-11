queue()
   .defer(d3.csv, "data/wise.csv")
  .await(makeGraphs);
  
  function makeGraphs(error, wiseData) {
    var ndx = crossfilter(wiseData);
      
    show_discoveryYear(ndx);
    show_PHA_data(ndx);
       
    show_class(ndx);
    
    dc.renderAll();
    
}
   
function show_containsMeat(ndx) {
    dim = ndx.dimension(dc.pluck('contains_meat'));
    group = dim.group();
    
    dc.selectMenu("#vegetarian-selector")
    .dimension(dim)
    .group(group);
}
   


function show_food_type(ndx) {

var food_type_dim = ndx.dimension(dc.pluck('food_type'));
var total_vegeterian_per_food_type = food_type_dim.group();
dc.pieChart('#category-data')
            .height(530)
            .radius(290)
            .transitionDuration(1500)
            .dimension(food_type_dim)
            .group(total_vegeterian_per_food_type);

}
