import { Link } from "react-router-dom";
import React from "react";
import "./styles.css"


function MyCars({ cars, id,  onDeleteCar}) {
    
  return (
    <li className="production-card" id={id}>
      <Link to={`/cars/${id}`} >   
      
      </Link>

   
    </li>
  )
}

export default MyCars
