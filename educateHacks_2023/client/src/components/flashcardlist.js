import React from 'react'
import Flashcard from './flashcard'
import {Typography} from '@mui/material';
import '../App.css'

export default function FlashcardList({ image, flashcards }) {
  console.log('image', image)
  return (
    <div>
      <img className="hide-text" width='200px' src={image}/>
      <div className="card-grid">
          {(flashcards.length == 0) ? (
            <>
            <p className="white-text">werwerwer</p>
            <p className="white-text">werwerwer</p>
            <p className="white-text">werwerwer</p>
            <p className="white-text">werwerwer</p>
            <p className="white-text">werwerwer</p>
            <p className="white-text">werwerwer</p>
            </>
          ) : (
            flashcards.map(flashcard => {
              return <Flashcard className="flashcard" flashcard={flashcard} key={flashcard.id} />
            })
          )}
        </div>
    </div>
  )
}
