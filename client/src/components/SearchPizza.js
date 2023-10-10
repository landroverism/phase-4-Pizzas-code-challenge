import React, { useState } from 'react';
import './SearchPizza.css';

const SearchPizza = ({ onSearch }) => {
  const [searchTerm, setSearchTerm] = useState('');

  const handleSearch = () => {
    onSearch(searchTerm);
  };

  return (
    <div>
      <input
        type="text"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        placeholder="Search Pizzas"
      />
      <button onClick={handleSearch}>Search</button>
    </div>
  );
};

export default SearchPizza;
