import React from 'react'
import {Typography} from '@mui/material';
import '../App.css'
import { Grid, Button } from '@mui/material';
import '../Style_Cards.css'
import { useState } from 'react';



export default function Worksheet({ worksheet }) {
    const [showText, setShowText] = useState(false);

    return (
   
  <>
    <div className="worksheet-problem-list">
    <Button  onClick={() => setShowText(!showText)}>Reveal Answers</Button></div>
        {worksheet[0].map((postDetail, index) => {
            return (
                <div className="worksheet-problem-list">
                    <Grid>
                        <h2> Problem Number {postDetail.id}</h2>
                        <p>{postDetail.question}</p>
                        <React.Fragment>
                            {showText && <p>Answer: <b>{postDetail.answer}</b></p>}
                        </React.Fragment>
                    </Grid>
                </div>
            )
            
        })}
        <a href="http://localhost:5000/pdf" target="_blank" download="Practice_Worksheet.pdf">
            <Button variant="contained">Download PDF</Button>
        </a>
    </>
  )
}