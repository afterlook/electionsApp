import React, {Component} from 'react'
import Nav from './components/Nav'

class GuestPage extends Component {
    render() {
        return (
            <div>
                <Nav login="true"/>
                <h1>Welcome</h1>
            </div>
        )
    }
}

export default GuestPage