var React = require('react')
var auth = require('./auth')
import Nav from './components/Nav'
import React, {Component} from 'react'

function LogoutButton(props) {
    return (
        <li>
            <a onClick={props.logout}>
                    <span className="glyphicon glyphicon-log-out"></span>
                     &nbsp; Logout
            </a>
        </li>
    )
}

function LoginLogoutButton(props) {
    var loginButton
    if(props.login == "true")
       loginButton = (
           <li>
            <a href="/mainapp/user/">
                <span className="glyphicon glyphicon-log-in"></span>
                 &nbsp; Login
            </a>
        </li>
       )
    else {
        loginButton = (
            <li>
                <a href={props.destination}>
                    <span className="glyphicon glyphicon-log-out"></span>
                     &nbsp; Logout
                </a>
            </li>
        )
    }
    return (
       loginButton
    )
}

function NavigationMenuButton(props) {
    return (
        <li><a href={props.destination}>{props.name}</a></li>
    )
}

function NavigationMenu (props) {
    return (
        <div className="collapse navbar-collapse" id="myNavbar">
            <ul className="nav navbar-nav">
                <NavigationMenuButton name="PLACEHOLDER" destination="#"/>
            </ul>
            <ul className="nav navbar-nav navbar-right">
                <LoginLogoutButton login={props.login} destination="#"/>
            </ul>
        </div>
    );
}

function NavigationHomeButton() {
    return (
        <div className="navbar-header">
            <button type="button" className="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                <span className="icon-bar"></span>
                <span className="icon-bar"></span>
                <span className="icon-bar"></span>
              </button>
              <a className="navbar-brand" href="/mainapp/home/">E-Elections</a>
        </div>
    )
}

class NavigationBar extends Component {
    render() {
        return (
            <nav className="navbar navbar-inverse menu">
                <div className="container-fluid">
                    <NavigationHomeButton />
                    <NavigationMenu login={this.props.login} />
                </div>
            </nav>
        )
    }
}

function ElectionList(props) {
    const listItems = props.list.map((e) =>
        <li key={e.election.toString()}>
            <a>{e.election}</a>
        </li>
    )
    return (
        <div>
            <ul>
                {listItems}
            </ul>
        </div>
    )
}

module.exports = React.createClass({
   getInitialState: function() {
        return {'user':[], 'elections':[]}
    },

    componentDidMount: function() {
        this.loadUserData()
    },
            
    contextTypes: {
        router: React.PropTypes.object.isRequired
    },

    logoutHandler: function() {
        auth.logout()
        this.context.router.replace('/app/login/')
    },

    loadUserData: function() {
       $.ajax({
            method: 'GET',
            url: '/mainapp/users/i/',
            datatype: 'json',
            headers: {
                'Authorization': 'Token ' + localStorage.token
            },
            success: function(res) {
                this.setState({user: res})
            }.bind(this)
        })
        $.ajax({
            method: 'GET',
            url: '/mainapp/user-elections/i/',
            datatype: 'json',
            headers: {
                'Authorization': 'Token ' + localStorage.token
            },
            success: function(res) {
                console.log(res)
                this.setState({elections: res})
            }.bind(this)
        })
        // var myHeaders = new Headers()
        // myHeaders.append('Authorization', 'Token ' + localStorage.token)
        // let jsonData
        // var myInit = {
        //     method: 'GET',
        //     headers: myHeaders,
        //     mode: 'cors',
        //     cache: 'default'
        // }
        // fetch('/mainapp/users', myInit).then(function(response) {
        //     return response.json()
        // }).then(function(j) {
        //     jsonData = j.results
        // }).catch(function(err) {
	     //    console.log('error')
        // });
        // this.setState({user: jsonData})
        // console.log(this.state.user)
    },

    render: function() {
        return (
            <div>
                <nav className="navbar navbar-inverse menu">
                    <div className="container-fluid">
                        <NavigationHomeButton />
                        <div className="collapse navbar-collapse" id="myNavbar">
                            <ul className="nav navbar-nav">
                                <NavigationMenuButton name="PLACEHOLDER" destination="#"/>
                            </ul>
                            <ul className="nav navbar-nav navbar-right">
                                <LogoutButton logout={this.logoutHandler} />
                            </ul>
                        </div>
                    </div>
                </nav>
                <h1>You are now logged in {this.state.user.username}</h1>
                <h2>You can vote on these elections</h2>
                <ElectionList list={this.state.elections} />
            </div>
        )        
    }
})
