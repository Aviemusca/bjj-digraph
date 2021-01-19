import React from "react";
import PropTypes from "prop-types";
import { useLocation } from "react-router-dom";

export const GraphContext = React.createContext();

// Context provider for all the state quantities
// associated with the current graph the user is working on
export const GraphProvider = ({ children }) => {
  const location = useLocation();

  // The graph detail view currently open in the browser
  const [currentGraphId, setCurrentGraphId] = React.useState("");
  React.useEffect(() => {
    //setCurrentGraphId(location.state.graphId);
  }, []);

  // All the nodes and edges of the current graph
  const [nodes, setNodes] = React.useState([]);
  const [edges, setEdges] = React.useState([]);

  // Default react-digraph selected and copied node
  const [selected, setSelected] = React.useState({});
  const [copiedNode, setCopiedNode] = React.useState({});

  // Custom implemented array of selected nodes
  const [multiSelect, setMultiSelect] = React.useState([]);

  // An array of paths connecting 2 nodes
  const [paths, setPaths] = React.useState([]);

  // For disabling backend API calls. Used in the node editor,
  // where API call only occurs on submit
  const [disableAPI, setDisableAPI] = React.useState(false);

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
        disableAPI,
        setDisableAPI,
      }}
    >
      {children}
    </GraphContext.Provider>
  );
};

GraphProvider.propTypes = {
  children: PropTypes.node.isRequired,
};
