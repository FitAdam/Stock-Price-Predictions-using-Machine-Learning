import React from 'react'


class Articles extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      articles: []
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
                  <h5>{article.title}</h5>
            </div>
          )
        })}
      </div>



    );
  }
}



export default Articles

///http://127.0.0.1:8000/api/post-list