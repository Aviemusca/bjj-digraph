import React from "react";
import { GraphView, Edge, Node, GraphUtils } from "react-digraph";
import styled from "styled-components";

import { graphConfig, NODE_KEY } from "../config/graphConfig";
import { useKeyPressed, useKeysPressed } from "../hooks/useKeyPressed";
import { GraphContext } from "../contexts/graphContext";
import { NodePanel, EdgePanel } from "./panels";
import { GraphOpsContext } from "../contexts/graphOpsContext";

const { nodeTypes, nodeSubtypes, edgeTypes } = graphConfig;

const GraphWrapper = styled.div`
  width: 100%;
  height: 1000px;
`;
const NodeContentWrapper = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  font-size: 1.25em;
`;

export const Graph = () => {
  const { nodes, edges, selected } = React.useContext(GraphContext);
  const {
    handleSelectNode,
    handleSelectEdge,
    handleCreateNode,
    handleDeleteNode,
    handleCreateEdge,
    handleSwapEdge,
    handleDeleteEdge,
    handleCopySelected,
    handlePasteSelected,
  } = React.useContext(GraphOpsContext);
  const graphRef = React.useRef();

  const renderNodeText = (data) => {
    return (
      <foreignObject x="-77" y="-77" width="154" height="154">
        <NodeContentWrapper>
          <span>{data.title} </span>
        </NodeContentWrapper>
      </foreignObject>
    );
  };
  const renderNode = (ref, data, id, selected, hovered) => {
    console.log(ref, data, id, selected, hovered);
    const nodeShapeContainerClassName = GraphUtils.classNames("shape");
    const nodeClassName = GraphUtils.classNames("node", { selected, hovered });
    const nodeSubtypeClassName = GraphUtils.classNames("subtype-shape", {
      selected,
    });
    const nodeSubtypeXlinkHref = Node.getNodeSubtypeXlinkHref(
      data,
      nodeSubtypes
    );
    const nodeTypeXlinkHref = Node.getNodeTypeXlinkHref(data, nodeTypes) || "";

    // get width and height defined on def element
    const defSvgNodeElement = nodeTypeXlinkHref
      ? document.querySelector(`defs>${nodeTypeXlinkHref}`)
      : null;
    const nodeWidthAttr = defSvgNodeElement
      ? defSvgNodeElement.getAttribute("width")
      : 0;
    const nodeHeightAttr = defSvgNodeElement
      ? defSvgNodeElement.getAttribute("height")
      : 0;
    const width = parseInt(nodeWidthAttr, 10);
    const height = parseInt(nodeHeightAttr, 10);
    console.log(
      nodeShapeContainerClassName,
      nodeClassName,
      nodeTypeXlinkHref,
      width,
      height
    );
    return (
      <g className={nodeShapeContainerClassName}>
        {!!data.subtype && (
          <use
            className={nodeSubtypeClassName}
            x={-width / 2}
            y={-height / 2}
            width={width}
            height={height}
            xlinkHref={nodeSubtypeXlinkHref}
          />
        )}
        <use
          className={nodeClassName}
          height={height}
          width={width}
          x={-width / 2}
          y={-height / 2}
          xlinkHref={nodeTypeXlinkHref}
        />
      </g>
    );
  };
  const renderNode2 = () => {
    return (
      <svg viewBox="0 0 20 20">
        <foreignObject x="-12" y="0" width="20" height="20">
          <div
            style={{
              width: "100%",
              height: "100%",
              background: "yellow",
            }}
          />
        </foreignObject>
      </svg>
    );
  };
  return (
    <GraphWrapper>
      <GraphView
        ref={graphRef}
        nodeKey={NODE_KEY}
        nodes={nodes}
        edges={edges}
        selected={selected}
        nodeTypes={nodeTypes}
        nodeSubtypes={nodeSubtypes}
        edgeTypes={edgeTypes}
        onSelectNode={handleSelectNode}
        onCreateNode={handleCreateNode}
        onDeleteNode={handleDeleteNode}
        onSelectEdge={handleSelectEdge}
        onCreateEdge={handleCreateEdge}
        onSwapEdge={handleSwapEdge}
        onDeleteEdge={handleDeleteEdge}
        onCopySelected={handleCopySelected}
        onPasteSelected={handlePasteSelected}
        renderNode={renderNode}
        renderNodeText={renderNodeText}
      />
      {selected && !selected.source && <NodePanel node={selected} />}
      {selected && selected.source && <EdgePanel edge={selected} />}
    </GraphWrapper>
  );
};
