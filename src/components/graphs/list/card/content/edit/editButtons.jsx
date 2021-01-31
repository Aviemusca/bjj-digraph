import React from "react";
import { Popup, Button } from "semantic-ui-react";
import { useToggle } from "../../../../../../hooks";
import { HeaderWrapper } from "../../styles";
import DeleteModal from "./delete";
import EditGraph from "./editGraph";

const EditButtons = ({ id, title }) => {
  const [deleteModal, toggleDeleteModal] = useToggle(false);
  const [editModal, toggleEditModal] = useToggle(false);
  React.useEffect(() => console.log(editModal), [editModal]);
  return (
    <React.Fragment>
      <HeaderWrapper>
        <Popup
          trigger={
            <Button
              icon="edit"
              size="tiny"
              compact
              circular
              onClick={toggleEditModal}
            />
          }
          content="Edit Map"
        />
        <Popup
          trigger={
            <Button
              icon="trash"
              size="tiny"
              compact
              circular
              negative
              onClick={toggleDeleteModal}
            />
          }
          content="Delete Map"
        />
      </HeaderWrapper>
      <DeleteModal
        title={title}
        id={id}
        open={deleteModal}
        handleClose={toggleDeleteModal}
      />
      <EditGraph id={id} open={editModal} handleClose={toggleEditModal} />
    </React.Fragment>
  );
};

export default EditButtons;
