import React, { useEffect, useState } from 'react';
import axios from 'axios';

const App = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:5000/stockchallenge')
      .then(response => {
        console.log(response.data)
        setData(response.data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  if (!data) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>Stock News Challenge</h1>
      <p><strong>Yesterday's Close:</strong> {data.yesterdays_close}</p>
      <p><strong>Day Before Yesterday's Close:</strong> {data.day_before_yesterdays_close}</p>
      <p><strong>Positive Difference:</strong> {data.positive_difference}</p>
      <p><strong>Percentage Difference:</strong> {data.percentage_difference}%</p>
      {data.percentage_difference > 5 && <div>
        <h2>News:</h2>
        <ul>
          {data.news.map((article, index) => (
            <li key={index}>
              <h3>{article.title}</h3>
              <p>{article.description}</p>
            </li>
          ))}
        </ul>
      </div>}
    </div>
  );
};



export default App;
