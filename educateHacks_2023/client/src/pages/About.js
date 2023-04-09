import Header from '../components/Header.js'
import { Box, Container, Typography, Stack, Button, Grid, Card, CardContent, CardActions } from '@mui/material'


export function About() {
    return (
        <>
        <div>
          <Header />
          <div className="about-background">
          <Box sx={{mt: 0}} className="body-content">
            <Container fixed >
            <Typography
            sx = {{mt: 5}}
              component="h1"
              variant="h2"
              align="center"
              color="text.primary"
              gutterBottom
              fontFamily={'jetbrains mono'}
            >
              About GenieLearn
            </Typography>
            <Typography variant="h5" align="center" color="text.secondary" paragraph>
              The all-in-one AI teaching tool
            </Typography>
            <Stack
              sx={{ pt: 0 }}
              direction="row"
              spacing={2}
              justifyContent="center"
            >
            </Stack>
            <h1></h1>
            <h1></h1>
            <Typography
            sx = {{mt: 5}}
              component="h4"
              variant="h4"
              align="center"
              color="text.primary"
              gutterBottom
              fontFamily={'jetbrains mono'}
            >
              Goal
            </Typography>
            <Typography variant="h5" align="center" color="text.secondary" paragraph>
                Teachers we interviewed indicated that they spend too much time on repetitive things like coming up with practice problems, or meterials for studying for exams. We wanted to help these teachers leverage the power of Artificial intelligence to automate these menial tasks.
            </Typography>
            <Typography
            sx = {{mt: 5}}
              component="h4"
              variant="h4"
              align="center"
              color="text.primary"
              gutterBottom
              fontFamily={'jetbrains mono'}
            >
              Flashcards
            </Typography>
            <Typography variant="h5" align="center" color="text.secondary" paragraph>
                Flashcards are one the best ways to memorize information for exams. On the flashcards page, students and teachers alike can input the topic they wish to study and flashcards will be generated on the topic.
            </Typography>
            <Typography
            sx = {{mt: 5}}
              component="h4"
              variant="h4"
              align="center"
              color="text.primary"
              gutterBottom
              fontFamily={'jetbrains mono'}
            >
              Worksheets
            </Typography>
            <Typography variant="h5" align="center" color="text.secondary" paragraph>
                For exams which dont require memorization, hands on experience is the best way to prepare. On the worksheets page, students can generate practice problems for their upcoming tests, or teachers can generate worksheets for their students. 
            </Typography>
            <p className="white-text">rgergreg</p>
          </Container>
          </Box>
          </div>
        </div>
    </>
    )
}