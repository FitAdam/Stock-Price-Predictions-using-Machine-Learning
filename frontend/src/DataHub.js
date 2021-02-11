import React from 'react'
import {Card, CardDeck} from 'react-bootstrap';

class DataHub extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      articles: [],
      article: []
    }
    this.fetchArticles = this.fetchArticles.bind(this)
  }


  componentDidMount() {
    this.fetchArticles()
  }

  fetchArticles() {
    console.log('Fetching...')

    fetch('http://127.0.0.1:8000/api/post-list')
      .then(response => response.json())
      .then(data =>
        this.setState({
          articles: data
        })
      )
  }

  render() {
    return (
      <div id="list-wrapper">
        {this.state.articles.map(function (article, author) {
          return (
            <div key={author} className="task-wrapper flex-wrapper">
            <CardDeck>
              <Card style={{ width: '18rem' }}>
                <Card.Body>
                  <Card.Title>{article.title}</Card.Title>
                  <Card.Subtitle className="mb-2 text-muted">{article.updated}</Card.Subtitle>
                  <Card.Text>
                    {article.body}
                  </Card.Text>
                  <Card.Link href="#">Card Link</Card.Link>
                  <Card.Link href="#">Another Link</Card.Link>
                </Card.Body>
              </Card>
              </CardDeck>
            </div>

          )
        })}
      </div>



    );
  }
}



export default DataHub

///http://127.0.0.1:8000/api/post-list