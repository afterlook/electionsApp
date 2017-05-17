var React = require('react')
var auth = require('./auth')
import Nav from './components/Nav'

module.exports = React.createClass({
    contextTypes: {
        router: React.PropTypes.object.isRequired
    },

    handleSubmit: function(event) {
        event.preventDefault()

        var username = this.refs.username.value
        var pass = this.refs.pass.value

        auth.login(username, pass, (loggedIn) => {
            this.context.router.replace('/mainapp/home/')
        })
    },

    render: function() {
        return (
            <div>
                <Nav login="true"/>
                <h1>To accesss content of this page you must either login or register</h1>
                <form onSubmit={this.handleSubmit}>
                    <input name="username" type="text" placeholder="username" ref="username"/> <br/>
                    <input name="pass" type="password" placeholder="password" ref="pass"/> <br />
                    <input type="submit"/>
                </form>
            </div>
        )
    }
})
