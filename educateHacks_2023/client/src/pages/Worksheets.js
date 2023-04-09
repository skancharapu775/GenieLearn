import Header from '../components/Header.js'
import PostForm from '../components/postform.js'
import React, { useState, useEffect, useRef } from 'react'
import { Box, TextField, Button, Typography } from '@mui/material'
import Worksheet from '../components/Worksheet.js'
import axios from 'axios'
import '../Style_Cards.css'
import '../App.css'


export function Worksheets() {
    const SAMPLE_WORKSHEET = [
        [
            {
                'id': 1,
                'question': 'Question: What is the value of x if 2x + 5 = 11?',
                'answer_id': 1, 'options': [], 'answer': 'x = 3'
            },
            {
                'id': 2,
                'question': 'Question: If a rectangular garden is 10 meters long and has a perimeter of 36 meters, what is the width of the garden?',
                'answer_id': 2, 'options': [], 'answer': 'The width of the garden is 8 meters'
            }
        ],
        [
                {
                    'id': 1,
                    'question_id': 1
                },
                {
                    'id': 2,
                    'question_id': 2
                }
        ]
    ]
    //post stuff
    const [worksheet, setWorksheet] = useState([])

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
        //setWorksheet(SAMPLE_WORKSHEET)
        // console.log('test')
        e.preventDefault()
        console.log(post)
        axios.post('http://localhost:5000/worksheets', post)
        .then(res => {
            axios.get('http://localhost:5000/worksheets')
            .then(res => {
            console.log("This is the output from the server:")
            console.log(res.data["results"]) //this is in same format as SAMPLE_WORKSHEET
            setWorksheet(res.data["results"])
            }, [])
        })
        .catch(err => {
          console.log(err)
        })
      }

  return (
    
    <>
    <Header />
    <div className="worksheets-background">
    <Box sx={{mt: 0}} className="body-content">
    <Box sx = {{mt: 2}} className="flashcard-form">
            <Typography
                component="h1"
                variant="h2"
                align="center"
                color="text.primary"
                gutterBottom
                fontFamily={''}
              >
                Generate Worksheet with AI
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
        {(worksheet.length == 0) ? (
          <>
            <p className="white-text">werwerwer</p>
            <p className="white-text">werwerwer</p>
            <p className="white-text">werwerwer</p>
            <p className="white-text">werwerwer</p>
            <p className="white-text">werwerwer</p>
            <p className="white-text">werwerwer</p>
            <p className="white-text">werwerwer</p>
            <p className="white-text">werwerwer</p>
            <p className="white-text">werwerwer</p>
          </>
        ) : (
            <Worksheet worksheet={worksheet} />
        )}
    </Box>
    </Box>
    </div>
    </>
  );
}