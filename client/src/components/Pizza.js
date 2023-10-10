import React from 'react';
import './Pizza.css';

const Pizza = ({ name, ingredients }) => {
  return (
    <div className="pizza">
      <h3>{name}</h3>
      <p>{ingredients}</p>
    </div>
  );
};

export default Pizza;
