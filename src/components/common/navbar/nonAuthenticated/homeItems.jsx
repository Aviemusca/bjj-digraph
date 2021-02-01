import React from "react";
import styled from "styled-components";
import { v4 as uuid } from "uuid";
import { useRefs } from "react-context-refs";
import AnchorLink from "react-anchor-link-smooth-scroll";

import { Menu } from "semantic-ui-react";

import { useActiveRef } from "../../../../hooks";

export const HomeItemsWrapper = styled.div`
  display: flex;
  flex-flow: row wrap;
  justify-content: space-around;
  align-items: center;
`;

const homeSections = ["home", "about", "try", "contact"];

// The home page menu, with smooth-scrolling between sections
const HomeItems = () => {
  // Get the section refs from context
  let sectionRefs = useRefs().filter((ref) => ref.type === "section");
  // Sort refs according to above sections
  sectionRefs = sectionRefs
    .slice()
    .sort(
      (a, b) =>
        homeSections.indexOf(a.meta.name) - homeSections.indexOf(b.meta.name)
    );
  const activeRef = useActiveRef(sectionRefs, { offset: 20 });
  return (
    <HomeItemsWrapper>
      {homeSections.map((section, idx) => (
        <AnchorLink href={`#${section}`} offset="-1" key={uuid()}>
          <Menu.Item as="" name={section} active={idx === activeRef} />
        </AnchorLink>
      ))}
    </HomeItemsWrapper>
  );
};

export default HomeItems;
