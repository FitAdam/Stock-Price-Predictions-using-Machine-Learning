import React from 'react'



class StockPred extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      firstTitle: '',
      secondTitle: '',
      thirdTitle: '',
    };

    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleInputChange(event) {
    const target = event.target;
    const value = target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }
  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.firstTitle + this.state.secondTitle + this.state.thirdTitle);
    event.preventDefault();
  }


  render() {
    return (
      <form onSubmit={this.handleSubmit}>

        <label>
          First Title:
          <input
            name="firstTitle"
            type="text"
            value={this.state.firstTitle}
            onChange={this.handleInputChange} />
        </label>
        <label>
          Second Title:
          <input
            name="secondTitle"
            type="text"
            value={this.state.secondTitle}
            onChange={this.handleInputChange} />
        </label>
        <label>
          Third Title:
          <input
            name="thirdTitle"
            type="text"
            value={this.state.thirdTitle}
            onChange={this.handleInputChange} />
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}

export default StockPred

///http://127.0.0.1:8000/api/post-list