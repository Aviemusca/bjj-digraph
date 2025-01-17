import React from "react";
import { useAuth } from "../../../hooks";

import NonAuthNavbar from "./nonAuthenticated";
import AuthNavbar from "./authenticated";

// The navbar for the app portion of the site
const AppNavbar = () => {
  const { isAuthenticated } = useAuth();
  return isAuthenticated ? (
    <AuthNavbar fixed={false} />
  ) : (
    <NonAuthNavbar fixed={false} />
  );
};

export default AppNavbar;
