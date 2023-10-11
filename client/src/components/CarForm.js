//import "./App.css";
import "./Form.css";
//import { useRef } from "react";


function CarForm({ onFormSubmitted }) {

  const onSubmit = (e) => {
    e.preventDefault();
    const formData = Object.fromEntries(new FormData(e.target));
    //console.log(formData);

    fetch("/cars", {
      method: "POST",
      headers: {
        accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((r) => r.json())
      .then((addedCar) => onFormSubmitted(addedCar));
  };

  return (
    <>
    <h3>Please fill in your car information</h3>
      <form onSubmit={onSubmit} className="form">
        <label>
          Make and Model
          <input type="text" name="make_model" />
        </label>
        <label>
          Color
          <input type="text" name="color" />
        </label>
        <label>
          License Plate
          <input type="text" name="licence_plate" />
        </label>
        {/* <label>
          Leave a comment
          <textarea name="Lyrics"></textarea>
        </label> */}
        <button type="submit">Add a car</button>
      </form>
    </>
  );
}

export default CarForm;
