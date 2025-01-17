import React from "react";
import { GraphUtils } from "react-digraph";
import { GraphContext } from "../../contexts/graph/graph";
import { NodeTypesContext } from "../../contexts/nodeTypes";

// A hook which returns a render node method for react digraphs.
// The svg properties of the node are embedded in the svg symbol
// returned by the render method
export const useRenderNode = () => {
  const { multiSelect, paths, showPathIndex } = React.useContext(GraphContext);
  const { nodeTypes } = React.useContext(NodeTypesContext);

  // Get the svg width, height and x, y position offset
  // of a nodeType
  const getNodeDimensions = (nodeType) => {
    const { width, height } = nodeType.shape.props;
    const x = -width / 2;
    const y = -height / 2;
    return { width, height, x, y };
  };

  // Returns the base (static) svg properties of a node of a given type
  const getBaseSvgProps = (nodeType) => {
    if (!nodeType) return;
    const svgProps = {
      ...nodeType.svgProps,
      ...getNodeDimensions(nodeType),
    };
    return svgProps;
  };

  // Returns the dynamic svg properties of a node due to user interaction
  const getDynamicSvgProps = (node) => {
    if (multiSelect.find((selectedNode) => selectedNode.id === node.id)) {
      return { filter: "url(#shadow)" };
    }
    if (paths.length) {
      if (paths[showPathIndex].find((pathNode) => pathNode.id === node.id)) {
        return { filter: "url(#shadow)" };
      }
    }
  };

  // Returns the complete svg properties of a node
  const getSVGProps = (node) => {
    const nodeType = nodeTypes[node.type] || nodeTypes["score-position-user"];
    const baseSvgProps = getBaseSvgProps(nodeType);
    const dynamicSvgProps = getDynamicSvgProps(node);
    const svgProps = { ...baseSvgProps, ...dynamicSvgProps };
    return svgProps;
  };

  // Render method providing suitable svg symbol for input node
  const renderNode = (ref, node, id, selected, hovered) => {
    console.log(nodeTypes);
    const nodeClassName = GraphUtils.classNames("node", { selected, hovered });
    const nodeType = nodeTypes[node.type] || nodeTypes["score-position-user"];
    console.log(node);
    const svgProps = getSVGProps(node);
    return (
      <g>
        <defs>
          <filter id="shadow">
            <feDropShadow
              dx="15"
              dy="15"
              floodColor="rgba(0, 0, 0, 0.6)"
              stdDeviation="4"
            />
          </filter>
        </defs>
        <use
          className={nodeClassName}
          href={nodeType.shapeId}
          xmlns="http://www.w3.org/2000/svg"
          {...svgProps}
        />
      </g>
    );
  };

  return renderNode;
};
