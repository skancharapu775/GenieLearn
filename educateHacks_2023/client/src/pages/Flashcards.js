import Header from '../components/Header.js'
import PostForm from '../components/postform.js'
import React, { useState, useEffect, useRef } from 'react'
import Flashcard from '../components/flashcard.js'
import FlashcardList from '../components/FlashcardList.js'
import { Box, TextField, Button, Typography } from '@mui/material'
import axios from 'axios'
import '../Style_Cards.css'
import '../App.css'


export function Flashcards() {

  const [flashcards, setFlashcards] = useState([])
  const [image, setImage] = useState([])
  const [loading, setLoading] = useState(false)
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
      axios.get('http://localhost:5000/flashcards')
      .then(res => {
        console.log('res.data.url', res.data.url)
        setImage(res.data.url)
      })
    })
    .catch(err => {
      console.log(err)
    })
  }



  return (
    
    <>
    <Header />
        <div className="flashcards-background">
        <Box sx={{mt: 0}} className="body-content">
            <h3></h3>
            <div className="flashcard-form">
              <Typography
                component="h1"
                variant="h2"
                align="center"
                color="text.primary"
                gutterBottom
                fontFamily={''}
              >
                Generate Flashcards with AI
              </Typography>
              <form onSubmit={submitHandler} noValidate autoComplete="off"> 
                  <TextField
                  margin="normal"
                  value={post.number}
                  onChange={changeHandler}
                  required
                  fullWidth
                  id="number"
                  label="Number"
                  name="number"
                  autoComplete="off"
                  />
                  <TextField
                  margin="normal"
                  required
                  fullWidth
                  id="topic"
                  label="Topic"
                  name="topic"
                  value={post.topic}
                  onChange={changeHandler}
                  autoComplete="off"
                  />
                  <Box textAlign='center'>
                      <Button variant='contained' type="submit" >Generate</Button>
                  </Box>
              </form>
              <div className="container">
                <FlashcardList image={image} flashcards={flashcards} />
              </div>
            </div>
        </Box>
        </div>
    </>
  );
}