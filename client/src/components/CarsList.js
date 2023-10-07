//import React from 'react'
import { Link } from 'react-router-dom'
//import "./App.css";
import React, { useState } from "react";
//import Home from './Home';


function CarsList({ cars, setCars }) {
  const [searchTerm, setSearchTerm] = useState("");

  const onFormSubmission = (e) => {
    e.preventDefault();

    setCars(cars.filter((car) => car.make_model.toLowerCase().includes(searchTerm)));
    // const filteredSongs = songs.filter(song =>
    //   song.Title.toLowerCase().includes(searchTerm))
  };

  const renderCars = Object.keys(cars).map((carID) => (
    <li key={carID}>
      <Link to={`/cars/${carID}`}>{cars[carID].make_model}</Link>
    </li>
  ));

 // const songPassToHome = songs.map((song) => <Home song={song} />);

  return (
    <div>
      <form onSubmit={onFormSubmission}>
        <label>
          🔎
          <input type="search" value={searchTerm} placeholder="search..." onChange={(e) => setSearchTerm(e.target.value.toLowerCase())} />
        </label>
      </form>
      <ol>{renderCars}</ol>
    </div>
  );
}

export default CarsList