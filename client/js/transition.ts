import anime from 'animejs';


type TransitionNavigation = {
	from: URL,
	to: URL
};

type TransitionState = {
	ongoing: boolean;
};

class Transition {

	private linkSelector: string = 'a[href^="/"]';

	private state: TransitionState = {
		ongoing: false
	};

	private target: HTMLDivElement = document.querySelector('.page-transition-layer');

	private get links(): HTMLAnchorElement[] {
		return [...document.querySelectorAll(this.linkSelector) as any];
	}

	public register(): void {
		window.addEventListener('popstate', this.reloadPage);
		this.links.forEach(link => link.addEventListener('click', this.onNavigate));
	}

	public destroy(): void {
		window.removeEventListener('popstate', this.reloadPage);
		this.links.forEach(link => link.removeEventListener('click', this.onNavigate));
	}

	private onNavigate = (event: MouseEvent): void => {
		event.preventDefault();
		event.stopPropagation();

		const link = this.eventIntoLink(event);

		if (!link) return;

		this.handleNavigation({
			to: new URL(link.href),
			from: new URL(window.location.href)
		});
	}

	private eventIntoLink(event: MouseEvent): HTMLAnchorElement | null {
		const target = event.target as HTMLElement;

		if (target.tagName !== 'A') {
			const closest = target.closest('a');
	
			if (!closest) return null;
	
			return closest;
		}
	
		return target as HTMLAnchorElement;
	}

	public async handleNavigation(navigation: TransitionNavigation): Promise<void> {
		const dom = await this.fetchDom(navigation.to);

		if (this.state.ongoing) return;

		this.state.ongoing = true;

		await anime({
			targets: this.target,
			translateX: ['-100vw', '0vw'],
			duration: 500,
			easing: 'easeInOutCubic'
		}).finished;

		this.destroy();
		this.replaceDom(dom, navigation.to);
		this.register();

		await anime({
			targets: this.target,
			translateX: ['0vw', '100vw'],
			duration: 500,
			easing: 'easeInOutCubic'
		}).finished;

		this.state.ongoing = false;
	}

	private async fetchDom(url: URL): Promise<Document> {
		const next = await fetch(url.pathname);
		const markup = await next.text();
		const dom = new DOMParser().parseFromString(markup, "text/html");

		return dom;
	}

	private replaceDom(dom: Document, newLocation: URL): void {
		document.head.innerHTML = dom.head.innerHTML;
		document.body.querySelector('nav').innerHTML = dom.body.querySelector('nav').innerHTML;
		document.body.querySelector('main').innerHTML = dom.body.querySelector('main').innerHTML;
		window.history.pushState({}, dom.title, newLocation.toString());
	}

	private reloadPage(): void {
		window.location.reload();
	}

}


export default new Transition();
