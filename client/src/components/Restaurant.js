import React from 'react';
import './Restaurant.css'

const Restaurant = ({ name, address, prices }) => {
  return (
    <div className="restaurant">
      <h2>{name}</h2>
      <p>{address}</p>
      <h4>Prices:</h4>
      <ul>
        {prices.map((price, index) => (
          <li key={index}>${price}</li>
        ))}
      </ul>
    </div>
  );
};

export default Restaurant;
