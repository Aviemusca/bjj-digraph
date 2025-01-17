import React from "react";
import PropTypes from "prop-types";
import { useLocation } from "react-router-dom";
import { routes } from "../../lib/config/routes/routes";

export const GraphContext = React.createContext();

// Context provider for all the state quantities
// associated with the current graph view of the viewport
export const GraphProvider = ({ children }) => {
  const location = useLocation();

  // The graph detail view currently open in the browser
  const [currentGraphId, setCurrentGraphId] = React.useState(null);
  React.useEffect(() => {
    if (
      location.pathname.startsWith(routes.pages.graphs.base) &&
      location.state
    )
      setCurrentGraphId(location.state.graphId);
    else setCurrentGraphId(null);
  }, [location, location.pathname]);

  // All the nodes and edges of the current graph
  const [nodes, setNodes] = React.useState([]);
  const [edges, setEdges] = React.useState([]);

  // Default react-digraph selected and copied node
  const [selected, setSelected] = React.useState({});
  const [copiedNode, setCopiedNode] = React.useState({});

  // Custom double-clicked node
  const [doubleClicked, setDoubleClicked] = React.useState({});

  // New default react-digraph multiselected
  const [selectedNodes, setSelectedNodes] = React.useState([]);
  const [selectedEdges, setSelectedEdges] = React.useState([]);
  const [copiedNodes, setCopiedNodes] = React.useState([]);
  const [copiedEdges, setCopiedEdges] = React.useState([]);

  // Custom implemented array of selected nodes
  const [multiSelect, setMultiSelect] = React.useState([]);

  // An array of paths connecting 2 nodes
  const [paths, setPaths] = React.useState([]);
  const [showPathIndex, setShowPathIndex] = React.useState(0);

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
        doubleClicked,
        setDoubleClicked,
        selectedNodes,
        setSelectedNodes,
        selectedEdges,
        setSelectedEdges,
        copiedNodes,
        setCopiedNodes,
        copiedEdges,
        setCopiedEdges,
        multiSelect,
        setMultiSelect,
        paths,
        setPaths,
        showPathIndex,
        setShowPathIndex,
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
