import Header from '../components/Header.js'
import PostForm from '../components/postform.js'
import React, { useState, useEffect, useRef } from 'react'
import Flashcard from '../components/Flashcard.js'
import axios from 'axios'
import '../Style_Cards.css'


export function Flashcards() {
  let SAMPLE_FLASHCARDS = []
  const OLD_SAMPLE_FLASHCARDS = [
    {
      id: 1,
      question: 'What is 2 + 2?',
      answer: '4',
      options: [
        '2',
        '3',
        '4',
        '5'
      ]
    },
    {
      id: 2,
      question: 'Question 2',
      answer: 'Answer 2',
      options: [
        'Answer 1',
        'Answer 2',
        'Answer 3',
        'Answer 4'
      ]
    },
    {
      id: 3,
      question: 'What is 2 + 2?',
      answer: '4',
      options: [
        '2',
        '3',
        '4',
        '5'
      ]
    },
  ]
  //flask api stuff
  //                    v initial state v
  const [data, setData] = useState([{}]);
  // data variable is used to middleman data between front and backend
  //set data is a function, puts JSON into data variable

  useEffect(() => {
    //gets response from flask members function
    fetch("http://localhost:5000/flashcards").then(
      //take API response and turn it into JSON
      res => res.json()
    ).then(
          //shove JSON data into data
          data => {
            setData(data)
            SAMPLE_FLASHCARDS = data
            console.log(SAMPLE_FLASHCARDS)
            console.log(OLD_SAMPLE_FLASHCARDS)
          }
        )
      }, [])

  //flashcard stuff
  let index = 0


  //send sample flashcards to flashcardlist
  const [flashcards, setFlashcards] = useState(SAMPLE_FLASHCARDS)
  const amountEl = useRef()

  function handleSubmit(e) {
    e.preventDefault()
    return {
      id: SAMPLE_FLASHCARDS[index].id ,
      question: SAMPLE_FLASHCARDS[index].question,
      answer: SAMPLE_FLASHCARDS[index].answer,
      options: SAMPLE_FLASHCARDS[index].options
    }
}
  
    
    
  return (
    <>
    <Header />
      <PostForm />
      <div className="container">
        <div className="card-grid">
        {data.flashcards.map(flashcard => {
          return <Flashcard flashcard={flashcard} key={flashcard.id} />
        })}
      </div>
      </div>
      <div>
        {(typeof data.flashcards === 'undefined') ? (
          <p>loading...</p>
        ) : (
          data.flashcards.map((member, i) => (
            <flashcard key={i}>{flashcards}</flashcard>
          ))
        )}
      </div>
    </>
  );
}