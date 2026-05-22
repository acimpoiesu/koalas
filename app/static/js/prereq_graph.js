async function createPrereqTree() {
    var raw = await d3.json("/api/courses");
    var treeData = {
        name: "Requirements tree",
        children: []
    };

    var subs = [];
    for (var i = 0; i < raw.length; i++) {
        if (subs.indexOf(raw[i].course_subject) === -1) {
            subs.push(raw[i].course_subject);
        }
    }

    subs.forEach(function(s) {
        treeData.children.push({ name: s, children: [] });
    });

    raw.forEach(function(c) {
        var node = treeData.children.find(function(n) { return n.name === c.course_subject; });
        var p = [];
        if (c.prereqs) {
            p = JSON.parse(c.prereqs);
        }
        
        node.children.push({
            name: c.course_code,
            title: c.course_name,
            children: p.map(function(val) { return { name: val }; })
        });
    });

    var w = document.getElementById("graph-container").clientWidth;
    var h = 600;
    var rootNode = d3.hierarchy(treeData);
    var treeLayout = d3.tree().nodeSize([15, w / 4]);
    treeLayout(rootNode);

    var svg = d3.select("#graph-container").append("svg")
        .attr("width", "100%")
        .attr("height", h + "px")
        .style("font", "10px sans-serif")
        .call(d3.zoom().on("zoom", function(e) {
            d3.select("#main-group").attr("transform", e.transform);
        }));

    var mainG = svg.append("g")
        .attr("id", "main-group")
        .attr("transform", "translate(" + (w/4) + ", 15)");
        
    mainG.append("g")
        .attr("fill", "none")
        .attr("stroke", "#555")
        .attr("stroke-opacity", 0.4)
      .selectAll("path")
      .data(rootNode.links())
      .enter().append("path")
        .attr("d", d3.linkHorizontal().x(function(d) { return d.y; }).y(function(d) { return d.x; }));

    var nodes = mainG.append("g")
      .selectAll("g")
      .data(rootNode.descendants())
      .enter().append("g")
        .attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; });

    nodes.append("circle")
        .attr("r", 2.5)
        .attr("fill", function(d) { return d.children ? "#555" : "#999"; });

    nodes.append("text")
        .attr("dy", "0.31em")
        .attr("x", function(d) { return d.children ? -6 : 6; })
        .attr("text-anchor", function(d) { return d.children ? "end" : "start"; })
        .text(function(d) { return d.data.name; })
        .attr("fill", "#14b8a6");
}

createPrereqTree();