import React, { Component } from 'react';
import axios from 'axios';

class PostForm extends Component {
    constructor(props) {
        super(props);

        this.state = {
            number: '',
            topic: ''
        };
    }

    //keep form values updated
    changeHandler = (e) => {
        this.setState({ [e.target.name]: e.target.value })
    }

    //runs when submit button is pressed
    submitHandler = (e) => {
        e.preventDefault();
        console.log(this.state);
        axios.post('http://localhost:5000/flashcards', this.state)
            .then(response => {
                console.log(response);
            })
            .catch(error => {
                console.log(error);
            })
    }

    render() {
        const { number, topic } = this.state;
        return (
            <div>
                <form onSubmit={this.submitHandler}>
                    <label>
                    Number:
                        <input type="text" name="number" value={number} onChange={this.changeHandler} />
                    </label>
                    <label>
                        Topic:
                        <input type="text" name="topic" value={topic} onChange={this.changeHandler} />
                    </label>
                    <input type="submit" value="Submit" />
                </form>
            </div>
        )
    }
}

export  default PostForm;