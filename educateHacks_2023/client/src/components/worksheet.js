import React from 'react'
import {Typography} from '@mui/material';
import '../App.css'

export default function worksheet({ worksheet }) {
  return (
    <>
    <div className="card-grid">
        <h1>{worksheet[0][0]['id']}</h1>
        {worksheet[0].map((postDetail, index) => {
            return (
                <div className="worksheet-problem-list">
                    <p className="worksheet-problem">{postDetail.id}, {postDetail.question}, {postDetail.answer}</p>
                </div>
            )
            
        })}
      </div>
    </>
  )
}