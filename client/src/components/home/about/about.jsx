import React from "react";
import { useContextRef } from "react-context-refs";

import styled from "styled-components";
import { Segment } from "semantic-ui-react";

import { useWindowSize } from "../../../hooks";

const StyledSegment = styled(Segment)`
  min-height: ${({ height }) => height}px;
  position: relative;
  &.segment.vertical {
    background: pink;
  }
`;

const About = () => {
  const windowSize = useWindowSize();
  const ref = useContextRef("section", { name: "about" });
  return (
    <div ref={ref} id="about">
      <StyledSegment vertical height={windowSize.height + 60} />
    </div>
  );
};

export default About;