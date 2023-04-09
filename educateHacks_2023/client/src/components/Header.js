import postform from './postform.js'
import { AppBar, Toolbar, IconButton, Typography, Stack, Button } from '@mui/material';
import Box from '@mui/material/Box';
import SchoolIcon from '@mui/icons-material/School';
import '../App.css';

export default function Header() {
    return (
        <Box sx={{ flexGrow: 1 }}>
            <div className='header'>
                <AppBar position='static'>
                    <Toolbar>
                        <IconButton size='large' edge='start' color='inherit' aria-label='logo'>
                            <SchoolIcon href="/home" />
                        </IconButton>
                        <Typography variant='h6' component='div' sx={{ flexGrow: 0 }}>
                            GenieLearn
                        </Typography>
                        <Stack direction='row' spacing = {1}>
                            <Button color='inherit' href='/home'></Button>
                            <Button color='inherit' href='/home'>Home</Button>
                            <Button color='inherit' href='/about'>About</Button>
                            <Button color='inherit' href='/flashcards'>Flashcards</Button>
                            <Button color='inherit' href='/worksheets'>Worksheets</Button>
                        </Stack>
                    </Toolbar>
                </AppBar>
            </div>
        </Box>
    )
}