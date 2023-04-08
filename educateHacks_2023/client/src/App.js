//import react stuff
import React, { useState, useEffect } from 'react';
import { BrowserRouter , Routes, Route } from 'react-router-dom';
import './App.css';
//import the pages
import { Home } from './pages/Home';
import { About } from './pages/About.js';
import { Flashcards } from './pages/Flashcards.js';

function App() {

  //                    v initial state v
  const [data, setData] = useState([{}]);
  // data variable is used to middleman data between front and backend
  //set data is a function, puts JSON into data variable

  useEffect(() => {
    //gets response from flask members function
    fetch("http://127.0.0.1:5000/members").then(
      //take API response and turn it into JSON
      res => res.json()
    ).then(
          //shove JSON data into data
          data => {
            setData(data)
            console.log(data)
          }
        )
      }, [])

  return (
    <>
      {/* Routing to different pages, specify page to render */}
      <BrowserRouter>
        <Routes>
          <Route index element={<Home />} />
          <Route path="home" element={<Home />} />
          <Route path="about" element={<About />} />
          <Route path="flashcards" element={<Flashcards />} />

        </Routes>
      </BrowserRouter>
      
      {/* Display data from backend, the data var */}
      <div>
        {(typeof data.members === 'undefined') ? (
          <p>loading...</p>
        ) : (
          data.members.map((member, i) => (
            <p key={i}>{member}</p>
          ))
        )}
      </div>
    </>
    );
}

export default App;
