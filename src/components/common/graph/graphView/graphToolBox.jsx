import React from "react";
import styled from "styled-components";
import { Button, Popup, Icon } from "semantic-ui-react";

import { SettingsContext } from "../../../../contexts/settings";
import { GraphContext } from "../../../../contexts/graph";
import { getConnectingPaths } from "../../../../lib/graph/algorithms/getConnectingPaths";
const Wrapper = styled.div`
  position: absolute;
  left: 0;
  top: 0;
  height: 3em;
  width: 20em;
  z-index: 1000;
`;

const Image = styled.img`
  width: 20px;
`;

const ToolBoxContainer = () => {
  const { readOnly, toggleReadOnly } = React.useContext(SettingsContext);
  const { nodes, edges, multiSelect, setPaths } = React.useContext(
    GraphContext
  );

  const handleConnectedPaths = () => {
    const paths = getConnectingPaths(
      nodes,
      edges,
      multiSelect[0].id,
      multiSelect[1].id
    );
    setPaths(paths);
    console.log(paths);
  };
  const canGetConnectingPaths = () => multiSelect.length === 2;
  return (
    <Wrapper>
      <Button.Group>
        <Button icon compact>
          <Image src="../media/icons/grid.svg" alt="Grid" />
        </Button>
        <Popup
          trigger={
            <Button icon compact onClick={toggleReadOnly}>
              <Icon name={readOnly ? "lock" : "unlock"} />
            </Button>
          }
          content={readOnly ? "Unlock" : "Lock"}
        />
        <Popup
          trigger={
            <Button
              icon
              compact
              onClick={handleConnectedPaths}
              disabled={!canGetConnectingPaths()}
            >
              <Icon name="code branch" />
            </Button>
          }
          content="See all connecting paths"
        />
      </Button.Group>
    </Wrapper>
  );
};

export default ToolBoxContainer;
