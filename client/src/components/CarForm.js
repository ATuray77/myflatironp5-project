//import "./App.css";
import "./Form.css";
//import { useRef } from "react";


function CarForm({ onFormSubmitted }) {

  const onSubmit = (e) => {
    e.preventDefault();
    const formData = Object.fromEntries(new FormData(e.target));
    console.log(formData);

    fetch("/cars", {
      method: "POST",
      headers: {
        accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((r) => r.json())
      .then((addedSong) => onFormSubmitted(addedSong));
  };

  return (
    <>
    <h3>Please fill in this form to submit a song</h3>
      <form onSubmit={onSubmit} className="form">
        <label>
          Title
          <input type="text" name="Title" />
        </label>
        <label>
          Artist
          <input type="text" name="Artist" />
        </label>
        <label>
          Style
          <select name="Style">
            <option>praise</option>
            <option>Worship</option>
          </select>
        </label>
        <label>
          Lyrics
          <textarea name="Lyrics"></textarea>
        </label>
        <button type="submit">Add a song</button>
      </form>
    </>
  );
}

export default CarForm;
