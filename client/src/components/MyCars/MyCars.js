import {useParams } from "react-router-dom"
import React from "react"
//import "./MyCars.css"



function MyCars({ cars, user }) {
  console.log(user.cars)

  //const myparams = useParams();
  const renderUsersCars = cars.map((car) => (
    <li Car key={car.id}>
      
      <h3>{car.make_model}</h3>

      <strong>Color:</strong> {car.color} - 

      <strong>License PLate:</strong> {car.licence_plate}
      
      </li>
  ))
  
  
  return (
    <div>
      <h2>All my parked cars</h2>


      {renderUsersCars}


    </div>
  
  );
}





  // {user ? (
  //   <li className="production-card" id={id}>
  //     {/* <NavLink to={`/allmyCars/${user.id}`} >  */}
  //       <div>
  //         <h2>{make_model}</h2>
  //         <p>{color}</p>
  //         <p>{licence_plate}</p>
  //       </div>  
  //     {/* </NavLink> */}
  //     </li>
  //     ) : (
  //       <p>NOT AUTHORIZED</p>

  //     )}

export default MyCars
