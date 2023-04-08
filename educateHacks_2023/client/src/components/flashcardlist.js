import React from 'react'
import Flashcard from './flashcard';

export default function FlashcardList({ flashcards }) {
  return (
    <div className="card-grid">
        {(flashcards.length == 0) ? (
          <p>Flashcards not yet Generated</p>
        ) : (
          flashcards.map(flashcard => {
            return <Flashcard flashcard={flashcard} key={flashcard.id} />
          })
        )}
      </div>
  )
}
