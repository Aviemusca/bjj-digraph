import React from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { Menu, Button, Message, Icon } from "semantic-ui-react";

import { StyledMenu, StyledMessage } from "./styles";
import withPortalHOC from "../../hocs/withPortal";
import withModalHOC from "../../hocs/withModal";

import GraphForm from "../graphForm";
import { GraphsContext } from "../../contexts/graphs";

const LoadingMessage = () => (
  <StyledMessage
    header="Just one second..."
    icon={<Icon name="circle notched" loading />}
  />
);

const ErrorMessage = ({ errorMsg }) => (
  <StyledMessage
    header={`Oops... ${errorMsg}`}
    content="Please try again."
    error
  />
);

const LoadingPortal = withPortalHOC(LoadingMessage);
const ErrorPortal = withPortalHOC(ErrorMessage);
const GraphFormModal = withModalHOC(GraphForm);

const Navbar = () => {
  const {
    isLoading,
    error,
    isAuthenticated,
    logout,
    loginWithPopup,
  } = useAuth0();

  const [newGraph, setNewGraph] = React.useState(false);
  const [showGraphs, setShowGraphs] = React.useState(false);
  const { graphs } = React.useContext(GraphsContext);
  return (
    <React.Fragment>
      <StyledMenu fixed inverted pointing secondary size="large">
        <LoadingPortal open={isLoading} />
        <ErrorPortal open={error} errorMsg={error} />
        <GraphFormModal
          open={newGraph}
          handleClose={() => setNewGraph(false)}
        />
        <Menu.Item>
          {!isAuthenticated && (
            <Button as="a" inverted onClick={loginWithPopup}>
              Log In
            </Button>
          )}

          {isAuthenticated && (
            <Button
              as="a"
              inverted
              onClick={() => logout({ returnTo: window.location.origin })}
            >
              Log Out
            </Button>
          )}
        </Menu.Item>
        <Menu.Item>
          {isAuthenticated && (
            <Button as="a" inverted onClick={() => setNewGraph(true)}>
              New Graph
            </Button>
          )}
        </Menu.Item>
        <Menu.Item>
          {isAuthenticated && (
            <Button as="a" inverted onClick={() => setShowGraphs(true)}>
              My Graphs
            </Button>
          )}
        </Menu.Item>
      </StyledMenu>
      {showGraphs && (
        <div>
          {graphs.map((graph) => (
            <div key={graph.id}>
              <h2>{graph.title}</h2>
              <h2>{graph.id}</h2>
            </div>
          ))}
        </div>
      )}
    </React.Fragment>
  );
};

export default Navbar;
