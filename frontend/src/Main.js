import React from 'react';
import { Switch, Route } from 'react-router-dom';
import Home from './Home';
import Articles from './Articles'
import DataHub from './DataHub'
import About from './About.js'


const Main = () => {
  return (
    <Switch> {/* The Switch decides which component to show based on the current URL.*/}
      <Route exact path='/Home' component={Home}></Route>
      <Route exact path='/Articles' component={Articles}></Route>
      <Route exact path='/DataHub' component={DataHub}></Route>
      <Route exact path='/about' component={About}></Route>
      <Route exact path='/about' component={About}></Route>
    </Switch>
  );
}

export default Main;