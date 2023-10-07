import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
//import "./App.css"
import NavBar from './NavBar';
import Home from "./Home";
import Login from "./Login";
import SignUp from "./Signup";
import CarForm from './CarForm';
import MyCars from './MyCars';


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


  function handleOnFormSubmitted(addedSong) {
    const updatedSongs = [...songs, addedSong];
    setSongs(updatedSongs);
  }


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
    <NavBar user={user} setUser={setUser}/> 
    
    {/* <div className={"App " + (isDarkMode ? "dark" : "light")}>
    <header>
      <h2> My Song Library</h2>
      <button onClick={handleDarkMode}>
        {isDarkMode ? "Dark" : "LIght"} Mode
      </button>
    </header> */}
      {user ? (
      <Switch>
        <Route path="/cars">
          {/* <UserHome user={user}/> */}
          <CarsPage songs={songs} setSongs={setSongs} />
        </Route>
        <Route path="/form">
          <CarForm onFormSubmitted={handleOnFormSubmitted} />
        </Route>
        <Route exact path="/">
          <UserHome songs={songs} setSongs={setSongs} id={songs.id} onDeleteSong={handleDeleteSong} />
        </Route>
      </Switch>
      ) : (
      <Switch>
        <Route path="/signup">
          <SignUp setUser={setUser} />
        </Route>

        <Route path="/login">
          <Login setUser={setUser}/>
        </Route>

        <Route exact path="/">
          <Home />
        </Route>
      </Switch>
      )}
    </>
  );
}


export default App;