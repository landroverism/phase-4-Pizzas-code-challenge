import React, { useState } from 'react';
import './Form.css';

const Form = ({ onSubmit }) => {
  const [price, setPrice] = useState('');
  const [pizzaId, setPizzaId] = useState('');
  const [restaurantId, setRestaurantId] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ price, pizzaId, restaurantId });
    setPrice('');
    setPizzaId('');
    setRestaurantId('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Price:
        <input type="number" value={price} onChange={(e) => setPrice(e.target.value)} />
      </label>
      <label>
        Pizza ID:
        <input type="number" value={pizzaId} onChange={(e) => setPizzaId(e.target.value)} />
      </label>
      <label>
        Restaurant ID:
        <input type="number" value={restaurantId} onChange={(e) => setRestaurantId(e.target.value)} />
      </label>
      <button type="submit">Create Restaurant-Pizza Entry</button>
    </form>
  );
};

export default Form;
