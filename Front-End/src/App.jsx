import * as d3 from "d3";
import { useRef, useEffect, useState } from "react";
import "./App.css";

function App() {
	const svgRef = useRef(null);
	const [fileContent, setFileContent] = useState("");
	const [astJson, setAstJson] = useState(null);
	const [treeData, setTreeData] = useState(null);

	useEffect(() => {
		const svg = svgRef.current;
		if (svg) {
			const treeBBox = svg.getBBox();
			svg.setAttribute("width", treeBBox.width + treeBBox.x);
			svg.setAttribute("height", treeBBox.height + treeBBox.y);
		}

		const fileInput = document.getElementById("file-input");
		fileInput.addEventListener("change", (event) => {
			const file = event.target.files[0];
			const reader = new FileReader();
			reader.readAsText(file);
			reader.onload = () => {
				setFileContent(reader.result);
			};
		});

		const fetchAstJson = async () => {
			try {
				const response = await fetch("http://localhost:5000/astjson");
				if (!response.ok) {
					throw new Error("Failed to fetch AST JSON data");
				}
				const data = await response.json();
				setAstJson(data);
				console.log(data);
			} catch (error) {
				console.error("Error fetching AST JSON data:", error);
			}
		};

		fetchAstJson();
	}, []);

	useEffect(() => {
		if (astJson) {
			const astHierarchy = () => d3.hierarchy(astJson).sum(() => 1);
			const createAST = d3.tree().size([900, 600]);
			const AbstractSyntaxTree = createAST(astHierarchy());
			setTreeData(AbstractSyntaxTree);
		}
	}, [astJson]);

	const runCode = async () => {
		try {
			const encodedFileContent = btoa(fileContent);
			const response = await fetch("http://localhost:5000/frontend", {
				method: "POST",
				headers: { "Content-Type": "text/plain" },
				body: encodedFileContent,
			});

			if (!response.ok) {
				throw new Error(`Server error: ${response.status}`);
			}
		} catch (error) {
			console.error("Error fetching or processing AST:", error);
		}
	};

	return (
		<div id='appcontainer'>
			<div id='heading'>
				<p>AST Visualizer</p>
			</div>
			<div id='maincontent'>
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
							<button onClick={runCode}>Run</button>
						</div>
					</div>
					<div id='file-content'>
						<textarea value={fileContent} readOnly></textarea>
					</div>
				</div>
				<div id='tree-area'>
					<svg ref={svgRef}>
						<g transform='translate(0, 20)' id='ast'>
							{treeData ? (
								<>
									{treeData
										.links()
										.map(
											(
												{ source: { x: x1, y: y1 }, target: { x: x2, y: y2 } },
												index
											) => (
												<line
													key={`line-${index}`}
													x1={x1}
													y1={y1}
													x2={x2}
													y2={y2}
													stroke='white'
												/>
											)
										)}
									{treeData
										.descendants()
										.map(({ x, y, data: { name } }, index) => (
											<g key={`node-${index}`}>
												<circle
													cx={x}
													cy={y}
													r={20}
													fill='none'
													stroke='white'
												/>
												<text
													x={x}
													y={y}
													textAnchor='middle'
													dominantBaseline='central'
													fontSize='10px'
													fill='white'
												>
													{name}
												</text>
											</g>
										))}
								</>
							) : (
								<text
									x='450'
									y='150'
									textAnchor='middle'
									fontSize='20px'
									fill='white'
								>
									No input data
								</text>
							)}
						</g>
					</svg>
				</div>
			</div>
		</div>
	);
}

export default App;
