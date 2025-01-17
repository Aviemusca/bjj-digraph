import React from "react";
import { usePrevious } from "../utils/usePrevious";

// A hook which returns the element of a dependency array
// triggering a useEffect call

export const useDependencyTrigger = (dependencies) => {
  const previousDeps = usePrevious(dependencies, []);

  const changedDeps = dependencies.reduce((accum, dependency, index) => {
    if (JSON.stringify(dependency) !== JSON.stringify(previousDeps[index])) {
      return {
        ...accum,
        index,
      };
    }
    return accum;
  }, {});
  if (Object.keys(changedDeps).length) return changedDeps;
};
