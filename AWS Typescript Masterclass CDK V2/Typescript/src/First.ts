var a = 'hello';
var someArray: string[] = [];
someArray.push(a);


console.log(a)

interface Person {
    firstName: string,
    lastName: string,
    job?: job,
    isVisitor?: boolean
};


type job = 'Engineer' | 'Programmer';
function generateEmail(input: Person, force?: boolean): string | undefined{
    if (input.isVisitor && !force) {
        return undefined
    } else {
        return `${input.firstName}.${input.lastName}@email.com`
    }
    
};

console.log(generateEmail({
    firstName: 'John',
    lastName: 'Doe',
    job: 'Engineer',
    isVisitor: true
}, true));

function isPerson(potentialPerson: any): boolean {
    if ('firstName' in potentialPerson &&
        'lastName' in potentialPerson) {
            return true
    } else {
        return false
    }
}

function printEmailIfPerson(potentialPerson: any): void{
    if (isPerson(potentialPerson)) {
        console.log(generateEmail(potentialPerson))
    } else {
        console.log('Input is not a person')
    }
}
printEmailIfPerson({
    firstName: 'John',
    lastName: 'Doe'
})