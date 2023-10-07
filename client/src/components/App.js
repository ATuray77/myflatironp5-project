import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";

function App() {
  const [user, setUser] = useState(null);
  const [songs, setSongs] = useState([]);






  useEffect(() => {
    fetch("/cars")
      .then((r) => r.json())
      .then((cars) => console.log(cars));
  }, []);

  return <h1>Check the console for a list of cars!</h1>;
}


export default App;