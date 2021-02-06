import React from 'react';
import Header from './Header.js'
import Footer from './Footer.js'
import JoinButton from './JoinButton.js';

class App extends React.Component {
  constructor() {
    super()
    this.state = {
    }
  }
  render() {
    return (
      <body>
        <Header />
        <div class="content">
        <JoinButton />
        </div>
        <Footer />
      </body>
    );
  }
}

export default App