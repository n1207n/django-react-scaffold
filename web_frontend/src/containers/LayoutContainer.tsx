import React, { ReactElement } from 'react';
import CssBaseline from '@material-ui/core/CssBaseline';
import Container from '@material-ui/core/Container';

interface LayoutContainerProps {
  children: ReactElement
}

export default function LayoutContainer(props: LayoutContainerProps) {
  return (
    <React.Fragment>
      <CssBaseline />
      <Container maxWidth="sm">
        {props.children}
      </Container>
    </React.Fragment>
  );
}