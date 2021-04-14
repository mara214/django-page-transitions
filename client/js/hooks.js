import {handlePageTransition} from './transition';


const getLinks = () => [...document.querySelectorAll('a[href^="/"]')];

export function startup() {
	console.log("started app")
	getLinks().map(link => link.addEventListener('click', handlePageTransition));
}

export function teardown() {
	console.log("closed app")
	getLinks().map(link => link.removeEventListener('click', handlePageTransition));
}
