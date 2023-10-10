import React from 'react'
import { NavLink } from 'react-router-dom'
//import "./App.css";


const linkStyles = {
  display: "in-line block",
  width: "50px",
  padding: "12px",
  margin: "0px 6px 6px",
  background: "green",
  textDecoration: "none",
  color: "white",
};

function NavBar({ user, setUser }) {

  function handleLogoutClick() {
    fetch("/logout", { method: "DELETE" }).then((r) => {
      if (r.ok) {
        setUser(null);
      }
    });
  }

  return (
    <>
      <div>
        <h1>
          WELCOME TO METRO PARKING GARAGE
        </h1>
      </div>

      <div>
        {user ? (
          <>
          {/* <button onClick={handleLogoutClick} style={linkStyles} activeStyle={{ background: "DarkOliveGreen" }}>Logout</button> */}
          <p>Welcome {user.first_name} {user.last_name}
          <button onClick={handleLogoutClick} >Logout</button>
          </p>
        <NavLink to="/cars" exact style={linkStyles} activeStyle={{ background: "DarkOliveGreen" }}>
          CARS
        </NavLink>

        <NavLink to="/carForm" exact style={linkStyles} activeStyle={{ background: "DarkOliveGreen" }}>
          NEW CAR FORM
        </NavLink>

        <NavLink to="/mycars" exact style={linkStyles} activeStyle={{ background: "DarkOliveGreen" }}>
          MyCars
        </NavLink>

        {/* <NavLink to="/UserHome" exact style={linkStyles} activeStyle={{ background: "DarkOliveGreen" }}>
          User Home
        </NavLink> */}
        </>
        ) : (
        <>

        <NavLink to="/signup" exact style={linkStyles} activeStyle={{ background: "DarkOliveGreen" }}>
          SignUp
        </NavLink>

        <NavLink to="/login" exact style={linkStyles} activeStyle={{ background: "DarkOliveGreen" }}>
          Login
        </NavLink>

        </>
       )}
        
      </div>
    </>
  );
}


export default NavBar