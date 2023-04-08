import Header from '../components/Header.js'
import PostForm from '../components/postform.js'
import React, { useState, useEffect, useRef } from 'react'
import Flashcard from '../components/flashcard.js'
import FlashcardList from '../components/FlashcardList.js'
import axios from 'axios'
import '../Style_Cards.css'


export function Flashcards() {

  const [flashcards, setFlashcards] = useState([])
  //flask api stuff
  
  // we expect data from flask API to look like this
  //SAMPLE_FLASHCARDS = [{"id": 1, "question": "What is 2 + 2?", "answer": "4", "options": ["2", "3", "4", "5"]}, {"id": 2, "question": "questions", "answer": "no", "options": ["yes", "no"]}]

  useEffect(() => {
    axios.get('http://localhost:5000/flashcards')
    .then(res => {
      res.data.results.map((questionItem, index) => {
      })
      setFlashcards(res.data.results)
      
    })
  }, [])

  //create object to hold number and topic
  const [post, setPost] = useState({
    number: '',
    topic: ''
  })

  //create function to handle change in input by updating number and topic
  const changeHandler = e => {
    setPost({
      ...post,
      [e.target.name]: e.target.value
    })
  }

  //create function to handle submit
  const submitHandler = e => {
    e.preventDefault()
    axios.post('http://localhost:5000/flashcards', post)
    .then(res => {
        axios.get('http://localhost:5000/flashcards')
      .then(res => {
        res.data.results.map((questionItem, index) => {
        })
        setFlashcards(res.data.results)
        
      })
    })
    .catch(err => {
      console.log(err)
    })
  }



  return (
    
    <>
    <Header />
    
            <div>
                <form onSubmit={submitHandler}>
                    <label>
                    Number:
                        <input type="text" name="number" value={post.number} onChange={changeHandler} />
                    </label>
                    <label>
                        Topic:
                        <input type="text" name="topic" value={post.topic} onChange={changeHandler} />
                    </label>
                    <input type="submit" value="Submit" />
                </form>
            </div>
      <div className="container">
        <FlashcardList flashcards={flashcards} />
      </div>
    </>
  );
}