import React from 'react'
import { useParams } from 'react-router-dom'

function CarShow({cars }) {
  // console.log(cars)

  const params = useParams(); //this function pulls out the id params
  console.log(params)
  //console.log(params)
  

  return (
    <div>
      <h3>make_model: {cars[params.carID].make_model}</h3>
      <h4>color: {cars[params.carID].color}</h4>
      <h5>licence_plate: {cars[params.carID].licence_plate}</h5>
      <p>{cars[params.carID].make_model}</p>
    </div>
  );
}

export default CarShow