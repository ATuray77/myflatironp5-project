import { NavLink } from "react-router-dom";
import React from "react";
import "./styles.css"


function MyCars({user, cars,  onDeleteCar}) {
  const [ id, make_model, color, licence_plate] = cars;
  console.log(make_model)
    
  return (
    <div>
      {user ? (
    <li className="production-card" id={id}>
      <NavLink to={`/cars/${id}`} > 
        <div>
          <h2>{make_model}</h2>
          <p>{color}</p>
          <p>{licence_plate}</p>
        </div>  
      </NavLink>
      </li>
      ) : (
        <p>NOT AUTHORIZED</p>

      )}
    
    </div>
  )}


export default MyCars
