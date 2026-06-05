async function createPrereqGraph() {
    const rawData = await d3.json("/api/courses");
    
    let nodes = [];
    let links = [];
    let nodeMap = new Map();

    rawData.forEach(c => {
        let node = {
            id: c.course_code,
            name: c.course_name,
            subject: c.course_subject,
            prereqs_raw: c.prereqs
        };
        nodes.push(node);
        nodeMap.set(c.course_code, node);
    });

    nodes.forEach(node => {
        if (node.prereqs_raw) {
            try {
                let reqs = JSON.parse(node.prereqs_raw);
                reqs.forEach(req => {
                    if (req.type === 'passed') {
                        req.courses.forEach(reqCode => {
                            links.push({ source: reqCode, target: node.id });
                            if (!nodeMap.has(reqCode)) {
                                let dummy = { id: reqCode, name: "External/Unknown Course", subject: "Other" };
                                nodes.push(dummy);
                                nodeMap.set(reqCode, dummy);
                            }
                        });
                    }
                });
            } catch(e) {
                console.error("Error parsing prereq for " + node.id, e);
            }
        }
    });
    const container = document.getElementById("graph-container");
    const width = container.clientWidth;
    const height = container.clientHeight || 600;

    d3.select("#graph-container").html("");

    const svg = d3.select("#graph-container").append("svg")
        .attr("width", width)
        .attr("height", height)
        .call(d3.zoom().on("zoom", (e) => {
            svgGroup.attr("transform", e.transform);
        }));
    const svgGroup = svg.append("g");
    svg.append("defs").append("marker")
        .attr("id", "arrowhead")
        .attr("viewBox", "-0 -5 10 10")
        .attr("refX", 22)
        .attr("refY", 0)
        .attr("orient", "auto")
        .attr("markerWidth", 6)
        .attr("markerHeight", 6)
        .attr("xoverflow", "visible")
        .append("svg:path")
        .attr("d", "M 0,-5 L 10 ,0 L 0,5")
        .attr("fill", "#9ca3af")
        .style("stroke","none");

    const simulation = d3.forceSimulation(nodes)
        .force("link", d3.forceLink(links).id(d => d.id).distance(120))
        .force("charge", d3.forceManyBody().strength(-400))
        .force("center", d3.forceCenter(width / 2, height / 2))
        .force("collide", d3.forceCollide().radius(40));

    const link = svgGroup.append("g")
        .attr("class", "links")
        .selectAll("line")
        .data(links)
        .enter().append("line")
        .attr("stroke-width", 2)
        .attr("stroke", "#e5e7eb")
        .attr("marker-end", "url(#arrowhead)");

    const color = d3.scaleOrdinal(d3.schemeCategory10);

    const node = svgGroup.append("g")
        .attr("class", "nodes")
        .selectAll("g")
        .data(nodes)
        .enter().append("g")
        .call(d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended));

    node.append("circle")
        .attr("r", 15)
        .attr("fill", d => d.subject === "Other" ? "#d1d5db" : color(d.subject))
        .attr("stroke", "#fff")
        .attr("stroke-width", 2)
        .style("cursor", "grab");

    node.append("text")
        .text(d => d.id)
        .attr("x", 20)
        .attr("y", 4)
        .style("font-family", "system-ui, sans-serif")
        .style("font-size", "12px")
        .style("font-weight", "600")
        .style("fill", "#374151")
        .style("pointer-events", "none");

    node.append("title")
        .text(d => d.name + " (" + d.subject + ")");

    simulation.on("tick", () => {
        link
            .attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y);
        node
            .attr("transform", d => `translate(${d.x},${d.y})`);
    });

    function dragstarted(event, d) {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
        d3.select(this).select("circle").style("cursor", "grabbing");
    }

    function dragged(event, d) {
        d.fx = event.x;
        d.fy = event.y;
    }

    function dragended(event, d) {
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
        d3.select(this).select("circle").style("cursor", "grab");
    }
}

createPrereqGraph();