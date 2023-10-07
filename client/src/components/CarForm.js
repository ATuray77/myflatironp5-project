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
    <h3>Please fill in your car information</h3>
      <form onSubmit={onSubmit} className="form">
        <label>
          Makd and Model
          <input type="text" name="Make_model" />
        </label>
        <label>
          Color
          <input type="text" name="color" />
        </label>
        <label>
          License Plate
          <select name="licence_plate">
            <option>praise</option>
            <option>Worship</option>
          </select>
        </label>
        <label>
          Leave a comment
          <textarea name="Lyrics"></textarea>
        </label>
        <button type="submit">Add a song</button>
      </form>
    </>
  );
}

export default CarForm;
