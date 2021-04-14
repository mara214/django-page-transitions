import anime from 'animejs';

import { startup, teardown } from './hooks';


const pageTransitionLayer = document.querySelector('.page-transition-layer');


function linkElementFromEvent(event) {
	if (event.target.tagName !== 'A') {
		const closest = event.target.closest('a');

		if (!closest) return null;

		return closest;
	}

	return event.target;
}

window.pageTransitionState = {
	ongoing: false
};

export async function handlePageTransition(event) {
	event.preventDefault();

	const link = linkElementFromEvent(event);

	if (!link) return;

	const next = await fetch(link.pathname);
	const markup = await next.text();
	const dom = new DOMParser().parseFromString(markup, "text/html");

	if (window.pageTransitionState.ongoing) return;

	window.pageTransitionState.ongoing = true;

	anime({
		targets: pageTransitionLayer,
		translateX: ['-100vw', '0vw'],
		opacity: 1,
		duration: 500,
		easing: 'easeInOutCubic',
		complete: () => {
			teardown();

			document.head.innerHTML = dom.head.innerHTML;
			document.body.querySelector('nav').innerHTML = dom.body.querySelector('nav').innerHTML;
			document.body.querySelector('main').innerHTML = dom.body.querySelector('main').innerHTML;
			window.history.pushState({}, dom.title, new URL(link.pathname, link.baseURI));

			startup();

			anime({
				targets: pageTransitionLayer,
				translateX: ['0vw', '100vw'],
				duration: 500,
				easing: 'easeInOutCubic',
				complete: () => {
					window.pageTransitionState.ongoing = false;
				}
			});
		}
	})
}