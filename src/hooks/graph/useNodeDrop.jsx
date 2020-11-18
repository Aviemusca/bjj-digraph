import React from "react";
import { useDrop, useDragLayer } from "react-dnd";

import { useGraphOps } from "./useGraphOps";
import PositionConverter from "../../lib/graph/positionConverter";
import { dragTypes } from "../../lib/config/types/dragTypes";

// A hook to drop nodes from the palette to the canvas
export const useNodeDrop = (graphRef, wrapperRef) => {
  const { handleCreateNode } = useGraphOps();

  // Creates a node of suitable type under the mouse cursor
  const handleDrop = () => {
    // Calculates the absolute position for dropping
    const positionConverter = new PositionConverter(
      [mousePosition.x, mousePosition.y],
      graphRef,
      wrapperRef
    );
    const dropPosition = positionConverter.getOutputPosition();
    if (dropPosition)
      handleCreateNode(dropPosition[0], dropPosition[1], itemType.subtype);
  };

  const [{ itemType }, dropRef] = useDrop({
    accept: dragTypes.NODE,
    drop: handleDrop,
    collect: (monitor) => ({
      itemType: monitor.getItem(),
    }),
  });

  // Tracks the mouse position during drag
  const mousePosition = useDragLayer((monitor) => monitor.getClientOffset());

  return dropRef;
};
