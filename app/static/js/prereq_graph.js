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