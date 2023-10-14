import {useParams } from "react-router-dom"
import React from "react"
//import "./MyCars.css"



function MyCars({ user }) {
  console.log(user.cars)

  //const myparams = useParams();
  const renderUsersCars = user.cars.map((car) => (
    <div Car key={car.id}>car={car}</div>
  ))
  
  
  return (
    <div>
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
