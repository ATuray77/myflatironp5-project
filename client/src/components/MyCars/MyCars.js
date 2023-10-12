import {useParams } from "react-router-dom"
import React from "react"
//import "./MyCars.css"



function MyCars({ users }) {
  console.log(users)

  const myparams = useParams();
  
    
  return (
    <div>
      <h3>first_name: {users[myparams.userID].first_name}</h3>
      <h4>last_name: {users[myparams.userID].last_name}</h4>
      <h5>email: {users[myparams.carID].email}</h5>
      <h5>phone: {users[myparams.carID].phone}</h5>
      <p>{users[myparams.userID].username}</p>
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
