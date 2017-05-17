var React = require('react')
var ReactDOM = require('react-dom')
var auth = require('./auth')
var Login = require('./login')
var App = require('./app')
import { Router, Route, Link, browserHistory } from 'react-router'

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
// class LoginLogoutButton extends React.Component {
//     constructor(props) {
//         super(props)
//         this.state = {isLoggedIn: false}
//     }
// }


// function App() {
//   return (
//     <div id="container">
//         <Nav/>
//     </div>
//   );
// }

function requireAuth(nextState, replace) {

    if (!auth.loggedIn()) {
        replace({
            pathname:'/app/login/',
            state: {nextPathname: '/mainapp/home/'}
        })
    }
}



if(document.getElementById('container')) {
    ReactDOM.render(
        <Router history={browserHistory}>
            <Route path='/app/login/' component={Login} />
            <Route path='/mainapp/home/' component={App} onEnter={requireAuth} />
        </Router>,
        document.getElementById('container')
    );
}
