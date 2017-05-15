var React = require('react')
var ReactDOM = require('react-dom')

// // fetch('/mainapp/user-list').then(function(response) {
// //     return response.json()
// // }).then(function(j) {
// //     j.results.forEach(function(element) {
// //         console.log(element.username);
// //     });
// // }).catch(function(err) {
// // 	console.log('error: did not read user json')
// // });
//

/*
Probably will be changed to class becouse of its
more advanced functionality and integration with django.
This is just a dummy button that is very similar to NavigationMenuButton.
*/
function LoginLogoutButton(props) {
    return (
        <li>
            <a href={props.destination}>
                <span className="glyphicon glyphicon-log-in"></span>
                {props.name}
            </a>
        </li>
    )
}

function NavigationMenuButton(props) {
    return (
        <li><a href={props.destination}>{props.name}</a></li>
    )
}

function NavigationMenu () {
    return (
        <div className="collapse navbar-collapse" id="myNavbar">
            <ul className="nav navbar-nav">
                <NavigationMenuButton name="PLACEHOLDER" destination="#"/>
            </ul>
            <ul className="nav navbar-nav navbar-right">
                <LoginLogoutButton name=" Login" destination="#"/>
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
              <a className="navbar-brand" href="#">E-Elections</a>
        </div>
    )
}

function NavigationBar() {
    return (
        <nav className="navbar navbar-inverse menu">
            <div className="container-fluid">
                <NavigationHomeButton/>
                <NavigationMenu/>
            </div>
        </nav>
    )
}

function App() {
  return (
    <div id="container">
        <NavigationBar/>
    </div>
  );
}

if(document.getElementById('container')) {
    ReactDOM.render(
        <App />,
        document.getElementById('container')
    );
}