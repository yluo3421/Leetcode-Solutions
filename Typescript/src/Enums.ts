enum AuthError {
    WRONG_CREDENTIALS,
    SERVER_FAIL,
    EXPRIED_SESSION
}

console.log(AuthError.WRONG_CREDENTIALS)

enum AuthError2 {
    WRONG_CREDENTIALS = 'wrong credentials',
    SERVER_FAIL = 'server fail',
    EXPRIED_SESSION = 'expired session'
}

function handleError(error: AuthError){
    switch (error) {
        case AuthError.EXPRIED_SESSION:
            console.log('Get a new session!')
            break;
        case AuthError.SERVER_FAIL:
            console.log('Restart the server.')
            break;
        case AuthError.WRONG_CREDENTIALS:
            console.log('check your input@')
            break;
        default:
            break;
    }
}

handleError(AuthError.EXPRIED_SESSION);