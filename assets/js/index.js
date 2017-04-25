var React = require('react')
var ReactDOM = require('react-dom')

fetch('/mainapp/user-list').then(function(response) {
    return response.json()
}).then(function(j) {
    j.results.forEach(function(element) {
        console.log(element.username);
    });
}).catch(function(err) {
	console.log('error: did not read user json')
});