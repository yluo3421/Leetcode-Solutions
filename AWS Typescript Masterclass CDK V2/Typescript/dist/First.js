var a = 'hello';
var someArray = [];
someArray.push(a);
console.log(a);
;
function generateEmail(input, force) {
    if (input.isVisitor && !force) {
        return undefined;
    }
    else {
        return `${input.firstName}.${input.lastName}@email.com`;
    }
}
;
console.log(generateEmail({
    firstName: 'John',
    lastName: 'Doe',
    job: 'Engineer',
    isVisitor: true
}, true));
function isPerson(potentialPerson) {
    if ('firstName' in potentialPerson &&
        'lastName' in potentialPerson) {
        return true;
    }
    else {
        return false;
    }
}
function printEmailIfPerson(potentialPerson) {
    if (isPerson(potentialPerson)) {
        console.log(generateEmail(potentialPerson));
    }
    else {
        console.log('Input is not a person');
    }
}
printEmailIfPerson({
    firstName: 'John',
    lastName: 'Doe'
});
