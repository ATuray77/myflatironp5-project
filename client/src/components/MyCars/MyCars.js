
import React from "react"
//import NavBar from "../NavBar"
//import "./MyCars.css"



function MyCars({ cars, user, setUser }) {
  console.log(user.cars)

  if (!user.cars) {
    return  <div> Loading...</div>
  }

  

 
  const renderUsersCars = cars.map((car) => (
    <li Car key={car.id}>
      
      <h3 style={{color: 'blue'}}>{car.make_model}</h3>

      <b style={{color: 'brown'}}>Color: {car.color}</b> -   

      <b style={{color: 'green'}}>License PLate:</b> {car.licence_plate}

      <button > Delete </button>
      
      </li>
  ))
  
  
  return (
    <>

      {user ? (
      <switch>
        <h2>All my parked cars</h2>


        {renderUsersCars}
      
      </switch>

        ) : (
       
      <switch>
        <div>not logged in </div>
      </switch>
      )}

    </>
  
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
