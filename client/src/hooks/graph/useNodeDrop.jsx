import React from "react";
import { useDrop, useDragLayer } from "react-dnd";

import { useGraphOps } from "./useGraphOps";
import { dragTypes } from "../../lib/config/types/dragTypes";
import { SettingsContext } from "../../contexts/graph/settings";
import { usePositionConverter } from "./usePositionConverter";

// A hook to drop nodes from the palette to the canvas
export const useNodeDrop = (graphRef, wrapperRef) => {
  const { handleCreateNode } = useGraphOps();
  const { clientToGraph } = usePositionConverter(graphRef, wrapperRef);
  const { settings } = React.useContext(SettingsContext);

  // Creates a node of suitable type under the mouse cursor
  const handleDrop = () => {
    // Calculates the absolute position for dropping
    const dropPosition = clientToGraph([mousePosition.x, mousePosition.y]);
    if (dropPosition)
      handleCreateNode(dropPosition[0], dropPosition[1], itemType.subtype);
  };

  const handleCanDrop = () => {
    if (!settings.readOnly) return true;
    // todo: else trigger a msg to user to unlock graph
  };

  const [{ itemType }, dropRef] = useDrop({
    accept: dragTypes.NODE,
    canDrop: handleCanDrop,
    drop: handleDrop,
    collect: (monitor) => ({
      itemType: monitor.getItem(),
    }),
  });

  // Tracks the mouse position during drag
  const mousePosition = useDragLayer((monitor) => monitor.getClientOffset());

  return dropRef;
};
