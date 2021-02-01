import styled, { css } from "styled-components";
import { Menu } from "semantic-ui-react";

const Color = css`
  background-color: #2f303a;
`;
export const NavbarMenu = styled(Menu)`
  &.ui.secondary.inverted.menu {
    ${Color}
    margin: 0;
    border-style: none;
    padding: 0.5em 0;
  }
  &.ui.menu {
    ${Color}
    padding: 0.5em 0;
  }
`;

export const SidebarMenu = styled(Menu)`
  &.ui.menu {
    ${Color}
  }
`;
