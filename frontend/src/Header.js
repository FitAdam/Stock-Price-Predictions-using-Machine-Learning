
import React from 'react';
import { Navbar, Nav, Form, FormControl, Button } from 'react-bootstrap';
import { NavLink, Switch, Route } from 'react-router-dom';

function Header() {
  
  return (

    <header className="header">
      <Navbar bg="dark" variant="dark" sticky="top">
        <Navbar.Brand href="#home">
          <img
            alt=""
            src="/logo.svg"
            width="30"
            height="30"
            className="d-inline-block align-top"
          />{' '}
              SpecBot 2021
            </Navbar.Brand>
        <Nav className="mr-auto">
          <Nav.Link ><NavLink exact activeClassName="current" to='/Home'>Home</NavLink></Nav.Link>
          <Nav.Link ><NavLink exact activeClassName="current" to='/Articles'>Articles</NavLink></Nav.Link>
          <Nav.Link ><NavLink exact activeClassName="current" to='/DataHub'>Stock Predictions</NavLink></Nav.Link>
        </Nav>
        <Form inline>
          <FormControl type="text" placeholder="Search" className="mr-sm-2" />
          <Button variant="primary">Search</Button>
        </Form>
      </Navbar>

    </header>

  )

}


export default Header;