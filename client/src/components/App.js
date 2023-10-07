import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";

function App() {
  const [user, setUser] = useState(null);
  const [cars, setCars] = useState([]);


  useEffect(() => {
    // auto-login
    fetch("/check_session").then((r) => {
      if (r.ok) {
        r.json().then((user) => setUser(user));
      }
    });
  }, []);



  useEffect(() => {
    fetch("/cars")
      .then((r) => r.json())
      // .then((cars) => console.log(cars));
      .then((cars) => setCars(cars));
  }, []);

  if (!cars) return <h2>Loading...</h2>;

   <h1>Check the console for a list of cars!</h1>;

  return (
    <>
    </>

  )
}


export default App;