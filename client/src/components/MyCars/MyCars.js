import {useParams } from "react-router-dom"
import React from "react"
//import "./MyCars.css"



function MyCars({ user }) {
  console.log(user.cars)

  //const myparams = useParams();
  // const renderUsersCars = user.cars.map((car) => (
  //   <li Car key={car.id}>car={car}</li>
  // ))
  
  
  return (
    <div>
      <p>Make and Model: {user.cars.make_model}</p>
      <p>Color: {user.cars.colors}</p>
      <p>Licence plate: {user.cars.licence_plate}</p>
      
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
