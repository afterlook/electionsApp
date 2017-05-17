import React, {Component} from 'react'

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
                    <NavigationMenu login={this.props.login}/>
                </div>
            </nav>
        )
    }
}

export default NavigationBar;