/* eslint-disable react/jsx-key */
import * as d3 from "d3";
import "./App.css";
import { useRef, useEffect, useState } from "react";

const data = {
	name: "Program",
	children: [
		{
			name: "=",
			children: [
				{
					name: "a",
				},
				{
					name: "+",
					children: [
						{
							name: "10",
						},
						{
							name: "5",
						},
					],
				},
			],
		},
	],
};
const animalsHierarchy = () => d3.hierarchy(data).sum(() => 1);
const createTree = d3.tree().size([900, 300]);
const animalsTree = createTree(animalsHierarchy());

function App() {
	const svgRef = useRef(null);
	const [fileContent, setFileContent] = useState("");

	useEffect(() => {
		// Set svg size
		const svg = svgRef.current;
		if (svg) {
			const treeBBox = svg.getBBox();

			svg.setAttribute("width", treeBBox.width + treeBBox.x);
			svg.setAttribute("height", treeBBox.height + treeBBox.y);
		}

		// File upload handling
		const fileInput = document.getElementById("file-input");

		fileInput.addEventListener("change", (event) => {
			const file = event.target.files[0];

			const reader = new FileReader();
			reader.readAsText(file);

			reader.onload = () => {
				setFileContent(reader.result);
			};
		});
	}, []);

	return (
		<div id='appcontainer'>
			<div id='input-area'>
				<div id='buttons'>
					<div id='file-upload'>
						<input
							type='file'
							id='file-input'
							accept='.py'
							style={{ display: "none" }}
						/>
						<button
							onClick={() => document.getElementById("file-input").click()}
						>
							Upload Files
						</button>
					</div>

					<div id='run-btn'>
						<button>Run</button>
					</div>
				</div>
				<div id='file-content'>
					<textarea value={fileContent} readOnly></textarea>
				</div>
			</div>
			<div id='tree-area'>
				<svg ref={svgRef}>
					<g transform='translate(0, 20)' id='ast'>
						{animalsTree
							.links()
							.map(({ source: { x: x1, y: y1 }, target: { x: x2, y: y2 } }) => (
								<line x1={x1} y1={y1} x2={x2} y2={y2} stroke='black' />
							))}
						{animalsTree.descendants().map(({ x, y, data: { name } }) => (
							<g key={name}>
								<circle cx={x} cy={y} r={10} fill='white' stroke='black' />
								<text
									x={x}
									y={y}
									textAnchor='middle'
									dominantBaseline='central'
									fontSize='10px'
									fill='black'
								>
									{name}
								</text>
							</g>
						))}
					</g>
				</svg>
			</div>
		</div>
	);
}

export default App;
