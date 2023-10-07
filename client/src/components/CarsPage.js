import React from 'react'
import { Route, useRouteMatch } from 'react-router-dom'
import CarsList from './CarsList'
import CarShow from './CarShow'
//import "./App.css";
//import SongForm from './SongForm'


function CarsPage({ cars, setCars }) {
  const match = useRouteMatch();
  // console.log(match)



  return (
    <div>
       <h3>Choose a car from the list to see details</h3>
      <CarsList cars={cars} setCars={setCars}  />
      <Route exact path={match.url}>
       
      </Route>

      <Route path={`${match.url}/:carID`}>
        <CarShow cars={cars} />
      </Route>
    </div>
  );
}

export default CarsPage