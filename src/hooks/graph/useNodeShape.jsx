import React from "react";
import { Node } from "react-digraph";
import { GraphContext } from "../../contexts/graph";
import {
  nodeTypes,
  opponentShapeProps,
  userShapeProps,
} from "../../lib/config/types/nodeTypes";
import { getNodeSize } from "../../lib/utils/graph";

// A hook which returns a function giving the svg properties of a node

export const useNodeShape = () => {
  const { multiSelect } = React.useContext(GraphContext);

  // returns the svg width, height and x, y position offset
  // of the node
  const getNodeDimensions = (xlinkHref) => {
    const { width, height } = getNodeSize(xlinkHref);
    const x = -width / 2;
    const y = -height / 2;
    return { width, height, x, y };
  };
  // Returns the base svg properties of a node of a given type and subtype
  const getBaseSvgProps = (nodeType, xlinkHref) => {
    const subtype = nodeType.subtype;
    let svgProps = { fill: nodeType.fill, ...getNodeDimensions(xlinkHref) };
    switch (subtype) {
      case "user":
        svgProps = { ...svgProps, ...userShapeProps };
        break;
      case "opponent":
        svgProps = { ...svgProps, ...opponentShapeProps };
        break;
      default:
        throw new Error(`Node subtype ${subtype} not recognized.`);
    }
    return svgProps;
  };
  const getDynamicSvgProps = (node) => {
    if (multiSelect.find((selectedNode) => selectedNode.id === node.id)) {
      return { stroke: "blue" };
    }
  };

  const getNodeShape = (node) => {
    const nodeType = nodeTypes[node.type];
    const nodeTypeXlinkHref = Node.getNodeTypeXlinkHref(node, nodeTypes) || "";
    const baseSvgProps = getBaseSvgProps(nodeType, nodeTypeXlinkHref);
    const dynamicSvgProps = getDynamicSvgProps(node);
    const svgProps = { ...baseSvgProps, ...dynamicSvgProps };

    return {
      nodeTypeXlinkHref,
      svgProps,
    };
  };

  return getNodeShape;
};