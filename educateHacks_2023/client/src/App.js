//import react stuff
import React, { useState, useEffect } from 'react';
import { BrowserRouter , Routes, Route } from 'react-router-dom';
import './App.css';
//import the pages
import { Home } from './pages/Home';
import { About } from './pages/About.js';
import { Flashcards } from './pages/Flashcards.js';
import { Worksheets } from './pages/Worksheets.js';

function App() {

  return (
    <>
      {/* Routing to different pages, specify page to render */}
      <BrowserRouter>
        <Routes>
          <Route index element={<Home />} />
          <Route path="home" element={<Home />} />
          <Route path="about" element={<About />} />
          <Route path="flashcards" element={<Flashcards />} />
          <Route path="worksheets" element={<Worksheets />} />

        </Routes>
      </BrowserRouter>
    </>
    );
}

export default App;
