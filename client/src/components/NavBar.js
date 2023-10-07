import React from 'react'
import { NavLink } from 'react-router-dom'
//import "./App.css";


const linkStyles = {
  display: "inline-block",
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
        <NavLink to="/" exact style={linkStyles} activeStyle={{ background: "DarkOliveGreen" }}>
          User Home
        </NavLink>
      </div>

      <div>
        {user ? (
          <>
          <button onClick={handleLogoutClick}>Logout</button>
          <p>Welcome {user.first_name} {user.last_name}</p>
        <NavLink to="/songs" exact style={linkStyles} activeStyle={{ background: "DarkOliveGreen" }}>
          Songs
        </NavLink>

        <NavLink to="/form" exact style={linkStyles} activeStyle={{ background: "DarkOliveGreen" }}>
          Form
        </NavLink>

        {/* <NavLink to="/UserHome" exact style={linkStyles} activeStyle={{ background: "DarkOliveGreen" }}>
          User Home
        </NavLink> */}
        </>
        ) : (
        <>
        <NavLink to="/signUp" exact style={linkStyles} activeStyle={{ background: "DarkOliveGreen" }}>
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