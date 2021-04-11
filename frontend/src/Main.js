import React from 'react';
import { Switch, Route } from 'react-router-dom';
import Articles from './Articles'
import StockPred from './StockPred'
import About from './About.js'
import Home from './components/pages/HomePage/Home';


const Main = () => {
  return (
    <Switch> {/* The Switch decides which component to show based on the current URL.*/}
      <Route exact path='/' component={Home}></Route>
      <Route exact path='/Articles' component={Articles}></Route>
      <Route exact path='/StockPred' component={StockPred}></Route>
      <Route exact path='/about' component={About}></Route>
    </Switch>
  );
}

export default Main;