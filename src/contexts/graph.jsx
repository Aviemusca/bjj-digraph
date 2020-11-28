import React from "react";
import PropTypes from "prop-types";

export const GraphContext = React.createContext();

// Context provider for all the state quantities
// associated with the current graph the user is working on

export const GraphProvider = ({ children }) => {
  const [currentGraphId, setCurrentGraphId] = React.useState("");
  const [nodes, setNodes] = React.useState([]);
  const [edges, setEdges] = React.useState([]);
  const [selected, setSelected] = React.useState({});
  // An array of selected nodes
  const [multiSelect, setMultiSelect] = React.useState([]);
  // An array of paths connecting 2 nodes
  const [paths, setPaths] = React.useState([]);
  const [copiedNode, setCopiedNode] = React.useState({});

  return (
    <GraphContext.Provider
      value={{
        currentGraphId,
        setCurrentGraphId,
        nodes,
        setNodes,
        edges,
        setEdges,
        selected,
        setSelected,
        multiSelect,
        setMultiSelect,
        paths,
        setPaths,
        copiedNode,
        setCopiedNode,
      }}
    >
      {children}
    </GraphContext.Provider>
  );
};

GraphProvider.propTypes = {
  children: PropTypes.node.isRequired,
};
