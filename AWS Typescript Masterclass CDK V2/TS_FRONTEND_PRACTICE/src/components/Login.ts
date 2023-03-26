


export class Login {
    private container = document.createElement('div')
    render(){
        const pageLabel = document.createElement('label');
        pageLabel.innerText = 'Welcome to the Login Page!';
        this.container.append(pageLabel);
        return this.container
    }
}