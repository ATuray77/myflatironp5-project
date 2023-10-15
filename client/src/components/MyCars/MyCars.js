
import React from "react"
//import NavBar from "../NavBar"
//import "./MyCars.css"



function MyCars({ cars, user, setUser, handleDeleteCar }) {
  //console.log(user.cars)

  const [id] = cars
  //console.log(id)


  const handleDeleteClick = async () => {

    const response = await fetch(`/cars/${id}`, {
    method: "DELETE",
  });
    if (response.ok) {
      console.log(id)
      handleDeleteCar(id);
      
      alert("Deleted Successfully 🌼")
    }
}

  

 
  const renderUsersCars = cars.map((car) => (
    <li car key={car.id}>
      
      <h3 style={{color: 'blue'}}>{car.make_model}</h3>

      <b style={{color: 'brown'}}>Color: {car.color}</b> -   

      <b style={{color: 'green'}}>License PLate:</b> {car.licence_plate}

      <button onClick={handleDeleteClick}> Delete </button>
      
      </li>
  ))
  
  
  return (
    <>

      {user ? (
      <div>
        <h2>All my parked cars</h2>


        {renderUsersCars}
      
      </div>

        ) : (
       
      <div>
        <div>not logged in </div>
      </div>
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
