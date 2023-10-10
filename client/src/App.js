import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [restaurants, setRestaurants] = useState([]);
  const [pizzas, setPizzas] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [searchedPizzas, setSearchedPizzas] = useState([]);

  useEffect(() => {
    // Fetch restaurants and pizzas when the component mounts
    axios.get('http://localhost:5555/restaurants')
      .then(response => {
        setRestaurants(response.data.restaurants);
      })
      .catch(error => {
        console.error('Error fetching restaurants', error);
      });

    axios.get('http://localhost:5555/pizzas')
      .then(response => {
        setPizzas(response.data.pizzas);
      })
      .catch(error => {
        console.error('Error fetching pizzas', error);
      });
  }, []);

  useEffect(() => {
    // Filter pizzas based on the search term
    const filteredPizzas = pizzas.filter(pizza =>
      pizza.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setSearchedPizzas(filteredPizzas);
  }, [searchTerm, pizzas]);

  return (
    <div className="Restaurants-Pizza">
      <h1>Restaurant Pizza</h1>

      <SearchPizzas onSearch={setSearchTerm} /> {/* Use the SearchPizzas component */}
      <Pizzas pizzas={searchedPizzas} /> {/* Use the Pizzas component */}
      
      <div>
        <h2>Restaurants</h2>
        {restaurants.map(restaurant => (
          <div key={restaurant.id}>
            <h3>{restaurant.name}</h3>
            <p>{restaurant.address}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
