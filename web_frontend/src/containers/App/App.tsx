import React from 'react';

import { createMuiTheme, ThemeProvider } from '@material-ui/core';
import { Switch, Router, Route } from 'react-router-dom';
import { createBrowserHistory } from 'history';
import LayoutContainer from '../LayoutContainer';

const useTheme = createMuiTheme({
  palette: {
    type: 'dark',
    background: {
      default: '#2196f3'
    }
  }
})

const history = createBrowserHistory();

export default function App() {
  return (
    <ThemeProvider theme={useTheme}>
      <div id="app-header">
      </div>
      <div id="app-container">
        <Router history={history}>
          <LayoutContainer>
            <Switch>
              <Route path="/">
                <div></div>
              </Route>
            </Switch>
          </LayoutContainer>
        </Router>
      </div>
    </ThemeProvider>
  );
};