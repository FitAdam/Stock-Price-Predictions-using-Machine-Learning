import React from 'react'
import './StockPred.css';

class StockPred extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      firstTitle: '',
      secondTitle: '',
      thirdTitle: '',
      prediction: 'Here you will see your prediction...',
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

    function getCookie(name){
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    const requestOptions = {
      method: 'POST',
      //mode: 'no-cors', // no-cors, *cors, same-origin
     // cache: 'default',
      headers: {'Content-Type': 'application/json' },
      body: JSON.stringify({ FIRST_TITLE: this.state.firstTitle, SECOND_TITLE: this.state.secondTitle, THIRD_TITLE: this.state.thirdTitle })
    };
    fetch('http://127.0.0.1:8000/api/news-titles', requestOptions)
      .then(async response => {
        const data = await response.json();

        // check for error response
        if (!response.ok) {
          // get error message from body or default to response status
          const error = (data && data.message) || response.status;
          return Promise.reject(error);
        }
        console.log('Went well');
        this.setState({ prediction: data })
      })
      .catch(error => {
        this.setState({ errorMessage: error.toString() });
        console.error('There was an error!', error);
      });
    event.preventDefault();
  }

  render() {
    return (
      <div className="display">
        <form className="item" onSubmit={this.handleSubmit}>

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
          <input className="button" type="submit" value="Submit" />
        </form>
        <div className="item">
        <h1 className="title">{this.state.prediction}</h1>

        </div>
        
      </div>


    );
  }
}

export default StockPred

