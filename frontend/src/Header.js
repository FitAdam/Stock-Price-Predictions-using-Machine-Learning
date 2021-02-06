
import React from 'react';
import { Navbar, Nav, Form, FormControl, Button } from 'react-bootstrap';

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
          <Nav.Link href="#home">Home</Nav.Link>
          <Nav.Link href="#features">About</Nav.Link>
          <Nav.Link href="#pricing">Pricing</Nav.Link>
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