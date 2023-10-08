import { Link } from "react-router-dom";
import React, { useState } from "react";
import "./styles.css"


function MyCars({ cars,  onDeleteCar}) {
  const [ id, make_model, color, licence_plate] = cars
    
  return (
    <li className="production-card" id={id}>
      <Link to={`/cars/${id}`} > 
        <div>
          {/* <h2>{make_model}</h2> */}
          <p>{color}</p>
          <p>{licence_plate}</p>
        </div>  
      </Link>
    </li>
  )
}

export default MyCars
