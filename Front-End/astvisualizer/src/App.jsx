import { useEffect } from "react";
import * as d3 from "d3";
import "./App.css";

function App() {
  const astData = {
    type: "Program",
    value: null,
    children: [
      {
        type: "Assignment",
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
      },
    ],
  };

  useEffect(() => {
    if (!astData) return;

    // Dimensions
    const width = 900;
    const height = 500;

    // Create the SVG canvas
    const svg = d3
      .select("#visualization")
      .append("svg")
      .attr("width", width)
      .attr("height", height);

    const g = svg
      .append("g")
      .attr("transform", `translate(${width / 2}, ${height / 2})`);

    // Basic tree layout
    const tree = d3.tree().size([300, 300]);

    // Convert AST to D3 hierarchy format
    const root = d3.hierarchy(astData);

    // Generate the links and nodes
    const link = g
      .selectAll(".link")
      .data(tree(root).links())
      .enter()
      .append("path")
      .attr("class", "link")
      .attr(
        "d",
        d3
          .linkHorizontal()
          .x((d) => d.y)
          .y((d) => d.x)
      );

    const node = g
      .selectAll(".node")
      .data(root.descendants())
      .enter()
      .append("g")
      .attr("class", function () {
        return "node";
      })
      .attr("transform", (d) => `translate(${d.y}, ${d.x})`);

    node.append("circle").attr("r", 8);

    node
      .append("text")
      .attr("dy", 5)
      .text((d) => d.data.type + (d.data.value ? ": " + d.data.value : ""));
  }, [astData]);

  return (
    <div className="App">
      <div id="visualization"></div>
    </div>
  );
}

export default App;
