import React, { useEffect, useState } from "react";
import * as d3 from "d3";
import "./App.css";

const App = () => {
  const [code, setCode] = useState(""); // State for Python code input
  const [astData, setAstData] = useState(null); // State for AST data

  useEffect(() => {
    // Generate AST data
    const data = generateASTData();
    setAstData(data);
  }, []);

  // Function to generate AST data (replace with actual logic)
  const generateASTData = () => ({
    type: null,
    value: "=",
    children: [
      {
        type: "Identifier",
        value: "a",
        children: [],
      },
      {
        type: "Operator",
        value: "+",
        children: [
          {
            type: "Number",
            value: 10,
            children: [],
          },
          {
            type: "Number",
            value: 5,
            children: [],
          },
        ],
      },
    ],
  });

  // Function to handle code input change
  const handleCodeChange = (e) => {
    setCode(e.target.value);
  };

  // Function to handle generating AST data
  const handleGenerateAST = () => {
    const data = generateASTData(); // Replace this with actual logic to generate AST from Python code
    setAstData(data);
  };

  // D3 code for AST visualization
  useEffect(() => {
    if (!astData) return;

    const width = 800;
    const height = 800;

    d3.select("#tree-area svg").remove();

    const svg = d3
      .select("#tree-area")
      .append("svg")
      .attr("width", width)
      .attr("height", height)
      .append("g");

    const g = svg
      .append("g")
      .attr("transform", `translate(${width / 3}, ${height / 3})`);

    const treeLayout = d3.tree().size([300, 300]);

    const rootNode = d3.hierarchy(astData);
    const treeData = treeLayout(rootNode);

    const links = g
      .selectAll(".link")
      .data(treeData.links());

    const linkEnter = links
      .enter()
      .append("path")
      .attr("class", "link")
      .attr("d", d3.linkVertical()
      .x(d => d.x)
      .y(d => d.y)
      );

      linkEnter
      .merge(links)
      .attr("d", d3.linkVertical().x(d => d.x).y(d => d.y));
      links.exit().remove();

    const nodes = g
      .selectAll(".node")
      .data(treeData.descendants(),  d => d.data.id);
      const nodeEnter = nodes
      .enter()
      .append("g")
      .attr("class", "node")
      .attr("transform", d => `translate(${d.x},${d.y})`);

    nodeEnter.append("circle")
      .attr("r", 20)
      .attr("fill", "white")
      .attr("stroke", "black");

    nodeEnter
      .append("text")
      .attr("dy", "0.35em")
      .attr("font-size", "25px")
      .style("text-anchor", "middle")
      .text(d => d.data.value || "");

    nodeEnter.append("title")
    .text(d =>  d.data.type + (d.data.value ? ": " + d.data.value : ""));

     
  // Add expand/collapse functionality
  nodeEnter.on("click", (event, d) => {
    if (d.children) {
      d.children = null;
    } else {
      d.children = d.data.children;
    }
    update(treeData);
  });

  function update(source) {
    const node = source.descendants();
    const link = source.links();

    links.data(link)
      .attr("d", d3.linkVertical()
        .x(d => d.x)
        .y(d => d.y)
      );

    nodes.data(node, d => d.data.id)
      .attr("transform", d => `translate(${d.x},${d.y})`)

    nodes.exit()
      .remove();
  }
  }, [astData]);

  return (
    <div className="App">
      <div id="input-area">
       <button onClick={handleGenerateAST}>Run</button>
        <textarea
          value={code}
          onChange={handleCodeChange}
          placeholder="Enter Python code :)"
        />
      </div>
      <div id="tree-area">
      
      </div>
    </div>
  );
};

export default App;
