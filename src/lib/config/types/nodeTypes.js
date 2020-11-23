import * as shapes from "../shapes/shapes";
const commonProps = {
  effectiveness: 50,
  priority: 50,
  proficiency: 50,
  comment: "",
  description: "",
};
export const nodeTypes = {
  position: {
    name: "position",
    typeText: "My Position",
    shapeId: "#circle-dark",
    shape: shapes.CircleDark,
    ...commonProps,
  },
  conditional: {
    name: "conditional",
    typeText: "New Conditional",
    shapeId: "#lozenge",
    shape: shapes.Lozenge,
    ...commonProps,
  },
  submission: {
    name: "submission",
    typeText: "New Submission",
    shapeId: "#complexCircle",
    shape: shapes.ComplexCircleShape,
    ...commonProps,
  },
  transition: {
    name: "transition",
    typeText: "New Transition",
    shapeId: "#skinny",
    shape: shapes.SkinnyRectangle,
    ...commonProps,
  },
  sweep: {
    name: "sweep",
    typeText: "New Poly",
    shapeId: "#hexagon-flat",
    shape: shapes.HexagonFlat,
    ...commonProps,
  },
  entry: {
    name: "entry",
    typeText: "New Entry",
    shapeId: "#hexagon",
    shape: shapes.Hexagon,
    ...commonProps,
  },
  guardPull: {
    name: "guardPull",
    typeText: "New Guard-Pull",
    shapeId: "#poly-star",
    shape: shapes.PolyStar,
    ...commonProps,
  },

  takedown: {
    name: "takedown",
    typeText: "New Takedown",
    shapeId: "#trial",
    shape: shapes.trial,
    ...commonProps,
  },
  test: {
    name: "test",
    typeText: "New Takedown",
    shapeId: "#square",
    shape: shapes.Square,
    ...commonProps,
  },
  dummy: {
    name: "dummy",
    typeText: "New Takedown",
    shapeId: "#dummy",
    shape: shapes.Dummy,
    ...commonProps,
  },
};

const extras = {
  pass: {
    typeText: "New Poly",
    shapeId: "#pass",
    shape: shapes.PassShape,
  },

  choice: {
    typeText: "New Poly",
    shapeId: "#choice",
    shape: shapes.ChoiceShape,
  },

  task: {
    typeText: "New Poly",
    shapeId: "#task",
    shape: shapes.TaskShape,
  },

  wait: {
    typeText: "New Poly",
    shapeId: "#wait",
    shape: shapes.WaitShape,
  },

  terminator: {
    typeText: "New Poly",
    shapeId: "#terminator",
    shape: shapes.TerminatorShape,
  },
  ellipse: {
    typeText: "New Ellipse",
    shapeId: "#ellipse",
    shape: shapes.Ellipse,
  },
  triangle: {
    typeText: "New Hex",
    shapeId: "#triangle",
    shape: shapes.Triangle,
  },
};
