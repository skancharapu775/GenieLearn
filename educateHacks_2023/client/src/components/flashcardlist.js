import React from 'react'
import Flashcard from './flashcard'
import {Typography} from '@mui/material';
import '../App.css'

export default function FlashcardList({ flashcards }) {
  return (
    <div className="card-grid">
        {(flashcards.length == 0) ? (
          <></>
        ) : (
          flashcards.map(flashcard => {
            return <Flashcard className="flashcard" flashcard={flashcard} key={flashcard.id} />
          })
        )}
      </div>
  )
}
