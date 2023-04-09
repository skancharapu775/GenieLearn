import Header from '../components/Header.js'
import { Container, Typography, Stack, Button } from '@mui/material'
import { Card, CardContent, CardActions, Grid } from '@mui/material'
import { Box } from '@mui/system'
import React from 'react'


export function Home() {
    return (
        <>
        <Header />
        <div className="body-background">
        <Box sx={{mt: 0}} className="body-content">

            <h3></h3>
            <Container fixed >
            <Typography
              component="h1"
              variant="h1"
              align="center"
              color="text.primary"
              gutterBottom
              fontFamily={'jetbrains mono'}
            >
              GenieLearn
            </Typography>
            <Typography variant="h5" align="center" color="text.secondary" paragraph>
              The <b>magical</b>, all-in-one  AI teaching tool
            </Typography>
            <Stack
              sx={{ pt: 0 }}
              direction="row"
              spacing={2}
              justifyContent="center"
            >
              <Button href='/flashcards' variant="contained">Learn with AI</Button>
              <Button href='/about' variant="outlined">About</Button>
            </Stack>
            <h1></h1>
            <h1></h1>
            <Typography
            sx = {{mt: 10}}
              component="h4"
              variant="h4"
              align="center"
              color="text.primary"
              gutterBottom
              fontFamily={'jetbrains mono'}
            >
              Features
            </Typography>
            <Typography variant="h5" align="center" color="text.secondary" paragraph>
                Speed up studying or teaching with our AI-powered features
            </Typography>
            {/* create 3 inline cards */}
            <Grid container spacing={2} sx={{justifyContent: 'center'}}>
                <Grid item xs={12} sm={4}>
                    <Card sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
                        <CardContent sx={{ flexGrow: 1 }}>
                            <Typography gutterBottom variant="h5" component="h2">
                                Flashcards
                            </Typography>
                            <Typography>
                                One of the best ways to learn new information is through flash cards. Here you can specify a topic and an AI will create flashcards for you.
                            </Typography>
                        </CardContent>
                        <CardActions>
                            <Button href="/flashcards" size="small">View</Button>
                        </CardActions>
                    </Card>
                </Grid>
                <Grid item xs={12} sm={4}>
                    <Card sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
                        <CardContent sx={{ flexGrow: 1 }}>
                            <Typography gutterBottom variant="h5" component="h2">
                                Worksheets
                            </Typography>
                            <Typography>
                                There is no substitute for hands on experience during exams. Here you can specify a topic and an AI will create worksheets for you.
                            </Typography>
                        </CardContent>
                        <CardActions>
                            <Button href="/worksheets" size="small">View</Button>
                        </CardActions>
                    </Card>
                </Grid>
            </Grid>
          </Container>
          <h3></h3>
          <h3></h3>
          <h3></h3>
          <h3></h3>
          <h3></h3>
        </Box>
        </div>
    </>
    )
}